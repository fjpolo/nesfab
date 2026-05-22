import os
from PIL import Image, ImageEnhance, ImageOps

media_dir = r"C:\Users\polo\.gemini\antigravity\brain\0fbfe38a-f0ab-4aab-9a1f-9a2a210d8dcc"

files1 = [
    "media__1779373733930.png", # 0. Text: "It is not the sun rising..."
    "media__1779373763356.png", # 1. Text: "Because it is my Guilt..."
    "media__1779373779346.png", # 2. Artwork: Woman praying wide
    "media__1779373793162.png", # 3. Text: "Make my chest hurt..."
    "media__1779373831792.png"  # 4. Artwork: Close up woman + "Forge your punishment..."
]

files2 = [
    "media__1779374073793.png", # 5. Text: "Shape my Guilt, once again."
    "media__1779374099535.png", # 6. Artwork: Close up of woman striking her breast
    "media__1779374114769.png", # 7. Artwork: Sword pierces her breast with blood
    "media__1779374144411.png", # 8. Artwork: Penitent One pulling sword out of the statue
    "media__1779374168774.png", # 9. Artwork: The Crucified pose / ending statue scene
    "media__1779374930079.png"  # 10. Artwork: Penitent One lying on pile of corpses (Final Frame!)
]

all_files = files1 + files2

# Exact NES Gothic 4-color palette order:
# 0: Black (0, 0, 0)
# 1: Deep Crimson (120, 24, 0)
# 2: Silver-Blue (148, 148, 252)
# 3: White (255, 255, 255)
colors = [
    (0, 0, 0),         # 0: Black
    (120, 24, 0),      # 1: Deep Crimson
    (148, 148, 252),   # 2: Silver-Blue
    (255, 255, 255)    # 3: White
]

# Cinematic resolution: 160x96 (20x12 tiles = 240 tiles total, fits under PPU 256-tile limit!)
target_w = 160
target_h = 96

def manual_quantize(im, dither=True):
    w, h = im.size
    
    if not dither:
        # Text cards: Force pure solid Black and White
        out_pixels = []
        for pixel in im.getdata():
            r, g, b = pixel[:3]
            lum = 0.299 * r + 0.587 * g + 0.114 * b
            if lum > 110:
                out_pixels.append(3) # White
            else:
                out_pixels.append(0) # Black
    else:
        # Floyd-Steinberg Dithering manually mapped to our exact palette index values
        px = [list(im.getpixel((x, y))[:3]) for y in range(h) for x in range(w)]
        out_pixels = [0] * (w * h)
        
        for y in range(h):
            for x in range(w):
                idx = y * w + x
                old_r, old_g, old_b = px[idx]
                
                # Clamp values
                old_r = max(0.0, min(255.0, old_r))
                old_g = max(0.0, min(255.0, old_g))
                old_b = max(0.0, min(255.0, old_b))
                
                # Find closest color in palette
                best_color_idx = 0
                min_dist = float('inf')
                for c_idx, color in enumerate(colors):
                    r_c, g_c, b_c = color
                    dist = (old_r - r_c)**2 + (old_g - g_c)**2 + (old_b - b_c)**2
                    if dist < min_dist:
                        min_dist = dist
                        best_color_idx = c_idx
                
                out_pixels[idx] = best_color_idx
                
                # Distribute error
                fit_r, fit_g, fit_b = colors[best_color_idx]
                err_r = old_r - fit_r
                err_g = old_g - fit_g
                err_b = old_b - fit_b
                
                if x + 1 < w:
                    n_idx = idx + 1
                    px[n_idx][0] += err_r * 7 / 16
                    px[n_idx][1] += err_g * 7 / 16
                    px[n_idx][2] += err_b * 7 / 16
                if y + 1 < h:
                    if x - 1 >= 0:
                        n_idx = idx + w - 1
                        px[n_idx][0] += err_r * 3 / 16
                        px[n_idx][1] += err_g * 3 / 16
                        px[n_idx][2] += err_b * 3 / 16
                    n_idx = idx + w
                    px[n_idx][0] += err_r * 5 / 16
                    px[n_idx][1] += err_g * 5 / 16
                    px[n_idx][2] += err_b * 5 / 16
                    if x + 1 < w:
                        n_idx = idx + w + 1
                        px[n_idx][0] += err_r * 1 / 16
                        px[n_idx][1] += err_g * 1 / 16
                        px[n_idx][2] += err_b * 1 / 16

    # CRITICAL: Force the top-left 8x8 block (tile 0) of every single image to be 100% solid Black
    # This guarantees that tile index 0 is a perfect, clean, empty black tile for clearing the nametable!
    for ty in range(8):
        for tx in range(8):
            out_pixels[ty * w + tx] = 0
            
    # Create indexed image
    out_im = Image.new('P', (w, h))
    out_im.putdata(out_pixels)
    
    # Force exact palette table mapping
    palette_data = []
    for color in colors:
        palette_data.extend(color)
    palette_data.extend([0] * (768 - len(palette_data)))
    out_im.putpalette(palette_data)
    
    return out_im

for idx, f in enumerate(all_files):
    path = os.path.join(media_dir, f)
    im = Image.open(path).convert('RGB')
    
    is_text = idx in [0, 1, 3, 5]
    
    if is_text:
        # Crop closely to text
        gray = ImageOps.grayscale(im)
        thresh = gray.point(lambda p: 255 if p > 30 else 0)
        bbox = thresh.getbbox()
        if bbox:
            cropped = im.crop(bbox)
        else:
            cropped = im
            
        w, h = cropped.size
        # Make a wider padded canvas to match widescreen aspect ratio
        aspect_ratio = target_w / target_h
        padded_w = int(max(w, h * aspect_ratio))
        padded_h = int(padded_w / aspect_ratio)
        
        padded = Image.new('RGB', (padded_w, padded_h), (0, 0, 0))
        padded.paste(cropped, ((padded_w - w) // 2, (padded_h - h) // 2))
        
        # High contrast white on black
        enhanced = ImageEnhance.Contrast(padded).enhance(3.5)
        enhanced = ImageEnhance.Brightness(enhanced).enhance(1.6)
        
        resized = enhanced.resize((target_w, target_h), Image.Resampling.LANCZOS)
        mapped = manual_quantize(resized, dither=False)
    else:
        # Artwork: crop to widescreen aspect ratio 1.67:1 centered
        w, h = im.size
        scale = min(w / target_w, h / target_h)
        crop_w = int(target_w * scale)
        crop_h = int(target_h * scale)
        
        left = (w - crop_w) // 2
        top = (h - crop_h) // 2
        cropped = im.crop((left, top, left + crop_w, top + crop_h))
        
        # Grayscale pre-conversion for perfect luminance matching
        gray_im = ImageOps.grayscale(cropped)
        rgb_im = gray_im.convert('RGB')
        
        # High fidelity gothic boosting
        enhanced = ImageEnhance.Brightness(rgb_im).enhance(2.6)
        enhanced = ImageEnhance.Contrast(enhanced).enhance(2.1)
        
        resized = enhanced.resize((target_w, target_h), Image.Resampling.LANCZOS)
        mapped = manual_quantize(resized, dither=True)
        
    mapped.save(f'assets/silent_sorrow_{idx}.png')
    print(f"Successfully processed Frame {idx} ({f}) -> assets/silent_sorrow_{idx}.png")

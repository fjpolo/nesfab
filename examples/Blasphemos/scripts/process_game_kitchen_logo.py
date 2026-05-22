import os
from PIL import Image, ImageOps, ImageEnhance

media_dir = r"C:\Users\polo\.gemini\antigravity\brain\0fbfe38a-f0ab-4aab-9a1f-9a2a210d8dcc"
logo_file = "media__1779376118271.png"

colors = [
    (0, 0, 0),         # 0: Black
    (120, 24, 0),      # 1: Deep Crimson
    (148, 148, 252),   # 2: Silver-Blue
    (255, 255, 255)    # 3: White
]

target_w = 160
target_h = 96

def quantize_logo(im):
    w, h = im.size
    out_pixels = []
    for pixel in im.getdata():
        r, g, b = pixel[:3]
        lum = 0.299 * r + 0.587 * g + 0.114 * b
        if lum > 120:
            out_pixels.append(3) # White
        else:
            out_pixels.append(0) # Black

    # Force tile 0 (top-left 8x8 block) to be solid black
    for ty in range(8):
        for tx in range(8):
            out_pixels[ty * w + tx] = 0

    out_im = Image.new('P', (w, h))
    out_im.putdata(out_pixels)

    palette_data = []
    for color in colors:
        palette_data.extend(color)
    palette_data.extend([0] * (768 - len(palette_data)))
    out_im.putpalette(palette_data)
    
    return out_im

def process():
    path = os.path.join(media_dir, logo_file)
    if not os.path.exists(path):
        print(f"Error: logo file not found at {path}")
        return
        
    im = Image.open(path).convert('RGB')
    w, h = im.size
    
    # Crop/pad to widescreen aspect ratio (160x96)
    aspect_ratio = target_w / target_h
    if w / h > aspect_ratio:
        # Too wide, pad height
        new_h = int(w / aspect_ratio)
        padded = Image.new('RGB', (w, new_h), (0, 0, 0))
        padded.paste(im, (0, (new_h - h) // 2))
    else:
        # Too tall, pad width
        new_w = int(h * aspect_ratio)
        padded = Image.new('RGB', (new_w, h), (0, 0, 0))
        padded.paste(im, ((new_w - w) // 2, 0))
        
    resized = padded.resize((target_w, target_h), Image.Resampling.LANCZOS)
    mapped = quantize_logo(resized)
    
    output_path = "assets/game_kitchen_logo.png"
    mapped.save(output_path)
    print(f"Successfully processed logo -> {output_path}")

if __name__ == "__main__":
    process()

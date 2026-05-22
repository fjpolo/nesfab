import os
from PIL import Image, ImageOps, ImageEnhance

media_dir = r"C:\Users\polo\.gemini\antigravity\brain\0fbfe38a-f0ab-4aab-9a1f-9a2a210d8dcc"
f = "media__1779373779346.png" # Artwork: kneeling woman

path = os.path.join(media_dir, f)
im = Image.open(path).convert('RGB')

# Let's crop to a 160x112 aspect ratio (1.43:1) centered on the action
w, h = im.size
target_w, target_h = 192, 128
scale = min(w / target_w, h / target_h)
crop_w = int(target_w * scale)
crop_h = int(target_h * scale)

left = (w - crop_w) // 2
top = (h - crop_h) // 2
cropped = im.crop((left, top, left + crop_w, top + crop_h))

# Convert to grayscale first to reduce color noise
gray_im = ImageOps.grayscale(cropped)
rgb_im = gray_im.convert('RGB')

# High fidelity gothic boosting
enhanced = ImageEnhance.Brightness(rgb_im).enhance(2.6)
enhanced = ImageEnhance.Contrast(enhanced).enhance(2.1)

resized = enhanced.resize((target_w, target_h), Image.Resampling.LANCZOS)

# Direct Floyd-Steinberg dither to 4 colors
colors = [
    (0, 0, 0),         # 0: Black
    (120, 24, 0),      # 1: Deep Crimson
    (148, 148, 252),   # 2: Silver-Blue
    (255, 255, 255)    # 3: White
]

px = [list(resized.getpixel((x, y))[:3]) for y in range(target_h) for x in range(target_w)]
out_pixels = [0] * (target_w * target_h)

for y in range(target_h):
    for x in range(target_w):
        idx = y * target_w + x
        old_r, old_g, old_b = px[idx]
        
        old_r = max(0.0, min(255.0, old_r))
        old_g = max(0.0, min(255.0, old_g))
        old_b = max(0.0, min(255.0, old_b))
        
        best_color_idx = 0
        min_dist = float('inf')
        for c_idx, color in enumerate(colors):
            r_c, g_c, b_c = color
            dist = (old_r - r_c)**2 + (old_g - g_c)**2 + (old_b - b_c)**2
            if dist < min_dist:
                min_dist = dist
                best_color_idx = c_idx
        
        out_pixels[idx] = best_color_idx
        
        fit_r, fit_g, fit_b = colors[best_color_idx]
        err_r = old_r - fit_r
        err_g = old_g - fit_g
        err_b = old_b - fit_b
        
        if x + 1 < target_w:
            n_idx = idx + 1
            px[n_idx][0] += err_r * 7 / 16
            px[n_idx][1] += err_g * 7 / 16
            px[n_idx][2] += err_b * 7 / 16
        if y + 1 < target_h:
            if x - 1 >= 0:
                n_idx = idx + target_w - 1
                px[n_idx][0] += err_r * 3 / 16
                px[n_idx][1] += err_g * 3 / 16
                px[n_idx][2] += err_b * 3 / 16
            n_idx = idx + target_w
            px[n_idx][0] += err_r * 5 / 16
            px[n_idx][1] += err_g * 5 / 16
            px[n_idx][2] += err_b * 5 / 16
            if x + 1 < target_w:
                n_idx = idx + target_w + 1
                px[n_idx][0] += err_r * 1 / 16
                px[n_idx][1] += err_g * 1 / 16
                px[n_idx][2] += err_b * 1 / 16

# Count unique 8x8 tiles in this 160x112 image
unique_tiles = set()
for ty in range(0, target_h, 8):
    for tx in range(0, target_w, 8):
        tile_pixels = []
        for dy in range(8):
            for dx in range(8):
                tile_pixels.append(out_pixels[(ty + dy) * target_w + (tx + dx)])
        unique_tiles.add(tuple(tile_pixels))

print(f"Total tiles in grid: { (target_w // 8) * (target_h // 8) }")
print(f"Unique tiles: {len(unique_tiles)}")

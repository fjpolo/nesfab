from PIL import Image
import os

img_path = 'c:/Workspace/nesfab/nesfab/examples/Blasphemos/assets/bg1.png'
im = Image.open(img_path)
im_rgb = im.convert('RGB')
w, h = im.size

# Analyze tiles of 8x8
print(f"Image size: {w}x{h}")
tiles_colors = []
for ty in range(0, h, 8):
    for tx in range(0, w, 8):
        tile_pixels = []
        for y in range(8):
            for x in range(8):
                tile_pixels.append(im_rgb.getpixel((tx + x, ty + y)))
        # Count unique colors in tile
        unique_colors = set(tile_pixels)
        # Check if there are warm colors (R > 180, G > 100, B < 100) or similar
        warm = False
        for r, g, b in unique_colors:
            if r > 150 and g > 50 and b < 100:
                warm = True
        tiles_colors.append((tx, ty, len(unique_colors), warm, list(unique_colors)[:3]))

print("Tiles with warm colors (potential torches/candles/flames):")
for idx, (tx, ty, num_cols, warm, sample) in enumerate(tiles_colors):
    if warm and num_cols > 1:
        print(f"Tile {idx} at ({tx}, {ty}): {num_cols} colors, sample: {sample}")

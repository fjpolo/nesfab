import os
from PIL import Image

def get_tile_mask(img, tx, ty):
    # Convert an 8x8 tile to a binary mask (shape)
    # Background pixel is defined as the color at (tx, ty) or dark/black
    # Let's count unique colors in the tile
    pixels = []
    colors = set()
    for y in range(8):
        for x in range(8):
            color = img.getpixel((tx + x, ty + y))[:3]
            pixels.append(color)
            colors.add(color)
            
    # Find background color: usually the most common color or black/dark
    bg_color = img.getpixel((tx, ty))[:3]
    
    mask = []
    for p in pixels:
        # If it's the background color, it's 0, else 1
        if p == bg_color or sum(p) < 10:
            mask.append(0)
        else:
            mask.append(1)
    return tuple(mask)

def main():
    orig_font_path = "assets/font_orig.png"
    if not os.path.exists(orig_font_path):
        print("font_orig.png not found!")
        return
        
    font_img = Image.open(orig_font_path).convert("RGBA")
    
    # Generate shapes/masks for all 96 original font tiles
    font_masks = {}
    for char_idx in range(96):
        tile_col = char_idx % 16
        tile_row = char_idx // 16
        mask = get_tile_mask(font_img, tile_col * 8, tile_row * 8)
        # Skip empty tiles (all 0s) to avoid false matches
        if sum(mask) > 0:
            font_masks[mask] = char_idx
            
    print(f"Generated masks for {len(font_masks)} non-empty font characters.")
    
    # Scan target images
    targets = ["assets/bg1.png", "assets/bg2.png", "assets/sprite.png", "assets/sprite2.png"]
    for target in targets:
        if not os.path.exists(target):
            print(f"{target} does not exist!")
            continue
            
        img = Image.open(target).convert("RGBA")
        width, height = img.size
        print(f"\nScanning {target} ({width}x{height})...")
        
        matches = 0
        for row in range(height // 8):
            for col in range(width // 8):
                mask = get_tile_mask(img, col * 8, row * 8)
                if mask in font_masks:
                    char_idx = font_masks[mask]
                    char_repr = chr(char_idx + 32)
                    print(f"  Tile at col {col}, row {row} matches ASCII character '{char_repr}' (Tile {char_idx})")
                    matches += 1
        print(f"Total matching font tiles found in {target}: {matches}")

if __name__ == "__main__":
    main()

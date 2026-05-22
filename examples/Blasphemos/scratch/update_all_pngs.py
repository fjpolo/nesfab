import os
import shutil
from PIL import Image
from collections import Counter

def get_tile_mask(img, tx, ty):
    pixels = []
    for y in range(8):
        for x in range(8):
            pixels.append(img.getpixel((tx + x, ty + y)))
            
    # Find the local background color: usually black/dark or the pixel at (tx, ty)
    bg_color = img.getpixel((tx, ty))
    
    mask = []
    for p in pixels:
        # If the pixel is similar to the background color or black
        if p[:3] == bg_color[:3] or sum(p[:3]) < 10:
            mask.append(0)
        else:
            mask.append(1)
    return tuple(mask)

def main():
    orig_font_path = "assets/font_orig.png"
    new_font_path = "assets/font.png"
    
    if not os.path.exists(orig_font_path) or not os.path.exists(new_font_path):
        print("Required font PNGs not found!")
        return
        
    font_orig_img = Image.open(orig_font_path).convert("RGBA")
    font_new_img = Image.open(new_font_path).convert("RGBA")
    
    # 1. Map old font masks to new font masks
    font_masks_orig = {}
    font_masks_new = {}
    for char_idx in range(96):
        tile_col = char_idx % 16
        tile_row = char_idx // 16
        tx, ty = tile_col * 8, tile_row * 8
        
        mask_orig = get_tile_mask(font_orig_img, tx, ty)
        mask_new = get_tile_mask(font_new_img, tx, ty)
        
        if sum(mask_orig) > 0:
            font_masks_orig[mask_orig] = char_idx
            font_masks_new[char_idx] = mask_new
            
    print(f"Generated shape masks for {len(font_masks_orig)} non-empty characters.")
    
    targets = ["assets/bg1.png", "assets/bg2.png", "assets/sprite.png", "assets/sprite2.png"]
    
    for target in targets:
        if not os.path.exists(target):
            print(f"Target {target} does not exist, skipping.")
            continue
            
        # Backup original
        backup_path = target.replace(".png", "_orig.png")
        if not os.path.exists(backup_path):
            print(f"Creating backup of {target} to {backup_path}...")
            shutil.copy(target, backup_path)
            
        img = Image.open(target).convert("RGBA")
        width, height = img.size
        pixels_modified = 0
        tiles_replaced = 0
        
        # We work on a copy of the image to modify it
        img_out = img.copy()
        
        for row in range(height // 8):
            for col in range(width // 8):
                tx, ty = col * 8, row * 8
                mask = get_tile_mask(img, tx, ty)
                
                if mask in font_masks_orig:
                    char_idx = font_masks_orig[mask]
                    char_repr = chr(char_idx + 32)
                    tiles_replaced += 1
                    
                    # Determine target tile's text and background colors
                    # Gather colors in active and background mask areas
                    active_colors = []
                    bg_colors = []
                    
                    for y in range(8):
                        for x in range(8):
                            pixel_color = img.getpixel((tx + x, ty + y))
                            if mask[y * 8 + x] == 1:
                                active_colors.append(pixel_color)
                            else:
                                bg_colors.append(pixel_color)
                                
                    # Pick most common colors to be robust against noise
                    active_color = Counter(active_colors).most_common(1)[0][0] if active_colors else (255, 255, 254, 255)
                    bg_color = Counter(bg_colors).most_common(1)[0][0] if bg_colors else (0, 0, 1, 255)
                    
                    # Get the new gothic mask for this character
                    new_mask = font_masks_new[char_idx]
                    
                    # Apply the new gothic mask using the extracted local colors
                    for y in range(8):
                        for x in range(8):
                            bit = new_mask[y * 8 + x]
                            if bit == 1:
                                img_out.putpixel((tx + x, ty + y), active_color)
                            else:
                                img_out.putpixel((tx + x, ty + y), bg_color)
                                
        # Save the updated image
        img_out.save(target)
        print(f"Successfully replaced {tiles_replaced} tiles in {target}")

if __name__ == "__main__":
    main()

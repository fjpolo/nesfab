import os
from PIL import Image

def main():
    font_path = "assets/font.png"
    sprite_path = "assets/sprite.png"
    
    if not os.path.exists(font_path) or not os.path.exists(sprite_path):
        print("Error: assets/font.png or assets/sprite.png not found!")
        return
        
    font_img = Image.open(font_path).convert("RGBA")
    sprite_img = Image.open(sprite_path).convert("RGBA")
    
    # Character mapping to copy:
    # Character -> (Font index, Target tile index in sprite.png)
    char_map = {
        'I': (73 - 32, 248),
        'N': (78 - 32, 249),
        'V': (86 - 32, 250),
        'C': (67 - 32, 251),
        'B': (66 - 32, 252),
        'L': (76 - 32, 253),
        'T': (84 - 32, 254),
        'Y': (89 - 32, 255),
        '!': (33 - 32, 242)
    }
    
    # Load and process each character
    for char, (font_idx, target_tile) in char_map.items():
        # Source coords
        src_col = font_idx % 16
        src_row = font_idx // 16
        src_x = src_col * 8
        src_y = src_row * 8
        
        # Target coords
        dst_col = target_tile % 16
        dst_row = target_tile // 16
        dst_x = dst_col * 8
        dst_y = dst_row * 8
        
        print(f"Injecting '{char}' (font idx {font_idx}) to sprite tile {target_tile} at ({dst_x}, {dst_y})")
        
        # Copy 8x8 pixels
        for y in range(8):
            for x in range(8):
                pixel = font_img.getpixel((src_x + x, src_y + y))
                # If pixel is visible, make it white (index 3 color).
                # If transparent, make it fully transparent (0, 0, 0, 0)
                if pixel[3] > 128:
                    # Pure white for sprite palette foreground rendering
                    sprite_img.putpixel((dst_x + x, dst_y + y), (255, 255, 255, 255))
                else:
                    sprite_img.putpixel((dst_x + x, dst_y + y), (0, 0, 0, 0))
                    
    # Save the updated sprite.png
    sprite_img.save(sprite_path)
    print("Successfully updated sprite.png with invincibility letters!")

if __name__ == "__main__":
    main()

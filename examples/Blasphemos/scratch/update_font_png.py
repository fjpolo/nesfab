import os
import shutil
from PIL import Image
import re

def parse_header_bytes(header_path):
    if not os.path.exists(header_path):
        raise FileNotFoundError(f"Header file {header_path} not found.")
        
    with open(header_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Find the position of the array definition
    start_pos = content.find("FONT_BYTELETTER_BITMAP")
    if start_pos == -1:
        raise ValueError("Could not find FONT_BYTELETTER_BITMAP array in header file.")
        
    # Get all hex values after this position
    hex_values = re.findall(r"0x[0-9a-fA-F]+", content[start_pos:])
    
    # We only expect 96 characters * 8 bytes = 768 bytes
    hex_values = hex_values[:768]
    
    byte_array = [int(val, 16) for val in hex_values]
    print(f"Parsed {len(byte_array)} bytes ({len(byte_array) // 8} characters).")
    return byte_array

def main():
    header_path = "scratch/Byteletter/Source/Byteletter.h"
    font_path = "assets/font.png"
    backup_path = "assets/font_orig.png"
    
    # 1. Backup the original font.png if not already done
    if not os.path.exists(backup_path):
        print(f"Creating backup of original font.png to {backup_path}...")
        shutil.copy(font_path, backup_path)
    else:
        print("Original font backup already exists.")
        
    # 2. Parse the gothic font bytes
    font_bytes = parse_header_bytes(header_path)
    if len(font_bytes) != 96 * 8:
        raise ValueError(f"Expected exactly 768 bytes (96 characters * 8 bytes), got {len(font_bytes)}.")
        
    # 3. Load the existing font.png
    img = Image.open(font_path).convert("RGBA")
    width, height = img.size
    print(f"Loaded font.png: {width}x{height}")
    
    # 4. Overwrite only the first 96 tiles
    for char_idx in range(96):
        tile_col = char_idx % 16
        tile_row = char_idx // 16
        
        char_bytes = font_bytes[char_idx * 8 : (char_idx + 1) * 8]
        
        # Determine tile top-left in the sheet
        tile_x = tile_col * 8
        tile_y = tile_row * 8
        
        for y in range(8):
            row_byte = char_bytes[y]
            for x in range(8):
                # Shift bit: 7 is left, 0 is right
                bit = (row_byte >> (7 - x)) & 1
                
                px = tile_x + x
                py = tile_y + y
                
                if bit == 1:
                    # Active pixel: off-white (255, 255, 254, 255)
                    img.putpixel((px, py), (255, 255, 254, 255))
                else:
                    # Background pixel: transparent dark blue (0, 0, 1, 255)
                    img.putpixel((px, py), (0, 0, 1, 255))
                    
    # 5. Save the updated image
    img.save(font_path)
    print(f"Successfully updated first 96 tiles in {font_path}")

if __name__ == "__main__":
    main()

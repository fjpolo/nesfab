import os
from PIL import Image

def main():
    img_path = "assets/font.png"
    if not os.path.exists(img_path):
        print("font.png not found")
        return
    img = Image.open(img_path).convert("RGBA")
    
    with open("scratch/font_ascii_mapped.txt", "w", encoding="utf-8") as f:
        # Loop through all 256 tiles
        for row in range(16):
            for col in range(16):
                tile_idx = row * 16 + col
                tile_x = col * 8
                tile_y = row * 8
                
                # Check if tile has any non-background colors
                has_content = False
                tile_lines = []
                for y in range(8):
                    line = ""
                    for x in range(8):
                        r, g, b, a = img.getpixel((tile_x + x, tile_y + y))
                        if (r, g, b) == (0, 0, 0):
                            line += "."
                        elif (r, g, b) == (0, 0, 1):
                            line += " "
                        elif (r, g, b) == (255, 255, 254):
                            line += "#"
                            has_content = True
                        elif (r, g, b) == (127, 127, 127):
                            line += "x"
                            has_content = True
                        elif (r, g, b) == (255, 255, 255):
                            line += "*"
                            has_content = True
                        else:
                            line += "?"
                            has_content = True
                    tile_lines.append(line)
                
                if has_content:
                    f.write(f"Tile {tile_idx} (row {row}, col {col}):\n")
                    for line in tile_lines:
                        f.write(line + "\n")
                    f.write("\n")

if __name__ == "__main__":
    main()

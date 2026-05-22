import os
from PIL import Image

def main():
    img_path = "assets/font.png"
    if not os.path.exists(img_path):
        print("font.png not found")
        return
    img = Image.open(img_path).convert("RGBA")
    
    first_96_colors = set()
    for row in range(6):
        for col in range(16):
            tile_x = col * 8
            tile_y = row * 8
            for y in range(8):
                for x in range(8):
                    pixel = img.getpixel((tile_x + x, tile_y + y))
                    first_96_colors.add(pixel)
                    
    print("Unique colors in the first 96 tiles:")
    for color in sorted(first_96_colors):
        print(color)

if __name__ == "__main__":
    main()

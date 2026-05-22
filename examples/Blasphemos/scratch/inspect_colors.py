import os
from PIL import Image

def main():
    img = Image.open("assets/font.png").convert("RGBA")
    colors = img.getcolors(maxcolors=65536)
    print("Unique colors in image:")
    for color in sorted(colors, key=lambda x: x[0], reverse=True):
        print(f"Count: {color[0]}, Color: {color[1]}")

if __name__ == "__main__":
    main()

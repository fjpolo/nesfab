from PIL import Image

def main():
    img = Image.open("assets/sprite.png")
    print("Format:", img.format)
    print("Mode:", img.mode)
    if img.mode == "P":
        print("Palette size:", len(img.getpalette()))
        print("Palette colors:", img.getpalette()[:24])
    else:
        # Find unique colors
        colors = set()
        for y in range(img.height):
            for x in range(img.width):
                colors.add(img.getpixel((x, y)))
        print("Unique colors:", list(colors)[:20])

if __name__ == "__main__":
    main()

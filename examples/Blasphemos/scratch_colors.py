import sys
from PIL import Image

def main():
    img = Image.open(r"C:\Workspace\nesfab\nesfab\examples\Blasphemos\assets\silent_sorrow_8.png").convert("RGB")
    print(f"Size: {img.size}")
    colors = img.getcolors(maxcolors=256)
    if colors:
        for c in colors:
            print(c)
    else:
        print("Too many colors")

if __name__ == "__main__":
    main()

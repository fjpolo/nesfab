import os
from PIL import Image

def main():
    img_path = "assets/font.png"
    if not os.path.exists(img_path):
        print("font.png not found")
        return
    img = Image.open(img_path)
    print(f"Font image dimensions: {img.size}")
    print(f"Format: {img.format}")
    print(f"Mode: {img.mode}")

if __name__ == "__main__":
    main()

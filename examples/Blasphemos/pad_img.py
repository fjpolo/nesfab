import sys
from PIL import Image

def pad_image():
    try:
        img = Image.open(r"C:\Workspace\nesfab\nesfab\examples\Blasphemos\assets\silent_sorrow_9.png").convert("RGB")
        # Create a 256x240 black image
        padded = Image.new("RGB", (256, 240), (0, 0, 0))
        
        # Center horizontally: (256 - 169) / 2 = 43 pixels. Let's round to nearest tile: 40 pixels (5 tiles)
        padded.paste(img, (40, 0))
        
        padded.save(r"C:\Workspace\nesfab\nesfab\examples\Blasphemos\assets\silent_sorrow_9_padded.png")
        print("Padded image saved.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    pad_image()

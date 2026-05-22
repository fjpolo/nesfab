import os
from PIL import Image

def main():
    path = "assets/sprite.png"
    if not os.path.exists(path):
        print("sprite.png not found")
        return
        
    img = Image.open(path).convert("RGBA")
    w, h = img.size
    cols = w // 8
    rows = h // 8
    
    empty_indices = []
    for r in range(rows):
        for c in range(cols):
            tile_idx = r * cols + c
            # Check if all pixels in this 8x8 tile are transparent (alpha == 0) or black
            is_empty = True
            for y in range(8):
                for x in range(8):
                    pixel = img.getpixel((c * 8 + x, r * 8 + y))
                    # If it has alpha and is not pure transparent/black
                    if len(pixel) == 4:
                        if pixel[3] > 0 and (pixel[0] > 0 or pixel[1] > 0 or pixel[2] > 0):
                            is_empty = False
                            break
                    else:
                        if pixel[0] > 0 or pixel[1] > 0 or pixel[2] > 0:
                            is_empty = False
                            break
                if not is_empty:
                    break
            if is_empty:
                empty_indices.append(tile_idx)
                
    print(f"Total empty tiles in sprite.png: {len(empty_indices)}")
    print(f"Empty tile indices: {empty_indices[:50]} ...")

if __name__ == "__main__":
    main()

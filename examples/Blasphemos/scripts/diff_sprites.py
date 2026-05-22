import os
import numpy as np
from PIL import Image

def analyze():
    sprite1_path = "assets/sprite.png"
    sprite2_path = "assets/sprite2.png"
    
    img1 = Image.open(sprite1_path).convert("RGB")
    img2 = Image.open(sprite2_path).convert("RGB")
    
    arr1 = np.array(img1)
    arr2 = np.array(img2)
    
    h, w, _ = arr1.shape
    diff_tiles = []
    
    for y in range(0, h, 8):
        for x in range(0, w, 8):
            tile1 = arr1[y:y+8, x:x+8]
            tile2 = arr2[y:y+8, x:x+8]
            if not np.array_equal(tile1, tile2):
                tile_idx = (y // 8) * 16 + (x // 8)
                diff_tiles.append(tile_idx)
                
    print(f"Number of different 8x8 tiles between sprite.png and sprite2.png: {len(diff_tiles)}")
    print("Different tile indices (Hex):")
    for idx in diff_tiles:
        print(f"  0x{idx:02X}")

if __name__ == "__main__":
    analyze()

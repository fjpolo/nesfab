import os
import numpy as np
from PIL import Image

def get_tiles_shape(img, name=""):
    img = img.convert("L") # Grayscale
    arr = np.array(img)
    unique_vals = np.unique(arr)
    print(f"Unique grayscale values in {name}: {unique_vals}")
    
    h, w = arr.shape
    tiles = []
    for y in range(0, h, 8):
        if y + 8 > h: break
        row = []
        for x in range(0, w, 8):
            if x + 8 > w: break
            tile = arr[y:y+8, x:x+8]
            t_uniq = np.unique(tile)
            norm_tile = np.zeros((8, 8), dtype=int)
            for i, val in enumerate(t_uniq):
                norm_tile[tile == val] = i
            row.append(norm_tile)
        tiles.append(row)
    return tiles

def analyze():
    sprite1_path = "assets/sprite.png"
    sprite2_path = "assets/sprite2.png"
    crucified_path = "assets/Crucified.png"
    
    img_sprite2 = Image.open(sprite2_path)
    img_sprite1 = Image.open(sprite1_path)
    img_crucified = Image.open(crucified_path)
    
    tiles_sprite2 = get_tiles_shape(img_sprite2, "sprite2.png")
    tiles_sprite1 = get_tiles_shape(img_sprite1, "sprite.png")
    tiles_crucified = get_tiles_shape(img_crucified, "Crucified.png")
    
    matches_sprite2 = []
    for cy in range(len(tiles_crucified)):
        for cx in range(len(tiles_crucified[cy])):
            ctile = tiles_crucified[cy][cx]
            if np.all(ctile == ctile[0,0]):
                continue
                
            found = False
            for sy in range(len(tiles_sprite2)):
                for sx in range(len(tiles_sprite2[sy])):
                    stile = tiles_sprite2[sy][sx]
                    if np.array_equal(ctile, stile):
                        found = True
                        tile_idx = sy * 16 + sx
                        matches_sprite2.append((cx, cy, tile_idx))
                        break
                if found: break
                
    print(f"Total non-empty Crucified tiles with matching shape in Sprite 2: {len(matches_sprite2)}")
    if matches_sprite2:
        print("First 20 matches (Crucified X, Y -> Sprite 2 Index):")
        for m in matches_sprite2[:20]:
            print(f"  ({m[0]}, {m[1]}) -> 0x{m[2]:02X}")

if __name__ == "__main__":
    analyze()

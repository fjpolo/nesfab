import sys
import itertools
from PIL import Image

def img_to_tiles(img, color_mapping):
    tiles = []
    for r in range(12):
        for c in range(20):
            tile_data = []
            for y in range(8):
                row = []
                for x in range(8):
                    pixel = img.getpixel((c*8+x, r*8+y))
                    color = color_mapping[pixel]
                    row.append(color)
                tile_data.append(row)
            
            nes_chr = bytearray(16)
            for y in range(8):
                plane0 = 0
                plane1 = 0
                for x in range(8):
                    color = tile_data[y][x]
                    plane0 |= (color & 1) << (7 - x)
                    plane1 |= ((color >> 1) & 1) << (7 - x)
                nes_chr[y] = plane0
                nes_chr[y + 8] = plane1
            tiles.append(bytes(nes_chr))
    return tiles

def read_chr(chr_path):
    with open(chr_path, 'rb') as f:
        data = f.read()
    tiles = []
    for i in range(len(data)//16):
        tiles.append(data[i*16:(i+1)*16])
    return tiles

def main():
    img = Image.open(r"C:\Workspace\nesfab\nesfab\examples\Blasphemos\assets\silent_sorrow_8.png").convert("RGB")
    colors = [c[1] for c in img.getcolors(maxcolors=256)]
    chr_tiles = read_chr(r"C:\Workspace\nesfab\nesfab\examples\Blasphemos\assets\silent_sorrow_8.chr")
    chr_set = set(chr_tiles)

    best_missing = 9999
    best_mapping = None
    best_nametable = None

    fixed = {}
    for c in colors:
        if c == (0,0,0): fixed[c] = [0]
        else: fixed[c] = [0, 1, 2, 3]

    keys = list(fixed.keys())
    values = [fixed[k] for k in keys]
    
    for combo in itertools.product(*values):
        mapping = dict(zip(keys, combo))
        
        # Constrain: mapping must use at least 3 distinct values
        distinct_vals = set(mapping.values())
        if len(distinct_vals) < 3:
            continue
            
        png_tiles = img_to_tiles(img, mapping)
        
        missing = sum(1 for pt in png_tiles if pt not in chr_set)
        if missing < best_missing:
            best_missing = missing
            best_mapping = mapping
            best_nametable = []
            for pt in png_tiles:
                if pt in chr_tiles:
                    best_nametable.append(chr_tiles.index(pt))
                else:
                    best_nametable.append(0)
            if best_missing == 0:
                break
                
    print(f"Best missing: {best_missing}")
    print(f"Best mapping: {best_mapping}")
    print(f"ct U[240] SORROW_NAM_8 = U[240]({', '.join(map(str, best_nametable))})")

if __name__ == "__main__":
    main()

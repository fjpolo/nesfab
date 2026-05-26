import sys
import itertools
from PIL import Image

def get_tile(img, c, r, mapping):
    nes_chr = bytearray(16)
    for y in range(8):
        plane0 = 0
        plane1 = 0
        for x in range(8):
            px_x = c*8+x
            px_y = r*8+y
            if px_x < img.width and px_y < img.height:
                pixel = img.getpixel((px_x, px_y))
                color = mapping[pixel]
            else:
                color = 0 # Padding color
            plane0 |= (color & 1) << (7 - x)
            plane1 |= ((color >> 1) & 1) << (7 - x)
        nes_chr[y] = plane0
        nes_chr[y + 8] = plane1
    return bytes(nes_chr)

def read_chr(chr_path):
    with open(chr_path, 'rb') as f:
        data = f.read(4096)
    tiles = []
    for i in range(len(data)//16):
        tiles.append(data[i*16:(i+1)*16])
    return tiles

def main():
    img = Image.open(r"C:\Workspace\nesfab\nesfab\examples\Blasphemos\assets\silent_sorrow_9.png").convert("RGB")
    colors = [c[1] for c in img.getcolors(maxcolors=256)]
    chr_tiles = read_chr(r"C:\Workspace\nesfab\nesfab\examples\Blasphemos\assets\silent_sorrow_9.chr")
    chr_set = set(chr_tiles)

    fixed = {}
    for c in colors:
        if c == (0,0,0): fixed[c] = [0]
        else: fixed[c] = [0, 1, 2, 3]

    keys = list(fixed.keys())
    values = [fixed[k] for k in keys]
    
    best_mapping = None

    # Find 5 non-empty tiles from the image to test mappings quickly
    test_coords = []
    for r in range(30):
        for c in range(22):
            empty = True
            for y in range(8):
                for x in range(8):
                    px_x = c*8+x
                    px_y = r*8+y
                    if px_x < img.width and px_y < img.height:
                        if img.getpixel((px_x, px_y)) != (0,0,0):
                            empty = False
            if not empty:
                test_coords.append((c, r))
                if len(test_coords) >= 5:
                    break
        if len(test_coords) >= 5:
            break

    for combo in itertools.product(*values):
        mapping = dict(zip(keys, combo))
        
        if len(set(mapping.values())) < 3:
            continue
            
        failed = False
        for c, r in test_coords:
            if get_tile(img, c, r, mapping) not in chr_set:
                failed = True
                break
                
        if not failed:
            # Full check
            for r in range(30):
                for c in range(22):
                    if get_tile(img, c, r, mapping) not in chr_set:
                        failed = True
                        break
                if failed: break
                
        if not failed:
            print(f"FOUND PERFECT MAPPING: {mapping}")
            best_mapping = mapping
            break

    if best_mapping:
        best_nametable = []
        for r in range(30):
            for c in range(22):
                tile = get_tile(img, c, r, best_mapping)
                best_nametable.append(chr_tiles.index(tile))
                
        full_nametable = []
        for r in range(30):
            row = [0]*5 + best_nametable[r*22 : (r+1)*22] + [0]*5
            full_nametable.extend(row)
        
        chunks = [full_nametable[i:i+240] for i in range(0, 960, 240)]
        with open('extracted_nam_9.txt', 'w') as f:
            for i, chunk in enumerate(chunks):
                f.write(f"ct U[240] SORROW_NAM_9_PART_{i} = U[240]({', '.join(map(str, chunk))})\n")
        print("Successfully wrote extracted_nam_9.txt")
    else:
        print("NO PERFECT MAPPING FOUND.")

if __name__ == "__main__":
    main()

import sys
import itertools
from PIL import Image

def img_to_tiles(img, color_mapping):
    tiles = []
    # Image padded to 22x30 tiles
    for r in range(30):
        for c in range(22):
            tile_data = []
            for y in range(8):
                row = []
                for x in range(8):
                    px_x = c*8+x
                    px_y = r*8+y
                    if px_x < img.width and px_y < img.height:
                        pixel = img.getpixel((px_x, px_y))
                        color = color_mapping[pixel]
                    else:
                        color = 0 # pad with 0 (black)
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
    
    best_nametable = None

    for combo in itertools.product(*values):
        mapping = dict(zip(keys, combo))
        
        if len(set(mapping.values())) < 3:
            continue
            
        failed = False
        for r in range(30):
            for c in range(22):
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
                            color = 0
                        plane0 |= (color & 1) << (7 - x)
                        plane1 |= ((color >> 1) & 1) << (7 - x)
                    nes_chr[y] = plane0
                    nes_chr[y + 8] = plane1
                
                if bytes(nes_chr) not in chr_set:
                    failed = True
                    break
            if failed:
                break
                
        if not failed:
            print(f"FOUND PERFECT MAPPING: {mapping}")
            png_tiles = img_to_tiles(img, mapping)
            best_nametable = [chr_tiles.index(pt) for pt in png_tiles]
            break

    if best_nametable:
        # We need to construct a 32x30 nametable array from the 22x30 map
        # It should be horizontally centered: (32 - 22) / 2 = 5 columns of empty tiles on each side
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

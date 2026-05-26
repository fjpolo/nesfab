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
                color = mapping.get(pixel, 0)
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

def hamming_distance(tile1, tile2):
    return sum(bin(b1 ^ b2).count('1') for b1, b2 in zip(tile1, tile2))

def main():
    img = Image.open(r"C:\Workspace\nesfab\nesfab\examples\Blasphemos\assets\silent_sorrow_9.png").convert("RGB")
    colors = [c[1] for c in img.getcolors(maxcolors=256)]
    chr_tiles = read_chr(r"C:\Workspace\nesfab\nesfab\examples\Blasphemos\assets\silent_sorrow_9.chr")

    # Map colors automatically by luminance to 4 indices
    def luminance(c):
        return 0.299*c[0] + 0.587*c[1] + 0.114*c[2]
        
    colors.sort(key=luminance)
    mapping = {}
    for i, c in enumerate(colors):
        if i == 0: mapping[c] = 3 # Black -> 3
        elif i == 1: mapping[c] = 0 # Dark Blue -> 0
        elif i >= len(colors)-2: mapping[c] = 2 # White/Beige -> 2
        else: mapping[c] = 1 # Grey -> 1

    best_nametable = []
    for r in range(30):
        for c in range(22):
            tile = get_tile(img, c, r, mapping)
            # Find closest tile in CHR
            best_dist = 9999
            best_idx = 0
            for i, chr_tile in enumerate(chr_tiles):
                dist = hamming_distance(tile, chr_tile)
                if dist < best_dist:
                    best_dist = dist
                    best_idx = i
            best_nametable.append(best_idx)

    full_nametable = []
    for r in range(30):
        row = [0]*5 + best_nametable[r*22 : (r+1)*22] + [0]*5
        full_nametable.extend(row)
    
    chunks = [full_nametable[i:i+240] for i in range(0, 960, 240)]
    with open('extracted_nam_9.txt', 'w') as f:
        for i, chunk in enumerate(chunks):
            f.write(f"ct U[240] SORROW_NAM_9_PART_{i} = U[240]({', '.join(map(str, chunk))})\n")
    print("Successfully generated nametable with fuzzy matching!")

if __name__ == "__main__":
    main()

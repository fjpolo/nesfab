import sys
from PIL import Image

def process(img_path, chr_path, array_name):
    img = Image.open(img_path)
    if img.mode != 'P':
        img = img.convert('P', palette=Image.ADAPTIVE, colors=4)
    w, h = img.size
    pw = (w + 7) // 8 * 8
    ph = (h + 7) // 8 * 8
    
    padded = Image.new('P', (pw, ph), 0)
    padded.putpalette(img.getpalette())
    padded.paste(img, (0, 0))
    
    pixels = padded.load()
    tiles = []
    nametable = []
    
    for y in range(0, ph, 8):
        for x in range(0, pw, 8):
            tile_data = bytearray(16)
            for ty in range(8):
                plane0 = 0
                plane1 = 0
                for tx in range(8):
                    px = min(pixels[x+tx, y+ty] or 0, 3)
                    plane0 |= (px & 1) << (7 - tx)
                    plane1 |= ((px >> 1) & 1) << (7 - tx)
                tile_data[ty] = plane0
                tile_data[ty+8] = plane1
            
            tile_bytes = bytes(tile_data)
            if tile_bytes not in tiles:
                if len(tiles) >= 256:
                    print(f'ERROR: Too many unique tiles in {img_path}!')
                    sys.exit(1)
                tiles.append(tile_bytes)
            
            nametable.append(tiles.index(tile_bytes))
            
    with open(chr_path, 'wb') as f:
        for t in tiles:
            f.write(t)
        f.write(b'\x00' * (4096 - len(tiles)*16))
        
    cols = pw // 8
    rows = ph // 8
    
    full_nt = [0] * 960
    start_r = (30 - rows) // 2
    start_c = (32 - cols) // 2
    for r in range(rows):
        for c in range(cols):
            full_nt[(start_r + r) * 32 + (start_c + c)] = nametable[r * cols + c]
            
    print(f'ct U[960] {array_name} = U[960](' + ', '.join(map(str, full_nt)) + ')')

process('../assets/silent_sorrow_2.png', '../assets/silent_sorrow_2.chr', 'SORROW_NAM_1_FULL')
process('../assets/silent_sorrow_4.png', '../assets/silent_sorrow_4.chr', 'SORROW_NAM_3_FULL')

import sys
from PIL import Image

def get_data(img_path, chr_path, prefix):
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
            
    res = []
    for i in range(4):
        part = full_nt[i*240:(i+1)*240]
        res.append(f'ct U[240] {prefix}_{i} = U[240](' + ', '.join(map(str, part)) + ')')
    return '\n'.join(res)

arr2 = get_data('../assets/silent_sorrow_2.png', '../assets/silent_sorrow_2.chr', 'SORROW_NAM_2_PART')
arr4 = get_data('../assets/silent_sorrow_4.png', '../assets/silent_sorrow_4.chr', 'SORROW_NAM_4_PART')

with open('intro_silent_sorrow.fab', 'r', encoding='utf-8') as f:
    content = f.read()

# remove old SORROW_NAM_2_FULL and SORROW_NAM_4_FULL arrays if they exist
lines = content.split('\n')
new_lines = []
for line in lines:
    if line.startswith('ct U[960] SORROW_NAM_2_FULL'): continue
    if line.startswith('ct U[960] SORROW_NAM_4_FULL'): continue
    if line.startswith('ct U[240] SORROW_NAM_2_PART'): continue
    if line.startswith('ct U[240] SORROW_NAM_4_PART'): continue
    new_lines.append(line)
content = '\n'.join(new_lines)

idx = content.find('fn sorrow_setup_nametable')
new_content = content[:idx] + arr2 + '\n' + arr4 + '\n\n' + content[idx:]

old_loop = '''    if current_frame == 2
        {PPUSTATUS}()
        {PPUADDR}($20)
        {PPUADDR}($00)
        for UU i = 0; i < 960; i += 1
            {PPUDATA}(SORROW_NAM_2_FULL[i])
    else if current_frame == 4
        {PPUSTATUS}()
        {PPUADDR}($20)
        {PPUADDR}($00)
        for UU i = 0; i < 960; i += 1
            {PPUDATA}(SORROW_NAM_4_FULL[i])'''

new_loop = '''    if current_frame == 2
        {PPUSTATUS}()
        {PPUADDR}($20)
        {PPUADDR}($00)
        for U i = 0; i < 240; i += 1
            {PPUDATA}(SORROW_NAM_2_PART_0[i])
        for U i = 0; i < 240; i += 1
            {PPUDATA}(SORROW_NAM_2_PART_1[i])
        for U i = 0; i < 240; i += 1
            {PPUDATA}(SORROW_NAM_2_PART_2[i])
        for U i = 0; i < 240; i += 1
            {PPUDATA}(SORROW_NAM_2_PART_3[i])
    else if current_frame == 4
        {PPUSTATUS}()
        {PPUADDR}($20)
        {PPUADDR}($00)
        for U i = 0; i < 240; i += 1
            {PPUDATA}(SORROW_NAM_4_PART_0[i])
        for U i = 0; i < 240; i += 1
            {PPUDATA}(SORROW_NAM_4_PART_1[i])
        for U i = 0; i < 240; i += 1
            {PPUDATA}(SORROW_NAM_4_PART_2[i])
        for U i = 0; i < 240; i += 1
            {PPUDATA}(SORROW_NAM_4_PART_3[i])'''

new_content = new_content.replace(old_loop, new_loop)

with open('intro_silent_sorrow.fab', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Done!")

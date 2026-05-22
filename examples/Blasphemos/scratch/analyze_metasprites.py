import os
import re

def parse_metasprites(file_path):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return []
        
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
        
    # Find all sprite blocks
    # Format matches: [] sprite_name followed by make_metasprite and list of Ms(...)
    sprite_blocks = []
    
    # State machine parser to handle multi-line Ms definitions robustly
    lines = content.splitlines()
    current_name = None
    current_sprites = []
    in_block = False
    
    ms_regex = re.compile(r'Ms\(\s*(-?\d+)\s*,\s*(-?\d+)\s*,\s*(0x[0-9A-Fa-f]+|\$[0-9A-Fa-f]+|\d+)\s*,\s*(0x[0-9A-Fa-f]+|\$[0-9A-Fa-f]+|\d+)\s*\)')
    
    for line in lines:
        line = line.strip()
        if line.startswith("[] sprite_"):
            if current_name and current_sprites:
                sprite_blocks.append((current_name, current_sprites))
            current_name = line.split("[]")[1].strip()
            current_sprites = []
            in_block = True
            continue
            
        if in_block:
            # Look for all Ms(...) matches on this line
            matches = ms_regex.findall(line)
            for m in matches:
                x = int(m[0])
                y = int(m[1])
                tile = m[2]
                attr = m[3]
                current_sprites.append((x, y, tile, attr))
                
            # If we see the closing parentheses of the metasprite array
            if ")))" in line or (line.startswith("[]") and not line.startswith("[] sprite_")):
                in_block = False
                if current_name and current_sprites:
                    sprite_blocks.append((current_name, current_sprites))
                    current_name = None
                    current_sprites = []
                    
    if current_name and current_sprites:
        sprite_blocks.append((current_name, current_sprites))
        
    return sprite_blocks

def analyze_scanline_density(sprites):
    if not sprites:
        return 0, 0, 0, 0, 0
        
    # Each sprite (x, y) is 8x8 pixels.
    # Scanline range is y to y + 7.
    # We find the min and max y coordinates to scan.
    min_y = min(s[1] for s in sprites)
    max_y = max(s[1] for s in sprites) + 8
    
    max_density = 0
    densest_y = 0
    
    # Check scanline density for every scanline
    for y in range(min_y, max_y):
        density = 0
        for sx, sy, _, _ in sprites:
            if sy <= y < sy + 8:
                density += 1
        if density > max_density:
            max_density = density
            densest_y = y
            
    # Calculate bounding box
    min_x = min(s[0] for s in sprites)
    max_x = max(s[0] for s in sprites) + 8
    width = max_x - min_x
    height = max_y - min_y
    
    return len(sprites), max_density, densest_y, width, height

def main():
    player_fab = "player.fab"
    print(f"Parsing player metasprites in {player_fab}...")
    metasprites = parse_metasprites(player_fab)
    
    if not metasprites:
        print("No metasprites parsed.")
        return
        
    print(f"Successfully parsed {len(metasprites)} metasprite frames.")
    print("-" * 105)
    print(f"{'Metasprite Frame Name':<45} | {'Total 8x8s':<10} | {'Max Scanline Overlap':<20} | {'Dimensions (WxH)':<16} | {'Status'}")
    print("-" * 105)
    
    high_density_count = 0
    for name, sprites in metasprites:
        total_sprites, max_density, densest_y, w, h = analyze_scanline_density(sprites)
        
        status = "OK [OPTIMIZED]"
        if max_density > 8:
            status = "HARD FLICKER (>8)"
            high_density_count += 1
        elif max_density > 4:
            status = "FLICKER RISK (>4)"
            high_density_count += 1
            
        dim_str = f"{w}x{h} px"
        print(f"{name:<45} | {total_sprites:<10} | {max_density:<20} | {dim_str:<16} | {status}")
        
    print("-" * 105)
    print(f"Analysis complete. Total flicker-prone frames: {high_density_count}/{len(metasprites)}")

if __name__ == "__main__":
    main()

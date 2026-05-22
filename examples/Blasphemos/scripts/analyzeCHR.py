import os
import sys
from PIL import Image, ImageDraw, ImageFont

def analyze_chr():
    rom_path = "BlasNESmous.nes"
    if not os.path.exists(rom_path):
        print(f"Error: ROM file '{rom_path}' not found in the current directory.")
        sys.exit(1)
        
    print("Reading BlasNESmous.nes...")
    with open(rom_path, "rb") as f:
        # Skip 16 bytes iNES header + 524288 bytes PRG-ROM
        f.seek(16 + 524288)
        chr_data = f.read(262144)
        
    if len(chr_data) < 262144:
        print(f"Warning: CHR-ROM read size ({len(chr_data)} bytes) is less than expected 262144 bytes.")
        # Pad with zeros if necessary
        chr_data = chr_data + b'\x00' * (262144 - len(chr_data))
        
    print("Analyzing CHR-ROM tiles...")
    # There are 16,384 tiles of 16 bytes each
    num_tiles = 16384
    tile_used = [False] * num_tiles
    
    for i in range(num_tiles):
        tile_bytes = chr_data[i*16 : (i+1)*16]
        # Check if the tile has any non-zero bytes (indicating it is used)
        if any(b != 0 for b in tile_bytes):
            tile_used[i] = True
            
    total_used_tiles = sum(1 for t in tile_used if t)
    total_defined_bytes = total_used_tiles * 16
    print(f"Total used tiles: {total_used_tiles} / {num_tiles} ({total_used_tiles / num_tiles:.1%})")
    print(f"Active graphic data size: {total_defined_bytes} bytes")
    
    # ----------------------------------------------------
    # IMAGE 1: chr_usage.png (CHR-ROM Space Utilization Map)
    # ----------------------------------------------------
    print("Generating chr_usage.png...")
    
    # Dimensions for layout: 8 columns x 4 rows of banks
    # Each bank has 16 columns of tiles x 32 rows of tiles
    # We scale each tile to a 2x2 pixel square in the heatmap
    tile_scale = 2
    bank_w = 16 * tile_scale
    bank_h = 32 * tile_scale
    
    padding_x = 16
    padding_y = 32
    header_h = 70
    footer_h = 40
    
    img_w = 8 * (bank_w + padding_x) + padding_x
    img_h = header_h + 4 * (bank_h + padding_y) + footer_h
    
    usage_img = Image.new("RGB", (img_w, img_h), "#121214")
    draw = ImageDraw.Draw(usage_img)
    
    # Title Text
    try:
        font_title = ImageFont.truetype("arial.ttf", 20)
        font_sub = ImageFont.truetype("arial.ttf", 12)
        font_label = ImageFont.truetype("arial.ttf", 9)
    except IOError:
        font_title = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        font_label = ImageFont.load_default()
        
    draw.text((padding_x, 15), "Blasphemos CHR-ROM Space Utilization Map", fill="#FFFFFF", font=font_title)
    draw.text((padding_x, 40), f"Active Graphics: {total_defined_bytes} bytes / {len(chr_data)} bytes expected (MMC3 256KB)", fill="#88888E", font=font_sub)
    
    # Draw banks
    for bank_idx in range(32):
        col_bank = bank_idx % 8
        row_bank = bank_idx // 8
        
        bx = padding_x + col_bank * (bank_w + padding_x)
        by = header_h + row_bank * (bank_h + padding_y)
        
        # Draw bank label
        draw.text((bx, by - 12), f"Bank {bank_idx}", fill="#A3A3AC", font=font_label)
        
        # Draw bank background
        draw.rectangle([bx - 1, by - 1, bx + bank_w, by + bank_h], outline="#2D2D34", fill="#1E1E24")
        
        # Draw tiles inside this bank
        bank_start_tile = bank_idx * 512
        for t_idx in range(512):
            global_tile_idx = bank_start_tile + t_idx
            t_col = t_idx % 16
            t_row = t_idx // 16
            
            tx = bx + t_col * tile_scale
            ty = by + t_row * tile_scale
            
            if tile_used[global_tile_idx]:
                # Turquoise color for used tiles
                draw.rectangle([tx, ty, tx + tile_scale - 1, ty + tile_scale - 1], fill="#00ADB5")
            else:
                # Dark gray for empty tiles
                draw.rectangle([tx, ty, tx + tile_scale - 1, ty + tile_scale - 1], fill="#1E1E24")
                
    # Footer
    draw.text((padding_x, img_h - 25), "Legend:   [ Turquoise ] Used Graphic Tile      [ Dark Gray ] Empty / Available Space", fill="#A3A3AC", font=font_sub)
    
    usage_img.save("analysis/chr_usage.png")
    print("Success! Heatmap saved to: analysis/chr_usage.png")
    
    # ----------------------------------------------------
    # IMAGE 2: chr_sheet.png (Rendered 2bpp CHR Tile Sheet)
    # ----------------------------------------------------
    print("Generating chr_sheet.png...")
    
    # Grid of 8x4 banks. Each bank is 16x32 tiles. Each tile is 8x8 pixels.
    # Total width: 8 * 16 * 8 = 1024 pixels.
    # Total height: 4 * 32 * 8 = 1024 pixels.
    sheet_w = 1024
    sheet_h = 1024
    
    sheet_img = Image.new("RGB", (sheet_w, sheet_h), "#000000")
    pixels = sheet_img.load()
    
    # Palette for rendering tiles (grayscaled retro look)
    palette_colors = [
        (16, 16, 20),      # Color 0 (Transparent/Background)
        (80, 80, 90),      # Color 1 (Dark Shadow)
        (160, 160, 175),   # Color 2 (Midtone)
        (240, 240, 255)    # Color 3 (Highlight)
    ]
    
    for bank_idx in range(32):
        col_bank = bank_idx % 8
        row_bank = bank_idx // 8
        
        bank_px = col_bank * 128
        bank_py = row_bank * 256
        
        bank_start_tile = bank_idx * 512
        
        for t_idx in range(512):
            global_tile_idx = bank_start_tile + t_idx
            t_col = t_idx % 16
            t_row = t_idx // 16
            
            tile_px = bank_px + t_col * 8
            tile_py = bank_py + t_row * 8
            
            # Decode the 16 bytes for this 8x8 tile
            tile_bytes = chr_data[global_tile_idx*16 : (global_tile_idx+1)*16]
            
            for y in range(8):
                p0 = tile_bytes[y]
                p1 = tile_bytes[y + 8]
                for x in range(8):
                    bit0 = (p0 >> (7 - x)) & 1
                    bit1 = (p1 >> (7 - x)) & 1
                    color_idx = (bit1 << 1) | bit0
                    
                    px = tile_px + x
                    py = tile_py + y
                    pixels[px, py] = palette_colors[color_idx]
                    
    # Draw high-fidelity grid borders between banks
    draw_sheet = ImageDraw.Draw(sheet_img)
    # Draw horizontal bank separators
    for r in range(1, 4):
        draw_sheet.line([(0, r * 256), (sheet_w - 1, r * 256)], fill="#8B0000", width=1)
    # Draw vertical bank separators
    for c in range(1, 8):
        draw_sheet.line([(c * 128, 0), (c * 128, sheet_h - 1)], fill="#8B0000", width=1)
        
    sheet_img.save("analysis/chr_sheet.png")
    print("Success! Rendered tile sheet saved to: analysis/chr_sheet.png")
    
if __name__ == "__main__":
    analyze_chr()

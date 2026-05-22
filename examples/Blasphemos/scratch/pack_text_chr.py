import os
from PIL import Image

def tile_to_chr(tile_pixels):
    plane0 = bytearray(8)
    plane1 = bytearray(8)
    for y in range(8):
        b0 = 0
        b1 = 0
        for x in range(8):
            pixel = tile_pixels[y * 8 + x]
            bit0 = pixel & 1
            bit1 = (pixel >> 1) & 1
            b0 = (b0 << 1) | bit0
            b1 = (b1 << 1) | bit1
        plane0[y] = b0
        plane1[y] = b1
    return bytes(plane0 + plane1)

def main():
    image_indices = [0, 1, 3, 5]
    images = {}
    
    for idx in image_indices:
        path = f"assets/silent_sorrow_{idx}.png"
        if not os.path.exists(path):
            print(f"Error: {path} not found!")
            return
        images[idx] = Image.open(path)
        
    unique_tiles = []
    unique_tiles_set = {}
    
    # We want tile 0 to be a completely solid black tile.
    # Let's pre-populate index 0 with a solid black 8x8 tile.
    black_tile = bytes([0] * 16)
    unique_tiles.append(black_tile)
    unique_tiles_set[black_tile] = 0
    
    nametables = {}
    
    for idx in image_indices:
        img = images[idx]
        w, h = img.size
        cols = w // 8
        rows = h // 8
        
        nametable = []
        
        for r in range(rows):
            for c in range(cols):
                # Extract 8x8 pixel block
                tile_pixels = []
                for y in range(8):
                    for x in range(8):
                        tile_pixels.append(img.getpixel((c * 8 + x, r * 8 + y)))
                        
                # Convert to 16-byte NES CHR representation
                tile_bytes = tile_to_chr(tile_pixels)
                
                # Check for uniqueness
                if tile_bytes not in unique_tiles_set:
                    unique_tiles_set[tile_bytes] = len(unique_tiles)
                    unique_tiles.append(tile_bytes)
                    
                nametable.append(unique_tiles_set[tile_bytes])
                
        nametables[idx] = nametable
        
    # Write the compiled CHR file
    chr_bytes = bytearray()
    for tile in unique_tiles:
        chr_bytes.extend(tile)
        
    # Print statistics
    print(f"Total unique tiles generated: {len(unique_tiles)} (Max allowed in Bank half is 256)")
    print(f"Total CHR size: {len(chr_bytes)} bytes")
    
    # Write the CHR file
    out_chr_path = "assets/silent_sorrow_text.chr"
    with open(out_chr_path, "wb") as f:
        f.write(chr_bytes)
    print(f"Successfully wrote raw CHR to {out_chr_path}")
    
    # Generate the NESFab array declarations
    print("\n--- COPY THE CODE BELOW ---")
    for idx in image_indices:
        nam = nametables[idx]
        array_str = ", ".join(str(val) for val in nam)
        print(f"ct U[240] SORROW_NAM_{idx} = U[240]({array_str})")
    print("---------------------------\n")

if __name__ == "__main__":
    main()


import os
from PIL import Image, ImageChops
import math

def mse(img1, img2):
    h1, w1 = img1.shape
    h2, w2 = img2.shape
    diff = img1 - img2
    err = np.sum(diff**2)
    mse = err / (float(h1*w1))
    return mse

def pixel_match(img_tile, ref_img, tolerance=30):
    # exact match check
    if img_tile.size != ref_img.size:
        return False
    
    # simplistic pixel diff
    diff = ImageChops.difference(img_tile, ref_img)
    if diff.getbbox() is None:
        return True
    
    # Calculate average difference
    stat = diff.convert("L").getextrema()
    if stat[1] < tolerance:
        return True
    return False

def create_bone_bars(size=(16,16)):
    # Create a 16x16 bone bar tile
    # Background Black
    img = Image.new("RGB", size, (0,0,0))
    pixels = img.load()
    
    # Colors (approx from palette)
    white = (252, 252, 252)
    grey = (188, 188, 188)
    dark = (0, 0, 0) # black
    red = (168, 16, 0) # deep red (if needed, but keeping to greyscale for bars)
    
    # Pattern: Two vertical bone-like columns
    # Col 1: x=4,5,6
    # Col 2: x=10,11,12
    
    for y in range(16):
        # Left Bar
        pixels[4, y] = grey
        pixels[5, y] = white
        pixels[6, y] = grey
        
        # Right Bar
        pixels[10, y] = grey
        pixels[11, y] = white
        pixels[12, y] = grey
        
        # Knuckles / Joints (every 6 pixels)
        if y % 6 in [0, 1]:
            # Left knuckle
            pixels[3, y] = white
            pixels[7, y] = white
            # Right knuckle
            pixels[9, y] = white
            pixels[13, y] = white
            
    return img

def main():
    bg1_path = "c:\\Workspace\\NES\\nesfab\\examples\\LuciYFer\\assets\\bg1.png"
    jail_ref_path = "c:\\Workspace\\NES\\nesfab\\examples\\LuciYFer\\assets\\reference_jail.png"
    
    print("Loading Images...")
    bg1 = Image.open(bg1_path).convert("RGB")
    
    try:
        ref = Image.open(jail_ref_path).convert("RGB")
        ref = ref.resize((16,16), Image.NEAREST)
        has_ref = True
    except:
        print("Reference jail not found or invalid.")
        has_ref = False
        
    bone_bars = create_bone_bars((16,16))
    
    # Scan for the tile
    width, height = bg1.size
    found_count = 0
    
    new_bg1 = bg1.copy()
    
    for y in range(0, height, 16):
        for x in range(0, width, 16):
            tile = bg1.crop((x, y, x+16, y+16))
            
            match = False
            if has_ref:
                if pixel_match(tile, ref, tolerance=60): # High tolerance as generation might be noisy
                    match = True
            
            # If we don't have a good ref match, we might have to rely on coordinate heuristics?
            # But earlier creation should have put it somewhere.
            
            if match:
                print(f"Found Jail Tile at {x},{y}. Replacing with Bone Bars.")
                new_bg1.paste(bone_bars, (x, y))
                found_count += 1
                
    if found_count == 0:
        print("No Jail Tile found matching reference! trying loose matching...")
        # Fallback? Maybe just look for the grey box?
        # Or force the user to provide coordinates?
        # Let's try to assume it's the only mostly-grey block?
        pass

    if found_count > 0:
        new_bg1.save(bg1_path)
        print(f"Saved update to {bg1_path} with {found_count} replacements.")
    else:
        print("Could not update. No matching tiles found.")

if __name__ == "__main__":
    main()

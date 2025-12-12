
import os
from PIL import Image

def analyze_and_fix(original_path, current_path):
    print(f"Analyzing original: {original_path}")
    try:
        with Image.open(original_path) as img:
            print(f"Original: Format={img.format}, Size={img.size}, Mode={img.mode}")
            orig_size = img.size
            orig_mode = img.mode
            orig_info = img.info
    except Exception as e:
        print(f"Failed to open original: {e}")
        return

    print(f"Analyzing current: {current_path}")
    try:
        current_img = Image.open(current_path)
        print(f"Current: Format={current_img.format}, Size={current_img.size}, Mode={current_img.mode}")
        
        # Determine if we need to fix it
        needs_fix = False
        if current_img.size != orig_size:
            print("Size mismatch! resizing/cropping...")
            needs_fix = True
        
        # NESFAB might require specific encoding. 
        # Often it wants indexed color (P) or specific RGB. 
        # If original was P, we might want to convert, but usually RGB is fine unless it's strict.
        # But the error "incorrect PNG signature" usually means the file is actually not a valid PNG or has bytes in front of the header.
        
        if needs_fix or True: # Force re-save to ensure valid PNG structure
            print("Re-saving image to ensure validity and correct size...")
            # Resize if needed
            if current_img.size != orig_size:
                current_img = current_img.resize(orig_size, Image.NEAREST)
            
            # Save
            current_img.save(current_path, format="PNG")
            print("Saved.")
            
    except Exception as e:
        print(f"Failed to open current or fix it: {e}")
        # If the file is properly corrupt (header issues), we might need to restore from backup or previous step, but let's see.

if __name__ == "__main__":
    analyze_and_fix("c:\\Workspace\\NES\\nesfab\\examples\\LuciYFer\\assets\\bg1.png.bak", "c:\\Workspace\\NES\\nesfab\\examples\\LuciYFer\\assets\\bg1.png")

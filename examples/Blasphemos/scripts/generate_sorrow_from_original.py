import os
from PIL import Image, ImageDraw

def generate_frames_from_original():
    os.makedirs('assets', exist_ok=True)
    
    # Load the original high-resolution pixel art
    orig = Image.open('assets/blasphemous-dead-1920x1080.png')
    
    # 4-color palette matching standard NES colors:
    # 0: Black (Background)
    # 1: Deep Crimson Red ($05) - Shadow silhouettes / Blood / Gothic background
    # 2: Cold Silver-Blue ($2C) - Steel armor / sword details
    # 3: Pure White ($30) - Visor shine / sparks / sky glow
    palette = [
        0, 0, 0,          # 0: Black
        120, 24, 0,       # 1: Deep Crimson
        148, 148, 252,    # 2: Silver-Blue
        255, 255, 255     # 3: White
    ]
    # Pad to 256 colors for Indexed PNG
    palette += [0] * (768 - len(palette))
    
    # Define crops that simulate a cinematic pan and zoom on the Penitent One standing on the dead bodies:
    # Bounding box of artwork is roughly: x=[284, 1614], y=[218, 981]
    # The Penitent One is typically in the center (x around 900 to 1050, y around 250 to 800)
    crops = [
        # Frame 0: Wide establishing shot of the gothic pile
        (500, 300, 1400, 950),
        # Frame 1: Zooming in closer to the mound
        (650, 350, 1300, 900),
        # Frame 2: Pan down to the heap of silent bodies
        (750, 500, 1250, 950),
        # Frame 3: Pan up to the Penitent One standing tall
        (800, 320, 1150, 720),
        # Frame 4: Closer shot on the Penitent One's chest and helmet
        (850, 280, 1100, 570),
        # Frame 5: Close up on the pointed helmet (The Cone of Silent Sorrow)
        (880, 250, 1060, 480),
        # Frame 6: Extreme close up on his glowing visor
        (890, 300, 1030, 440),
        # Frame 7: The visor flashes with a divine white cross/glow!
        (895, 305, 1025, 435)
    ]
    
    # We will create a palette image to map colors properly
    palette_im = Image.new('P', (1, 1))
    palette_im.putpalette(palette)

    for idx, box in enumerate(crops):
        # 1. Crop the original image
        cropped = orig.crop(box)
        
        # 2. Resize to 128x128 with Lanczos for super sharp downsampling
        resized = cropped.resize((128, 128), Image.Resampling.LANCZOS)
        
        # 3. Convert to RGB to discard original indices
        rgb = resized.convert('RGB')
        
        # 4. Map the colors to our custom 4-color NES palette using nearest color match
        # This keeps the pixel art crisp and prevents noisy dithering
        mapped = rgb.quantize(palette=palette_im, dither=Image.Dither.NONE)
        
        # 5. For Frame 7 (the final epic flash), let's draw a glowing white visor/cross
        if idx == 7:
            draw = ImageDraw.Draw(mapped)
            # Find the visor area (roughly in the center of the cropped face, around x=64, y=60)
            # Let's draw a bright white visor gleam!
            draw.rectangle((50, 55, 78, 62), fill=3)
            # Draw cross flare rays from the visor
            draw.line((64, 40, 64, 80), fill=3, width=2)
            draw.line((44, 58, 84, 58), fill=3, width=2)

        # Save the indexed frame
        mapped.save(f'assets/silent_sorrow_{idx}.png')
        print(f"Generated assets/silent_sorrow_{idx}.png from original artwork.")

if __name__ == '__main__':
    generate_frames_from_original()

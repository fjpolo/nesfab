import cv2
import os
from PIL import Image, ImageEnhance

def extract_original_cutscene_frames():
    os.makedirs('assets', exist_ok=True)
    vid = cv2.VideoCapture('assets/original_cinematic.mp4')
    
    # 4-color palette matching standard NES colors:
    # 0: Black (Background)
    # 1: Deep Crimson Red ($05) - Shadows / Silhouettes / Blood
    # 2: Cold Silver-Blue ($2C) - Metal armor / sword outlines
    # 3: Pure White ($30) - Flashes / glows / visor gleam
    palette = [
        0, 0, 0,          # 0: Black
        120, 24, 0,       # 1: Deep Crimson
        148, 148, 252,    # 2: Silver-Blue
        255, 255, 255     # 3: White
    ]
    palette += [0] * (768 - len(palette))
    
    palette_im = Image.new('P', (1, 1))
    palette_im.putpalette(palette)
    
    # The video has a total of 4226 frames.
    # The actual narrative sequence containing the woman begging the Miracle to transform her statue
    # and the sword piercing her chest happens in the very beginning. Let's sample 8 highly dramatic frames
    # from the opening sequence of the video (approx frames 100 to 1200).
    # Specifically, we want:
    # Frame 0: The kneeling woman praying (around frame 120)
    # Frame 1: Woman striking her chest (around frame 240)
    # Frame 2: Close-up on the painful prayer (around frame 360)
    # Frame 3: The Miracle manifesting and statue cracking (around frame 480)
    # Frame 4: The statue turning into the Mea Culpa blade (around frame 600)
    # Frame 5: The sword piercing through her chest (around frame 720)
    # Frame 6: The woman turning into a grey kneeling stone monument with the sword embedded (around frame 840)
    # Frame 7: The Penitent One walking up and pulling Mea Culpa from her petrified breast (around frame 1050)
    
    target_frames = [120, 240, 360, 480, 600, 720, 840, 1050]
    
    for idx, frame_num in enumerate(target_frames):
        vid.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
        ret, frame = vid.read()
        if not ret:
            print(f"Failed to read frame {frame_num}")
            continue
            
        # Convert BGR (OpenCV) to RGB (PIL)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(rgb_frame)
        
        # Crop to square 1:1 format (extract center 360x360 window)
        w, h = im.size
        left = (w - h) // 2
        cropped = im.crop((left, 0, left + h, h))
        
        # Enhance Brightness (boost by 2.2x to reveal all details)
        enhanced = ImageEnhance.Brightness(cropped).enhance(2.2)
        # Enhance Contrast (boost by 1.8x to make shapes and borders extremely defined)
        enhanced = ImageEnhance.Contrast(enhanced).enhance(1.8)
        
        # Resize to sharp 128x128 for NES nametable compatibility
        resized = enhanced.resize((128, 128), Image.Resampling.LANCZOS)
        
        # Quantize using Floyd-Steinberg dithering for gorgeous retro details and maximum visibility!
        mapped = resized.quantize(palette=palette_im, dither=Image.Dither.FLOYDSTEINBERG)
        
        # Save frame
        mapped.save(f'assets/silent_sorrow_{idx}.png')
        print(f"Successfully extracted and generated assets/silent_sorrow_{idx}.png from video frame {frame_num}.")
        
    vid.release()

if __name__ == '__main__':
    extract_original_cutscene_frames()

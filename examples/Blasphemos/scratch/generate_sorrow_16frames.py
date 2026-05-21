import cv2
import os
from PIL import Image, ImageEnhance

def extract_high_quality_frames():
    os.makedirs('assets', exist_ok=True)
    vid = cv2.VideoCapture('assets/original_cinematic.mp4')
    
    palette = [
        0, 0, 0,          # 0: Black
        120, 24, 0,       # 1: Deep Crimson
        148, 148, 252,    # 2: Silver-Blue
        255, 255, 255     # 3: White
    ]
    palette += [0] * (768 - len(palette))
    
    palette_im = Image.new('P', (1, 1))
    palette_im.putpalette(palette)
    
    # We want 16 gorgeous, high-fidelity frames to double the quality and fluidity!
    # Let's map target frames from the critical story segments (Begging, Crack, Blade form, Pierce, Petrification, Awakening)
    target_frames = [
        80,   # 0. Kneeling prayer wide
        160,  # 1. Praying close
        240,  # 2. Chest striking pose
        320,  # 3. Striking impact
        400,  # 4. Crack starts on statue
        480,  # 5. Golden light breaks out of statue
        560,  # 6. Blade tip forms
        640,  # 7. Blade crossguard forms
        720,  # 8. Full Mea Culpa sword pierces woman
        800,  # 9. Liquid blood splash on floor
        880,  # 10. Monument petrifies
        960,  # 11. Silent sorrow chapel wide
        1040, # 12. Penitent One walking in
        1120, # 13. Penitent One kneeling at monument
        1200, # 14. Grasping the sword hilt
        1280  # 15. Pulling Mea Culpa out
    ]
    
    for idx, frame_num in enumerate(target_frames):
        vid.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
        ret, frame = vid.read()
        if not ret:
            print(f"Failed to read frame {frame_num}")
            continue
            
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(rgb_frame)
        
        w, h = im.size
        left = (w - h) // 2
        cropped = im.crop((left, 0, left + h, h))
        
        # High quality enhancement settings
        enhanced = ImageEnhance.Brightness(cropped).enhance(2.4)
        enhanced = ImageEnhance.Contrast(enhanced).enhance(2.0)
        
        resized = enhanced.resize((128, 128), Image.Resampling.LANCZOS)
        
        mapped = resized.quantize(palette=palette_im, dither=Image.Dither.FLOYDSTEINBERG)
        
        mapped.save(f'assets/silent_sorrow_{idx}.png')
        print(f"Extracted enhanced frame {idx} (video frame {frame_num})")
        
    vid.release()

if __name__ == '__main__':
    extract_high_quality_frames()

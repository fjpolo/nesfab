import os
from PIL import Image, ImageEnhance, ImageOps

media_dir = r"C:\Users\polo\.gemini\antigravity\brain\0fbfe38a-f0ab-4aab-9a1f-9a2a210d8dcc"
files = [
    "media__1779373733930.png", # 0. "It is not the sun rising..."
    "media__1779373763356.png", # 1. "Because it is my Guilt..."
    "media__1779373779346.png", # 2. Kneeling woman wide
    "media__1779373793162.png", # 3. "Make my chest hurt..."
    "media__1779373831792.png"  # 4. Close up woman with subtitle
]

# NES Gothic 4-color palette:
# 0: Black ($0F)
# 1: Deep Crimson ($05)
# 2: Silver-Blue ($2C)
# 3: White ($30)
palette = [
    0, 0, 0,          # 0: Black
    120, 24, 0,       # 1: Deep Crimson
    148, 148, 252,    # 2: Silver-Blue
    255, 255, 255     # 3: White
]
palette += [0] * (768 - len(palette))

palette_im = Image.new('P', (1, 1))
palette_im.putpalette(palette)

for idx, f in enumerate(files):
    path = os.path.join(media_dir, f)
    im = Image.open(path).convert('RGB')
    
    # Let's determine if this is a text card or an artwork card.
    # Text cards have indices 0, 1, 3.
    is_text = idx in [0, 1, 3]
    
    if is_text:
        # For text cards, crop closely to the text to keep it large and legible.
        # Find the bounding box of non-black pixels to crop perfectly around the text.
        gray = ImageOps.grayscale(im)
        # Threshold the grayscale to make background pure black
        thresh = gray.point(lambda p: 255 if p > 30 else 0)
        bbox = thresh.getbbox()
        if bbox:
            cropped = im.crop(bbox)
        else:
            cropped = im
            
        # Add black border padding to make it a square before resizing
        w, h = cropped.size
        max_dim = max(w, h)
        padded = Image.new('RGB', (max_dim, max_dim), (0, 0, 0))
        padded.paste(cropped, ((max_dim - w) // 2, (max_dim - h) // 2))
        
        # High contrast boost for maximum text crispness
        enhanced = ImageEnhance.Contrast(padded).enhance(3.0)
        enhanced = ImageEnhance.Brightness(enhanced).enhance(1.5)
        
        resized = enhanced.resize((128, 128), Image.Resampling.LANCZOS)
        # No dither for text cards to keep font perfectly solid and sharp!
        mapped = resized.quantize(palette=palette_im, dither=Image.Dither.NONE)
    else:
        # Artwork card: crop to square centered on the action
        w, h = im.size
        dim = min(w, h)
        left = (w - dim) // 2
        top = (h - dim) // 2
        cropped = im.crop((left, top, left + dim, top + dim))
        
        # Boost brightness/contrast to pop details out of the dark gothic background
        enhanced = ImageEnhance.Brightness(cropped).enhance(2.5)
        enhanced = ImageEnhance.Contrast(enhanced).enhance(2.0)
        
        resized = enhanced.resize((128, 128), Image.Resampling.LANCZOS)
        # Gorgeous Floyd-Steinberg dither for stunning 8-bit texturing!
        mapped = resized.quantize(palette=palette_im, dither=Image.Dither.FLOYDSTEINBERG)
        
    mapped.save(f'assets/silent_sorrow_{idx}.png')
    print(f"Processed Frame {idx} ({f}) -> assets/silent_sorrow_{idx}.png successfully.")

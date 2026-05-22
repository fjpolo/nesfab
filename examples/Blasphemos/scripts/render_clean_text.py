import os
from PIL import Image

def main():
    font_path = "assets/font.png"
    if not os.path.exists(font_path):
        print("Error: font.png not found!")
        return

    font_img = Image.open(font_path).convert("RGBA")
    
    # 4-color palette:
    # 0: Black, 1: Deep Crimson Red, 2: Silver-Blue, 3: White
    palette = [
        0, 0, 0,
        120, 24, 0,
        148, 148, 252,
        255, 255, 255
    ]
    palette += [0] * (768 - len(palette))
    
    palette_im = Image.new('P', (1, 1))
    palette_im.putpalette(palette)
    
    # Define text cards with exact line splitting to fit within 20 chars per line (160px wide)
    cards = {
        0: [
            "It is not the",
            "sun rising,",
            "but our sins"
        ],
        1: [
            "Because it is my",
            "guilt, I claim you,",
            "Grievous Miracle."
        ],
        3: [
            "Make my chest hurt",
            "with regret, forward",
            "your punishment,",
            "and nail it deep;"
        ],
        5: [
            "Shape my Guilt,",
            "once again."
        ]
    }
    
    for idx, lines in cards.items():
        # Create a solid black RGBA image of size 160x96
        canvas = Image.new("RGBA", (160, 96), (0, 0, 0, 255))
        
        # Center vertically
        total_height = len(lines) * 8
        start_y = (96 - total_height) // 2
        
        for line_idx, line in enumerate(lines):
            y = start_y + line_idx * 8
            
            # Center horizontally
            total_width = len(line) * 8
            start_x = (160 - total_width) // 2
            
            for char_idx, char in enumerate(line):
                x = start_x + char_idx * 8
                
                # Get char position in assets/font.png
                ascii_code = ord(char)
                font_idx = ascii_code - 32
                if font_idx < 0 or font_idx >= 256:
                    font_idx = 0 # default to space
                    
                col = font_idx % 16
                row = font_idx // 16
                
                # Crop 8x8 character tile from font
                char_tile = font_img.crop((col * 8, row * 8, col * 8 + 8, row * 8 + 8))
                
                # Paste it onto canvas
                canvas.paste(char_tile, (x, y), char_tile)
                
        # Force the top-left 8x8 block (tile 0) of the canvas to be pure solid black
        # to ensure tile 0 remains the black empty tile for clear nametable!
        for ty in range(8):
            for tx in range(8):
                canvas.putpixel((tx, ty), (0, 0, 0, 255))
                
        # Convert to palette mode (no dithering)
        quantized = canvas.convert("RGB").quantize(palette=palette_im, dither=Image.Dither.NONE)
        
        out_path = f"assets/silent_sorrow_{idx}.png"
        quantized.save(out_path)
        print(f"Saved custom clean text card to {out_path}")

if __name__ == "__main__":
    main()

import os
from PIL import Image, ImageDraw, ImageFont

def create_frames():
    os.makedirs('assets', exist_ok=True)
    
    # 4-color palette matching standard NES colors:
    # 0: Black (Background)
    # 1: Dark Crimson (Shadow/Sword/Thorns)
    # 2: Golden Yellow (Miracle Cross/Glow/Text)
    # 3: White (Sword Blade/Shimmer/Flashes)
    palette = [
        0, 0, 0,          # 0: Black
        128, 0, 0,        # 1: Dark Crimson
        228, 180, 0,      # 2: Golden Yellow
        255, 255, 255     # 3: White
    ]
    # Pad to 256 colors for Indexed PNG
    palette += [0] * (768 - len(palette))

    # Procedural drawing function for a frame
    for f in range(8):
        # Create an 8-bit indexed image (mode 'P')
        im = Image.new('P', (128, 128), 0)
        im.putpalette(palette)
        draw = ImageDraw.Draw(im)

        # Draw backgrounds/decorations
        if f > 0:
            # Subtle crimson vignette / background glow in the center
            glow_radius = 20 + f * 8
            if f < 7:
                draw.ellipse((64 - glow_radius, 64 - glow_radius, 64 + glow_radius, 64 + glow_radius), outline=1, width=2)
        
        # Draw the Miracle Cross in the background (glowing gold)
        if f in [2, 3, 4, 5, 6]:
            cross_glow = f - 1
            # Draw glowing halo or vertical/horizontal bars of the cross
            # Vertical bar
            draw.rectangle((62, 10, 66, 110), fill=2 if f < 6 else 3)
            # Horizontal bar
            draw.rectangle((36, 42, 92, 46), fill=2 if f < 6 else 3)
            
            # Additional cross lines/decorations
            draw.line((64, 5, 64, 115), fill=2)
            draw.line((30, 44, 98, 44), fill=2)

        # Draw the Sword (Mea Culpa)
        # 1. Hilt and Pommel
        draw.line((64, 80, 64, 100), fill=1, width=2) # Grip
        draw.ellipse((61, 98, 67, 104), fill=1)       # Pommel
        
        # 2. Crossguard
        draw.line((48, 80, 80, 80), fill=1, width=2)   # Crossguard bar
        draw.ellipse((45, 78, 49, 82), fill=1)         # Left crossguard end
        draw.ellipse((79, 78, 83, 82), fill=1)         # Right crossguard end

        # 3. Thorns wrapping around crossguard & hilt (stylized details)
        if f > 1:
            draw.line((48, 80, 56, 88), fill=1 if f < 4 else 2)
            draw.line((80, 80, 72, 88), fill=1 if f < 4 else 2)

        # 4. Blade
        # Center of blade is column 63-64.
        if f == 0:
            # Outline only
            draw.line((64, 18, 64, 79), fill=1, width=2)
        elif f == 1:
            # Crimson awakening
            draw.line((64, 18, 64, 79), fill=1, width=2)
            draw.line((64, 25, 64, 75), fill=3)
        elif f in [2, 3, 4, 5]:
            # Glowing blade
            draw.line((63, 18, 65, 79), fill=1)
            draw.line((64, 18, 64, 79), fill=3)
        elif f == 6:
            # Pure white shimmer flash
            draw.line((62, 17, 66, 80), fill=3)
        elif f == 7:
            # Fade to black (only silhouette remains)
            draw.line((64, 18, 64, 79), fill=1)

        # Draw Thorns on the Blade
        if f >= 2 and f < 7:
            # Thorns wrapping around the blade (Gold or Red depending on frame)
            thorn_color = 1 if f < 4 else 2
            draw.line((60, 30, 68, 38), fill=thorn_color)
            draw.line((68, 45, 60, 53), fill=thorn_color)
            draw.line((60, 60, 68, 68), fill=thorn_color)

        # Draw flying sparks/particles (small dots)
        if f in [3, 4, 5]:
            draw.point((50, 35), fill=2)
            draw.point((78, 48), fill=2)
            draw.point((45, 70), fill=1)
            draw.point((82, 60), fill=2)
            draw.point((55, 90), fill=1)
            draw.point((72, 25), fill=2)
        elif f == 6:
            # More active white sparks
            draw.point((48, 30), fill=3)
            draw.point((80, 42), fill=3)
            draw.point((42, 65), fill=3)
            draw.point((85, 55), fill=3)

        # Draw "SOUTHPOLE PRESENTS" Text
        if f in [5, 6]:
            # Top Text "SOUTHPOLE"
            # Draw letter by letter or procedurally if font not loaded.
            # To be 100% robust and independent of external ttf files,
            # we will draw the letters using pixel line strokes!
            
            # "SOUTHPOLE" letter strokes centered at top (y=15 to 22)
            # S
            draw.line((24, 15, 28, 15), fill=2 if f==5 else 3)
            draw.line((24, 15, 24, 18), fill=2 if f==5 else 3)
            draw.line((24, 18, 28, 18), fill=2 if f==5 else 3)
            draw.line((28, 18, 28, 21), fill=2 if f==5 else 3)
            draw.line((24, 21, 28, 21), fill=2 if f==5 else 3)
            # O
            draw.rectangle((31, 15, 35, 21), outline=2 if f==5 else 3, fill=0)
            # U
            draw.line((38, 15, 38, 21), fill=2 if f==5 else 3)
            draw.line((42, 15, 42, 21), fill=2 if f==5 else 3)
            draw.line((38, 21, 42, 21), fill=2 if f==5 else 3)
            # T
            draw.line((45, 15, 49, 15), fill=2 if f==5 else 3)
            draw.line((47, 15, 47, 21), fill=2 if f==5 else 3)
            # H
            draw.line((52, 15, 52, 21), fill=2 if f==5 else 3)
            draw.line((56, 15, 56, 21), fill=2 if f==5 else 3)
            draw.line((52, 18, 56, 18), fill=2 if f==5 else 3)
            # P
            draw.line((72, 15, 72, 21), fill=2 if f==5 else 3)
            draw.line((72, 15, 76, 15), fill=2 if f==5 else 3)
            draw.line((76, 15, 76, 18), fill=2 if f==5 else 3)
            draw.line((72, 18, 76, 18), fill=2 if f==5 else 3)
            # O
            draw.rectangle((79, 15, 83, 21), outline=2 if f==5 else 3, fill=0)
            # L
            draw.line((86, 15, 86, 21), fill=2 if f==5 else 3)
            draw.line((86, 21, 90, 21), fill=2 if f==5 else 3)
            # E
            draw.line((93, 15, 93, 21), fill=2 if f==5 else 3)
            draw.line((93, 15, 97, 15), fill=2 if f==5 else 3)
            draw.line((93, 18, 96, 18), fill=2 if f==5 else 3)
            draw.line((93, 21, 97, 21), fill=2 if f==5 else 3)

            # Bottom Text "PRESENTS" (y=112 to 118)
            # P
            draw.line((34, 112, 34, 118), fill=1)
            draw.line((34, 112, 38, 112), fill=1)
            draw.line((38, 112, 38, 115), fill=1)
            draw.line((34, 115, 38, 115), fill=1)
            # R
            draw.line((41, 112, 41, 118), fill=1)
            draw.line((41, 112, 45, 112), fill=1)
            draw.line((45, 112, 45, 115), fill=1)
            draw.line((41, 115, 45, 115), fill=1)
            draw.line((43, 115, 45, 118), fill=1)
            # E
            draw.line((48, 112, 48, 118), fill=1)
            draw.line((48, 112, 52, 112), fill=1)
            draw.line((48, 115, 51, 115), fill=1)
            draw.line((48, 118, 52, 118), fill=1)
            # S
            draw.line((55, 112, 59, 112), fill=1)
            draw.line((55, 112, 55, 115), fill=1)
            draw.line((55, 115, 59, 115), fill=1)
            draw.line((59, 115, 59, 118), fill=1)
            draw.line((55, 118, 59, 118), fill=1)
            # E
            draw.line((62, 112, 62, 118), fill=1)
            draw.line((62, 112, 66, 112), fill=1)
            draw.line((62, 115, 65, 115), fill=1)
            draw.line((62, 118, 66, 118), fill=1)
            # N
            draw.line((69, 112, 69, 118), fill=1)
            draw.line((69, 112, 73, 118), fill=1)
            draw.line((73, 112, 73, 118), fill=1)
            # T
            draw.line((76, 112, 80, 112), fill=1)
            draw.line((78, 112, 78, 118), fill=1)
            # S
            draw.line((83, 112, 87, 112), fill=1)
            draw.line((83, 112, 83, 115), fill=1)
            draw.line((83, 115, 87, 115), fill=1)
            draw.line((87, 115, 87, 118), fill=1)
            draw.line((83, 118, 87, 118), fill=1)

        im.save(f'assets/intro_frame_{f}.png')
        print(f"Generated assets/intro_frame_{f}.png")

if __name__ == '__main__':
    create_frames()

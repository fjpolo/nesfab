import os
from PIL import Image, ImageDraw

def generate_sorrow_frames():
    os.makedirs('assets', exist_ok=True)
    
    # 4-color palette matching standard NES colors:
    # 0: Black (Background)
    # 1: Deep Crimson Red ($05 / $06) - Silhouettes / Blood / Shadows
    # 2: Cold Silver-Blue ($1B / $2C) - Armor / Sword / Steel
    # 3: Pure White ($30) - Highlights / Divine Glow / visor shine
    palette = [
        0, 0, 0,          # 0: Black
        120, 24, 0,       # 1: Deep Crimson
        148, 148, 252,    # 2: Silver-Blue
        255, 255, 255     # 3: White
    ]
    # Pad to 256 colors for Indexed PNG
    palette += [0] * (768 - len(palette))

    # Procedural drawing function for the Silent Sorrow Cutscene
    for f in range(8):
        # Create an 8-bit indexed image (mode 'P')
        im = Image.new('P', (128, 128), 0)
        im.putpalette(palette)
        draw = ImageDraw.Draw(im)

        if f == 0:
            # --- Frame 0: The Pile of Silent Bodies ---
            # Draw a massive gothic mound of silent bodies in silhouette
            # Draw base mound (Crimson silhouette)
            draw.ellipse((10, 80, 118, 150), fill=1)
            draw.ellipse((30, 60, 98, 140), fill=1)
            draw.ellipse((45, 50, 83, 110), fill=1)
            
            # Draw individual details of bodies (swords/limbs sticking out)
            draw.line((64, 45, 64, 65), fill=2, width=2)  # Sword sticking out
            draw.line((58, 50, 70, 50), fill=2, width=1)  # Sword crossguard
            draw.line((35, 65, 25, 55), fill=1, width=2)  # Corpse arm
            draw.line((90, 75, 105, 65), fill=1, width=2) # Corpse arm
            
            # Add some silver highlights to outline the mound
            draw.line((45, 50, 55, 58), fill=2)
            draw.line((83, 110, 95, 125), fill=2)

        elif f == 1:
            # --- Frame 1: The Crucified Hanging on the Cross ---
            # Draw a wooden cross
            draw.rectangle((60, 15, 68, 115), fill=1) # Vertical shaft
            draw.rectangle((34, 40, 94, 48), fill=1)  # Horizontal bar
            
            # Draw the Crucified body (Silver-Blue)
            draw.ellipse((61, 30, 67, 36), fill=2)   # Head
            draw.line((64, 36, 64, 75), fill=2, width=3) # Torso/Spine
            draw.line((64, 44, 38, 44), fill=2, width=2) # Left arm
            draw.line((64, 44, 90, 44), fill=2, width=2) # Right arm
            draw.line((64, 75, 54, 100), fill=2, width=2) # Left leg
            draw.line((64, 75, 74, 100), fill=2, width=2) # Right leg
            
            # Dripping blood (Crimson)
            draw.line((64, 100, 64, 112), fill=1) # Blood from feet
            draw.line((38, 44, 38, 56), fill=1)   # Blood from left hand
            draw.line((90, 44, 90, 56), fill=1)   # Blood from right hand
            
            # Highlight crown of thorns
            draw.point((64, 29), fill=3)

        elif f == 2:
            # --- Frame 2: The Penitent One Kneeling ---
            # Crimson body pile in the background
            draw.ellipse((0, 90, 128, 150), fill=1)
            
            # Penitent One kneeling (Silver-Blue)
            # Head (bowed down)
            draw.ellipse((60, 55, 68, 63), fill=2)
            # Kneeling armor/torso
            draw.rectangle((58, 63, 70, 95), fill=2)
            # Kneeling legs
            draw.line((58, 95, 48, 105), fill=2, width=3)
            draw.line((70, 95, 80, 105), fill=2, width=3)
            
            # Pointed helmet resting on the ground in front of him
            draw.polygon([(42, 105), (32, 70), (46, 105)], fill=1) # Helmet silhouette
            draw.polygon([(42, 105), (32, 70), (46, 105)], outline=2) # Helmet outlines

        elif f == 3:
            # --- Frame 3: The Pointed Helmet Close-up ---
            # Tall pointed helmet held in front of the screen
            # Background is dark crimson gothic borders
            draw.ellipse((10, 10, 118, 118), outline=1, width=1)
            
            # Pointed Helmet (Cone of Silent Sorrow)
            # A very tall triangle in the center
            draw.polygon([(64, 10), (40, 105), (88, 105)], fill=2)
            # Helmet decorations (Crimson lines)
            draw.line((64, 10, 64, 105), fill=1, width=2) # Center thorn crease
            draw.line((48, 105, 52, 60), fill=1)
            draw.line((80, 105, 76, 60), fill=1)
            
            # Hands holding the helmet base
            draw.ellipse((35, 100, 48, 112), fill=2) # Left gauntlet
            draw.ellipse((80, 100, 93, 112), fill=2) # Right gauntlet

        elif f == 4:
            # --- Frame 4: Blood Dripping into the Helmet ---
            # Pointed helmet held facing upward
            # We see the hollow open base of the helmet (ellipse)
            draw.ellipse((40, 75, 88, 115), fill=2, outline=1, width=2)
            # The upper conical body extending off-screen downward
            draw.polygon([(40, 95), (64, 128), (88, 95)], fill=2)
            
            # Sacred blood droplets dripping into it from above
            draw.line((64, 15, 64, 25), fill=1, width=2)   # Dripping stream
            draw.ellipse((62, 35, 66, 42), fill=1)          # Droplet 1
            draw.ellipse((63, 50, 65, 55), fill=1)          # Droplet 2
            
            # White sparkles/ripples inside the helmet base
            draw.ellipse((58, 85, 70, 95), outline=3, width=1)
            draw.point((64, 90), fill=3)

        elif f == 5:
            # --- Frame 5: Putting the Helmet on (Brilliant Flash!) ---
            # Silhouette of Penitent One's upper body putting on the pointed helmet
            draw.rectangle((52, 65, 76, 128), fill=1) # Armor Torso
            # Tall pointed helmet being lowered on
            draw.polygon([(64, 5), (48, 75), (80, 75)], fill=2)
            draw.line((64, 5, 64, 75), fill=1)
            
            # Hands raising the helmet
            draw.line((35, 95, 48, 75), fill=2, width=2) # Left arm
            draw.line((93, 95, 80, 75), fill=2, width=2) # Right arm
            
            # A divine, pure white explosive glow around the helmet
            draw.ellipse((44, 45, 84, 85), outline=3, width=2)
            draw.line((64, 20, 64, 40), fill=3, width=2)  # Top flash ray
            draw.line((35, 60, 50, 60), fill=3, width=2)  # Left flash ray
            draw.line((93, 60, 78, 60), fill=3, width=2)  # Right flash ray

        elif f == 6:
            # --- Frame 6: Penitent One Stands up with Mea Culpa (Visor Glow!) ---
            # Upper body portrait of the Penitent One in full armor
            draw.rectangle((44, 80, 84, 128), fill=2)  # Chestplate armor
            # Gothic thorn pattern on chestplate
            draw.line((44, 90, 84, 105), fill=1, width=2)
            
            # Tall pointed helmet on head
            draw.polygon([(64, 15), (50, 80), (78, 80)], fill=2)
            draw.line((64, 15, 64, 80), fill=1, width=2) # Helmet crease
            
            # Visor opening
            draw.rectangle((58, 68, 70, 72), fill=1)
            # Glowing Crimson Visor Eye (Visor glow!)
            draw.point((64, 70), fill=3)
            draw.point((63, 70), fill=3)
            
            # Sword Mea Culpa held vertically in front
            draw.line((40, 45, 40, 115), fill=2, width=2) # Blade
            draw.line((32, 100, 48, 100), fill=1, width=2) # Crossguard
            draw.line((40, 38, 40, 45), fill=3, width=2)  # Glowing sword tip

        elif f == 7:
            # --- Frame 7: Fade to Crimson Mist ---
            # Screen filled with heavy crimson fog/mist
            # Subtle silver/white silhouette of Mea Culpa glowing in the center
            for r in range(0, 128, 4):
                draw.rectangle((0, r, 128, r+2), fill=1) # Mist lines
            
            # Glowing sword in center
            draw.line((64, 30, 64, 100), fill=2)
            draw.line((64, 25, 64, 30), fill=3) # White glowing tip

        im.save(f'assets/silent_sorrow_{f}.png')
        print(f"Generated assets/silent_sorrow_{f}.png")

if __name__ == '__main__':
    generate_sorrow_frames()

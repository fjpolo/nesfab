import json

with open('blasnesmous.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("PALETTES IN JSON:")
pals = data['palettes']['data']
# Each palette consists of 25 bytes? Wait, scratch/mapfab_to_json.py says:
# for _ in range(256 * 25): palette_data.append(get8())
# Wait! Let's see how many palettes there actually are.
num_palettes = data['palettes']['num']
print(f"Num Palettes: {num_palettes}")
# Let's see how they are defined in code.
# In level.macrofab: (@pal_#palette_name#)
# Let's search level.fab or another file for pal_0, pal_1 etc.

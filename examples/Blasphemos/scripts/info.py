import json

with open('blasnesmous.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("LEVELS IN JSON:")
for lvl in data['levels']:
    print(f"  Name: {lvl['name']}")
    print(f"    CHR: {lvl['chr']}")
    print(f"    Palette: {lvl['palette']}")
    print(f"    Metatile Set: {lvl['metatile_set']}")
    print(f"    Width: {lvl['width']}, Height: {lvl['height']}")
    print("-" * 30)

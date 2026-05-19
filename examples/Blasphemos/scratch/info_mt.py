import json

with open('blasnesmous.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("METATILE SETS:")
for mt in data['metatile_sets']:
    print(f"  Name: {mt['name']}")
    print(f"    CHR: {mt['chr']}")
    print(f"    Palette: {mt['palette']}")
    print("-" * 30)

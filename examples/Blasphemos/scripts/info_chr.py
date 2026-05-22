import json

with open('blasnesmous.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("CHR SETS IN JSON:")
for i, c in enumerate(data['chr']):
    print(f"  Index {i}: {c['name']} -> {c['path']}")

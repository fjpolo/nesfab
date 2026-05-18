import json
import os

def main():
    json_path = 'blasnesmous.json'
    if not os.path.exists(json_path):
        print(f"Error: {json_path} does not exist!")
        return

    # Load JSON
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Find l3
    l3_index = -1
    for i, lvl in enumerate(data['levels']):
        if lvl['name'] == 'l3':
            l3_index = i
            break

    if l3_index == -1:
        print("Error: Level 'l3' not found in JSON!")
        return

    l3 = data['levels'][l3_index]
    original_width = l3['width']
    original_height = l3['height']
    original_tiles = l3['tiles']
    original_objects = l3['objects']

    print(f"Found Level 'l3' with size {original_width}x{original_height} and {len(original_objects)} objects.")

    if original_width != 64:
        print(f"Warning: Level 'l3' width is already {original_width}, not 64! Maybe already split?")
        return

    # Split tiles using a proper Row-Major stride of 64 columns
    # Height is 16.
    # Level 3a is columns 0 to 31.
    # Level 3b is columns 32 to 63.
    tiles_a = []
    tiles_b = []
    w = original_width  # 64
    h = original_height  # 16
    
    for r in range(h):
        row_start = r * w
        # Columns 0 to 31 (Level 3a)
        tiles_a.extend(original_tiles[row_start : row_start + 32])
        # Columns 32 to 63 (Level 3b)
        tiles_b.extend(original_tiles[row_start + 32 : row_start + 64])

    # Split objects
    objects_a = []
    objects_b = []
    split_x = 32 * 16  # 512 pixels

    for obj in original_objects:
        obj_x = obj['x']
        if obj_x < split_x:
            objects_a.append(obj)
        else:
            # Shift X coordinate for objects in Level 3b
            new_obj = dict(obj)
            new_obj['x'] = obj_x - split_x
            objects_b.append(new_obj)

    # Create Level 3b
    l3b = {
        'chr': l3['chr'],
        'height': h,
        'macro': l3['macro'],
        'metatile_set': l3['metatile_set'],
        'name': 'l3b',
        'objects': objects_b,
        'palette': l3['palette'],
        'tiles': tiles_b,
        'width': 32
    }

    # Update Level 3a (keep name 'l3' for minimal code changes)
    l3['width'] = 32
    l3['tiles'] = tiles_a
    l3['objects'] = objects_a

    # Append Level 3b to the levels array
    data['levels'].append(l3b)

    # Save JSON back
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    print(f"Successfully split Level 'l3' into:")
    print(f"  - l3 (Level 3a): width=32, objects={len(objects_a)}")
    print(f"  - l3b (Level 3b): width=32, objects={len(objects_b)}")

if __name__ == '__main__':
    main()

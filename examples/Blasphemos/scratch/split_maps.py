import json
import os

def split_level(data, level_name, new_name, split_width=32):
    l_index = -1
    for i, lvl in enumerate(data['levels']):
        if lvl['name'] == level_name:
            l_index = i
            break

    if l_index == -1:
        print(f"Error: Level '{level_name}' not found!")
        return False

    l = data['levels'][l_index]
    original_width = l['width']
    original_height = l['height']
    original_tiles = l['tiles']
    original_objects = l['objects']

    if original_width <= split_width:
        print(f"Warning: Level '{level_name}' width is {original_width}, not greater than {split_width}! Skipping.")
        return False

    tiles_a = []
    tiles_b = []
    w = original_width
    h = original_height
    
    for r in range(h):
        row_start = r * w
        tiles_a.extend(original_tiles[row_start : row_start + split_width])
        tiles_b.extend(original_tiles[row_start + split_width : row_start + w])

    objects_a = []
    objects_b = []
    split_x = split_width * 16  # 16 pixels per tile

    for obj in original_objects:
        obj_x = obj['x']
        if obj_x < split_x:
            objects_a.append(obj)
        else:
            new_obj = dict(obj)
            new_obj['x'] = obj_x - split_x
            objects_b.append(new_obj)

    # Create new split level
    lb = {
        'chr': l['chr'],
        'height': h,
        'macro': l['macro'],
        'metatile_set': l['metatile_set'],
        'name': new_name,
        'objects': objects_b,
        'palette': l['palette'],
        'tiles': tiles_b,
        'width': w - split_width
    }

    # Update original level
    l['width'] = split_width
    l['tiles'] = tiles_a
    l['objects'] = objects_a

    # Append to levels array
    data['levels'].append(lb)

    print(f"Split '{level_name}' into '{level_name}' (w={split_width}) and '{new_name}' (w={w - split_width})")
    return True

def main():
    json_path = 'blasnesmous.json'
    if not os.path.exists(json_path):
        print(f"Error: {json_path} does not exist!")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    changed = False
    changed |= split_level(data, 'l2', 'l2b')
    changed |= split_level(data, 'l3', 'l3b')
    changed |= split_level(data, 'l6', 'l6b')

    if changed:
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        print("Updated blasnesmous.json successfully.")

if __name__ == '__main__':
    main()

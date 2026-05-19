import os
import json
import sys

def convert_mapfab_to_json(mapfab_path, json_path):
    print(f"Converting {mapfab_path} to {json_path}...")
    with open(mapfab_path, 'rb') as f:
        data = f.read()
    
    ptr = 0
    end = len(data)
    
    def get8(adjust=False):
        nonlocal ptr
        if ptr >= end:
            raise ValueError("Unexpected EOF")
        val = data[ptr]
        ptr += 1
        if adjust and val == 0:
            return 256
        return val
        
    def get16():
        lo = get8()
        hi = get8()
        return lo | (hi << 8)
        
    def get_str():
        chars = []
        while True:
            c = get8()
            if c == 0:
                break
            chars.append(chr(c))
        return "".join(chars)

    # Magic and Version
    if end - ptr < 8:
        raise ValueError("Invalid MapFab file: no magic number.")
    
    magic = data[ptr:ptr+7]
    if magic != b"MapFab\x00":
        raise ValueError("Incorrect magic number.")
    
    save_version = data[ptr+7]
    ptr += 8

    # Collision file path (discarded in JSON but present in binary)
    collisions_path = get_str()

    # CHR
    num_chr = get8(True)
    chrs = []
    for _ in range(num_chr):
        name = get_str()
        path = get_str()
        chrs.append({"name": name, "path": path})

    # Palettes
    num_palettes = get8(True)
    palette_data = []
    for _ in range(256 * 25):
        palette_data.append(get8())

    # Metatile Sets
    num_mt = get8(True)
    mt_sets = []
    for _ in range(num_mt):
        mt_name = get_str()
        chr_name = get_str()
        palette = get8()
        num = get8(True)
        
        tiles = [get8() for _ in range(1024)]
        attributes = [get8() for _ in range(256)]
        collisions = [get8() for _ in range(256)]
        
        mt_sets.append({
            "name": mt_name,
            "chr": chr_name,
            "palette": palette,
            "num": num,
            "tiles": tiles,
            "attributes": attributes,
            "collisions": collisions
        })

    # Object Classes
    num_oc = get8(True)
    object_classes = []
    ocs_fields = {}
    for _ in range(num_oc):
        name = get_str()
        get8() # R
        get8() # G
        get8() # B
        
        num_fields = get8()
        fields = []
        fields_info = []
        for _ in range(num_fields):
            f_name = get_str()
            f_type = get_str()
            fields.append({"name": f_name, "type": f_type})
            fields_info.append((f_name, f_type))
            
        object_classes.append({
            "name": name,
            "fields": fields
        })
        ocs_fields[name] = fields_info

    # Levels
    num_levels = get8(True)
    levels = []
    for _ in range(num_levels):
        name = get_str()
        macro = get_str()
        chr_name = get_str()
        palette = get8()
        metatile_set = get_str()
        w = get8(True)
        h = get8(True)
        
        tiles = [get8() for _ in range(w * h)]
        
        num_objects = get16()
        objects = []
        for _ in range(num_objects):
            obj_name = get_str()
            obj_oc = get_str()
            
            x_bytes = [get8(), get8()]
            x = x_bytes[0] | (x_bytes[1] << 8)
            if x >= 32768:
                x -= 65536
                
            y_bytes = [get8(), get8()]
            y = y_bytes[0] | (y_bytes[1] << 8)
            if y >= 32768:
                y -= 65536
                
            fields_data = {}
            if obj_oc in ocs_fields:
                for f_name, f_type in ocs_fields[obj_oc]:
                    fields_data[f_name] = get_str()
                
                objects.append({
                    "fields": fields_data,
                    "name": obj_name,
                    "object_class": obj_oc,
                    "x": x,
                    "y": y
                })
            
        levels.append({
            "chr": chr_name,
            "height": h,
            "macro": macro,
            "metatile_set": metatile_set,
            "name": name,
            "objects": objects,
            "palette": palette,
            "tiles": tiles,
            "width": w
        })

    json_data = {
        "version": save_version,
        "chr": chrs,
        "palettes": {
            "num": num_palettes,
            "data": palette_data
        },
        "metatile_sets": mt_sets,
        "object_classes": object_classes,
        "levels": levels
    }

    # Make sure parent directory of output exists
    os.makedirs(os.path.dirname(os.path.abspath(json_path)), exist_ok=True)
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=2)
    print(f"Successfully converted to {json_path}")

def main():
    mapfab_path = 'BlasNESmous.mapfab'
    json_path = 'blasnesmous.json'
    
    if not os.path.exists(mapfab_path):
        print(f"Error: {mapfab_path} does not exist!")
        sys.exit(1)
        
    convert_mapfab_to_json(mapfab_path, json_path)

if __name__ == '__main__':
    main()

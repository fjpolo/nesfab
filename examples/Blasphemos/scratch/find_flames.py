from PIL import Image

def find_flame_tiles(img_path):
    im = Image.open(img_path)
    im_rgb = im.convert('RGB')
    w, h = im.size
    flame_tiles = []
    
    # Let's search for warm colors (R > 200, G > 120, B < 100)
    for ty in range(0, h, 8):
        for tx in range(0, w, 8):
            has_flame_color = False
            for y in range(8):
                for x in range(8):
                    r, g, b = im_rgb.getpixel((tx + x, ty + y))
                    if r > 200 and g > 120 and b < 100:
                        has_flame_color = True
                        break
                if has_flame_color:
                    break
            if has_flame_color:
                tile_idx = (ty // 8) * (w // 8) + (tx // 8)
                flame_tiles.append(tile_idx)
    return flame_tiles

print("bg1 flame tiles:", find_flame_tiles('c:/Workspace/nesfab/nesfab/examples/Blasphemos/assets/bg1.png'))
print("bg2 flame tiles:", find_flame_tiles('c:/Workspace/nesfab/nesfab/examples/Blasphemos/assets/bg2.png'))

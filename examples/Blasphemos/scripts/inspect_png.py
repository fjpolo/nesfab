import os
from PIL import Image

assets_dir = 'c:/Workspace/nesfab/nesfab/examples/Blasphemos/assets'
for f in os.listdir(assets_dir):
    if f.endswith('.png'):
        try:
            im = Image.open(os.path.join(assets_dir, f))
            print(f"{f}: {im.size} - {im.mode}")
        except Exception as e:
            print(f"Error opening {f}: {e}")

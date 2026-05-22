import os
from PIL import Image

media_dir = r"C:\Users\polo\.gemini\antigravity\brain\0fbfe38a-f0ab-4aab-9a1f-9a2a210d8dcc"
files = [
    "media__1779374073793.png",
    "media__1779374099535.png",
    "media__1779374114769.png",
    "media__1779374144411.png",
    "media__1779374168774.png"
]

for f in files:
    path = os.path.join(media_dir, f)
    if os.path.exists(path):
        im = Image.open(path)
        print(f"{f}: size={im.size}, mode={im.mode}")
    else:
        print(f"Not found: {path}")

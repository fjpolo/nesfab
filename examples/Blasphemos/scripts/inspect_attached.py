import os
from PIL import Image

media_dir = r"C:\Users\polo\.gemini\antigravity\brain\0fbfe38a-f0ab-4aab-9a1f-9a2a210d8dcc"
files = [
    "media__1779373733930.png",
    "media__1779373763356.png",
    "media__1779373779346.png",
    "media__1779373793162.png",
    "media__1779373831792.png"
]

for f in files:
    path = os.path.join(media_dir, f)
    if os.path.exists(path):
        im = Image.open(path)
        print(f"{f}: size={im.size}, mode={im.mode}")
    else:
        print(f"Not found: {path}")

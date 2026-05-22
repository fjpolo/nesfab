import os
from PIL import Image

path = r"C:\Users\polo\.gemini\antigravity\brain\0fbfe38a-f0ab-4aab-9a1f-9a2a210d8dcc\media__1779373733930.png"
if os.path.exists(path):
    img = Image.open(path)
    print("Original size:", img.size)
    print("Original mode:", img.mode)
else:
    print("Path does not exist!")

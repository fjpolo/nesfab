from PIL import Image
import numpy as np

img = Image.open('assets/silent_sorrow_0.png')
print("Size:", img.size)
print("Mode:", img.mode)
print("Palette:", img.getpalette()[:12])
# Print pixel representation as 0, 1, 2, 3
arr = np.array(img)
unique, counts = np.unique(arr, return_counts=True)
print("Unique pixels:", dict(zip(unique, counts)))

from PIL import Image
import numpy as np

img = Image.open('assets/silent_sorrow_0.png')
arr = np.array(img)
h, w = arr.shape

# Let's print it in blocks of 2x2 or 4x4, or line by line
for y in range(0, h, 2):
    line = ""
    for x in range(0, w, 2):
        val = arr[y, x]
        if val == 3:
            line += "#"
        else:
            line += " "
    # Skip completely empty lines to make it concise
    if line.strip():
        print(line)

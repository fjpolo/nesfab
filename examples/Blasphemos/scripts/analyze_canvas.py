from PIL import Image

im = Image.open('assets/blasphemous-dead-1920x1080.png')
rgb = im.convert('RGB')
w, h = im.size

# Find bounding box of non-black pixels
min_x, min_y = w, h
max_x, max_y = 0, 0

for y in range(h):
    for x in range(w):
        r, g, b = rgb.getpixel((x, y))
        if r > 5 or g > 5 or b > 5:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)

print(f"Non-black bbox: x1={min_x}, y1={min_y}, x2={max_x}, y2={max_y}")

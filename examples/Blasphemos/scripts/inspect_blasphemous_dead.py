from PIL import Image

try:
    im = Image.open('assets/blasphemous-dead-1920x1080.png')
    print("Format:", im.format)
    print("Size:", im.size)
    print("Mode:", im.mode)
except Exception as e:
    print("Error:", e)

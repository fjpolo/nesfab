from PIL import Image

try:
    c = Image.open('assets/Crucified.png')
    print("Crucified format:", c.format, "size:", c.size, "mode:", c.mode)
    
    d = Image.open('assets/Damned_orig.png')
    print("Damned format:", d.format, "size:", d.size, "mode:", d.mode)
except Exception as e:
    print("Error:", e)

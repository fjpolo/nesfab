import os
from PIL import Image

# Paths
orig_path = r"c:\Workspace\nesfab\nesfab\examples\Blasphemos\assets\bg1.orig.png"
new_path = r"C:\Users\polo\.gemini\antigravity\brain\b7f85d61-6d5b-4b98-bc52-dea98f882677\bg1_no_bricks_1779382214897.png"
out_path = r"c:\Workspace\nesfab\nesfab\examples\Blasphemos\assets\bg1.png"

# Load original palette
orig_img = Image.open(orig_path)
if orig_img.mode != 'P':
    orig_img = orig_img.convert('P')
orig_palette = orig_img.getpalette()

# Create a palette image for quantization
palette_img = Image.new('P', (1, 1))
palette_img.putpalette(orig_palette)

# Load new image and quantize to original palette
new_img = Image.open(new_path).convert('RGB')
quantized = new_img.quantize(palette=palette_img)

# Save result as PNG (no alpha, no interlace)
quantized.save(out_path, format='PNG')
print('Palette converted background saved to', out_path)

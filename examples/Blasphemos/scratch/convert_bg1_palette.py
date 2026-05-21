import os
from PIL import Image

# Paths
orig_path = r"c:\Workspace\nesfab\nesfab\examples\Blasphemos\assets\bg1.orig.png"
new_path = r"C:\Users\polo\.gemini\antigravity\brain\b7f85d61-6d5b-4b98-bc52-dea98f882677\bg1_no_bricks_1779382214897.png"
out_path = r"c:\Workspace\nesfab\nesfab\examples\Blasphemos\assets\bg1.png"

# Load original to get palette (assume it is palette mode or RGB)
orig = Image.open(orig_path)
# Ensure we have a palette list of RGB tuples
if orig.mode != 'P':
    # Convert to palette mode using adaptive palette (should match original colors)
    orig = orig.convert('P')
palette = orig.getpalette()  # flat list of 768 values (256*3)

# Load new image
new_img = Image.open(new_path).convert('RGB')
# Convert new image to use original palette via quantize
new_indexed = new_img.quantize(palette=Image.frombytes('P', (16,16), bytes(palette)))
# Save as PNG, no alpha, no interlace
new_indexed.save(out_path, format='PNG')
print('Palette‑converted background saved to', out_path)

import os
from PIL import Image

# Source: brick‑free background generated earlier
src_path = r"C:\Users\polo\.gemini\antigravity\brain\b7f85d61-6d5b-4b98-bc52-dea98f882677\bg1_no_bricks_1779382214897.png"
# Destination used by the project
dst_path = r"c:\Workspace\nesfab\nesfab\examples\Blasphemos\assets\bg1.png"

if not os.path.isfile(src_path):
    raise FileNotFoundError(f"Source image not found: {src_path}")

# Load, ensure RGB (no alpha) and save as standard PNG (no interlace)
im = Image.open(src_path).convert('RGB')
im.save(dst_path, format='PNG')
print('Clean PNG saved to', dst_path)

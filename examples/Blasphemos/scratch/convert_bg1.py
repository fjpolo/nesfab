from PIL import Image
import os

# Path to the generated artifact (relative to workspace)
src = r"C:\Users\polo\.gemini\antigravity\brain\b7f85d61-6d5b-4b98-bc52-dea98f882677\bg1_fixed_1779381941627.png"
# Destination in the project assets folder
dst = r"c:\Workspace\nesfab\nesfab\examples\Blasphemos\assets\bg1.png"

if not os.path.isfile(src):
    raise FileNotFoundError(f"Source image not found: {src}")

im = Image.open(src)
# Ensure mode is RGB (no alpha) and no interlace
im = im.convert('RGB')
# Save with PNG defaults (no interlace)
im.save(dst, format='PNG')
print(f"Re‑saved PNG to {dst}")

import os
import shutil

src_usage = "chr_usage.png"
src_sheet = "chr_sheet.png"

dest_dir = r"C:\Users\polo\.gemini\antigravity\brain\87349f45-1792-49e4-a809-dfc61d163151"

if os.path.exists(src_usage):
    shutil.copy(src_usage, os.path.join(dest_dir, "chr_usage.png"))
    print("Copied chr_usage.png to artifacts.")
else:
    print("chr_usage.png not found.")

if os.path.exists(src_sheet):
    shutil.copy(src_sheet, os.path.join(dest_dir, "chr_sheet.png"))
    print("Copied chr_sheet.png to artifacts.")
else:
    print("chr_sheet.png not found.")

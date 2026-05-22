import os
import re

def main():
    header_path = "scratch/Byteletter/Source/Byteletter.h"
    with open(header_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    char_count = 0
    for i, line in enumerate(lines):
        if "0x" in line:
            hex_vals = re.findall(r"0x[0-9a-fA-F]+", line)
            print(f"Line {i+1} ({line.strip()}): found {len(hex_vals)} bytes")
            char_count += 1
            
    print(f"Total lines with 0x: {char_count}")

if __name__ == "__main__":
    main()

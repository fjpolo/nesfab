try:
    import matplotlib.pyplot as plt
    import numpy as np
except ImportError:
    import sys
    print("Warning: matplotlib or numpy not found. Analysis skipped.")
    sys.exit(0)
import os
import re

def analyze_nes_memory(labels_file="BlasNESmous.mlb"):
    # 2KB Internal RAM ($0000 - $07FF)
    ram_size = 2048
    ram_map = np.zeros(ram_size)
    
    # 1. --- DATA PARSING ---
    # Static system allocations
    allocations = [
        (0x0000, 0x100, "Zero Page"),
        (0x0100, 0x100, "Stack"),
    ]

    # Map static allocations
    for start, size, label in allocations:
        ram_map[start:start+size] = 0.5 # Partial usage for system areas

    if labels_file and os.path.exists(labels_file):
        with open(labels_file, 'r') as f:
            for line in f:
                # Parse MLB format: "R:ADDR:NAME@INDEX:"
                # Example: "R:0400:oam@0:"
                match = re.match(r'^R:([0-9A-Fa-f]+):', line)
                if match:
                    try:
                        addr = int(match.group(1), 16)
                        if addr < ram_size:
                            ram_map[addr] = 1.0 # Full usage for variables
                    except:
                        continue

    # 2. --- VISUALIZATION ---
    # 32 rows of 64 bytes = 2048 bytes
    grid_map = ram_map.reshape((32, 64))

    plt.figure(figsize=(14, 10))
    # Use a color map where 0 is white, 0.5 is light blue, 1 is dark blue
    plt.imshow(grid_map, cmap='Blues', aspect='equal', interpolation='nearest', vmin=0, vmax=1)
    
    # Add grid lines every 16 bytes (columns) and every 256 bytes (rows = 4 rows)
    plt.xticks(np.arange(0, 64, 16), ["$00", "$10", "$20", "$30"])
    plt.yticks(np.arange(0, 32, 4), ["$000", "$100", "$200", "$300", "$400", "$500", "$600", "$700"])
    
    plt.grid(color='gray', linestyle='-', linewidth=0.2, which='major')

    plt.title("NES RAM Usage Heatmap ($0000 - $07FF)")
    plt.xlabel("Columns (Byte Offset in Page)")
    plt.ylabel("Rows (Page Address)")

    # Add a legend-like info
    plt.text(65, 2, "Dark Blue: Variable", color='darkblue', fontweight='bold')
    plt.text(65, 4, "Light Blue: System Area", color='skyblue', fontweight='bold')
    plt.text(65, 6, "White: Free RAM", color='gray')

    # 3. --- SAVE ---
    output_path = "memory_usage.png"
    plt.savefig(output_path, bbox_inches='tight')
    print(f"Success! Analysis saved to: {os.getcwd()}/{output_path}")

if __name__ == "__main__":
    analyze_nes_memory()
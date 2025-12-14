import matplotlib.pyplot as plt
import numpy as np
import os

def analyze_nes_memory(labels_file=None):
    # 2KB Internal RAM ($0000 - $07FF)
    ram_size = 2048
    ram_map = np.zeros(ram_size)
    
    # 1. --- DATA PARSING ---
    # Replace this list with actual logic to parse your nesfab output
    allocations = [
        (0x0000, 0x100, "Zero Page"),
        (0x0100, 0x100, "Stack"),
        (0x0200, 0x100, "OAM (Sprites)"),
    ]

    if labels_file and os.path.exists(labels_file):
        with open(labels_file, 'r') as f:
            for line in f:
                # Basic parsing logic for common NES label formats
                # Example line: "player_pos = $0300"
                if "=" in line and "$" in line:
                    try:
                        parts = line.split('=')
                        addr = int(parts[1].strip().replace('$', ''), 16)
                        if addr < ram_size:
                            ram_map[addr] = 1
                    except:
                        continue

    # 2. --- VISUALIZATION ---
    # Map allocations to the array
    for start, size, label in allocations:
        ram_map[start:start+size] = 1

    grid_map = ram_map.reshape((32, 64))

    plt.figure(figsize=(12, 8))
    plt.imshow(grid_map, cmap='Blues', aspect='equal', interpolation='nearest')
    
    # Add grid lines for clarity
    plt.xticks(np.arange(-.5, 64, 4), [])
    plt.yticks(np.arange(-.5, 32, 4), [])
    plt.grid(color='white', linestyle='-', linewidth=0.5)

    plt.title("NES RAM Usage Heatmap ($0000 - $07FF)")
    plt.xlabel("Columns (Bytes 0-63)")
    plt.ylabel("Rows (Page Offset)")

    # 3. --- SAVE INSTEAD OF SHOW ---
    output_path = "memory_usage.png"
    plt.savefig(output_path)
    print(f"Success! Analysis saved to: {os.getcwd()}/{output_path}")

if __name__ == "__main__":
    analyze_nes_memory()
import os
import re

def format_ranges(addresses):
    if not addresses:
        return ""
    addrs = sorted(list(set(addresses)))
    ranges = []
    start = addrs[0]
    prev = addrs[0]
    for i in range(1, len(addrs)):
        if addrs[i] == prev + 1:
            prev = addrs[i]
        else:
            ranges.append(f"${start:04X}-${prev:04X}" if start != prev else f"${start:04X}")
            start = addrs[i]
            prev = addrs[i]
    ranges.append(f"${start:04X}-${prev:04X}" if start != prev else f"${start:04X}")
    return ", ".join(ranges)

def analyze_nes_memory(labels_file="BlasNESmous.mlb"):
    # 2KB Internal RAM ($0000 - $07FF)
    ram_size = 2048
    ram_usage_map = [0.0] * ram_size
    
    # 1. --- DATA PARSING ---
    vars_info = {} # name -> [addresses]
    
    # Static system allocations
    allocations = [
        (0x0000, 0x100, "Zero Page"),
        (0x0100, 0x100, "Stack"),
    ]

    # Map static allocations
    for start, size, label in allocations:
        for i in range(start, start + size):
            if i < ram_size:
                ram_usage_map[i] = 0.5 # Partial usage for system areas

    if labels_file and os.path.exists(labels_file):
        with open(labels_file, 'r') as f:
            for line in f:
                # Parse MLB format: "R:ADDR:NAME@INDEX:"
                # Example: "R:0400:oam@0:"
                match = re.match(r'^R:([0-9A-Fa-f]+):([^@:]+)@(\d+):', line)
                if match:
                    try:
                        addr = int(match.group(1), 16)
                        name = match.group(2)
                        if addr < ram_size:
                            ram_usage_map[addr] = 1.0 # Full usage for variables
                            if name not in vars_info:
                                vars_info[name] = []
                            vars_info[name].append(addr)
                    except:
                        continue

    # 2. --- SAVE VARIABLE LIST ---
    list_path = "analysis/ram_variables.txt"
    with open(list_path, "w") as f:
        f.write(f"{'Variable Name':<40} {'Size':<8} {'Address Range(s)'}\n")
        f.write("=" * 80 + "\n")
        
        # Sort by first address
        sorted_vars = sorted(vars_info.items(), key=lambda x: min(x[1]))
        
        for name, addrs in sorted_vars:
            size = len(addrs)
            addr_str = format_ranges(addrs)
            f.write(f"{name:<40} {size:<8} {addr_str}\n")
        
        # Summary
        used_bytes = sum(1 for x in ram_usage_map if x == 1.0)
        sys_bytes = sum(1 for x in ram_usage_map if x == 0.5)
        f.write("\n" + "=" * 80 + "\n")
        f.write(f"Variable Bytes: {used_bytes}\n")
        f.write(f"System Bytes:   {sys_bytes}\n")
        f.write(f"Free Bytes:     {ram_size - used_bytes - sys_bytes}\n")
        f.write(f"Total Usage:    {used_bytes + sys_bytes}/{ram_size} bytes ({(used_bytes + sys_bytes)/ram_size:.1%})\n")
    
    print(f"Success! Variable list saved to: {os.path.join(os.getcwd(), list_path)}")
    print(f"RAM Usage: {used_bytes + sys_bytes}/{ram_size} bytes ({(used_bytes + sys_bytes)/ram_size:.1%})")

    # 3. --- VISUALIZATION ---
    try:
        import matplotlib.pyplot as plt
        import numpy as np
        
        ram_map = np.array(ram_usage_map)
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

        # SAVE
        output_path = "analysis/memory_usage.png"
        plt.savefig(output_path, bbox_inches='tight')
        print(f"Success! Heatmap saved to: {os.path.join(os.getcwd(), output_path)}")
        
    except ImportError:
        print("Warning: matplotlib or numpy not found. Heatmap skipped.")

if __name__ == "__main__":
    analyze_nes_memory()
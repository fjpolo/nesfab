import os
import sys

def analyze_prg_banks():
    rom_path = "BlasNESmous.nes"
    if not os.path.exists(rom_path):
        print(f"Error: ROM file '{rom_path}' not found.")
        return
        
    print(f"Analyzing PRG-ROM banks in '{rom_path}'...")
    
    with open(rom_path, "rb") as f:
        header = f.read(16)
        
        if header[:4] != b'NES\x1a':
            print("Error: Invalid iNES header.")
            return
            
        # Parse iNES header details
        prg_banks_16k = header[4]
        chr_banks_8k = header[5]
        
        prg_size = prg_banks_16k * 16384
        chr_size = chr_banks_8k * 8192
        
        # Seek past the header to read PRG-ROM
        f.seek(16)
        prg_data = f.read(prg_size)
        
    # MMC3 maps PRG-ROM in 8KB physical banks (8192 bytes)
    bank_size = 8192
    num_8k_banks = prg_size // bank_size
    
    print(f"PRG-ROM Size: {prg_size // 1024} KB ({num_8k_banks} banks of 8KB)")
    print(f"CHR-ROM Size: {chr_size // 1024} KB ({chr_banks_8k} banks of 8KB)")
    print("-" * 95)
    print(f"{'Bank':<8} | {'Address Range':<15} | {'Usage Bar':<32} | {'Used Bytes':<12} | {'Free Bytes':<12} | {'Capacity'}")
    print("-" * 95)
    
    total_used = 0
    total_free = 0
    
    for i in range(num_8k_banks):
        bank_bytes = prg_data[i * bank_size : (i + 1) * bank_size]
        
        # Scan backwards to find the last active byte.
        # Padding in NES compiles is typically b'\x00' or b'\xFF'.
        free_bytes = 0
        for b in reversed(bank_bytes):
            if b == 0x00 or b == 0xFF:
                free_bytes += 1
            else:
                break
                
        # If the bank is completely empty
        if free_bytes == bank_size:
            used_bytes = 0
        else:
            used_bytes = bank_size - free_bytes
            
        total_used += used_bytes
        total_free += free_bytes
        
        used_pct = (used_bytes / bank_size)
        
        # Create usage bar
        bar_chars = int(used_pct * 30)
        usage_bar = "[" + "=" * bar_chars + " " * (30 - bar_chars) + "]"
        
        # Capacity label with alerts
        capacity_str = f"{used_pct:6.1%}"
        if used_pct > 0.98:
            capacity_str += " [!! CRITICAL]"
        elif used_pct > 0.90:
            capacity_str += " [! NEAR FULL]"
            
        # Address mapping (typically maps to $8000-$9FFF, $A000-$BFFF, $C000-$DFFF, or $E000-$FFFF)
        bank_range = f"Bank {i:02d}"
        
        print(f"{bank_range:<8} | {i*8:03d}K - {(i+1)*8:03d}K | {usage_bar} | {used_bytes:<12} | {free_bytes:<12} | {capacity_str}")
        
    print("-" * 95)
    overall_used_pct = total_used / prg_size
    print(f"TOTALS   | PRG-ROM Capacity | Used: {total_used:<6} bytes | Free: {total_free:<6} bytes | Overall: {overall_used_pct:.1%}")
    print("-" * 95)

if __name__ == "__main__":
    analyze_prg_banks()

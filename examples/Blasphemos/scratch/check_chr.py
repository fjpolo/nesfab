import os

rom_path = "BlasNESmous.nes"
if os.path.exists(rom_path):
    with open(rom_path, "rb") as f:
        f.seek(16 + 524288) # Skip header + PRG-ROM
        chr_data = f.read(262144)
        print(f"Read CHR-ROM size: {len(chr_data)} bytes")
        
        non_zero_total = sum(1 for b in chr_data if b != 0)
        print(f"Total non-zero bytes: {non_zero_total} ({non_zero_total / len(chr_data):.1%})")
        
        # Analyze by 8KB banks
        print("\nBank Analysis:")
        for bank_idx in range(32):
            bank_start = bank_idx * 8192
            bank_end = bank_start + 8192
            bank_bytes = chr_data[bank_start:bank_end]
            non_zero_bank = sum(1 for b in bank_bytes if b != 0)
            print(f"  Bank {bank_idx:2d}: {non_zero_bank:4d} / 8192 bytes non-zero ({non_zero_bank / 8192:.1%})")
else:
    print("ROM file not found.")

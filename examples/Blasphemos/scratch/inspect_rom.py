import os

rom_path = "BlasNESmous.nes"
if os.path.exists(rom_path):
    with open(rom_path, "rb") as f:
        header = f.read(16)
        print("Header bytes:", [f"${b:02X}" for b in header])
        prg_banks = header[4]
        chr_banks = header[5]
        print(f"PRG-ROM banks (16KB): {prg_banks} ({prg_banks * 16384} bytes)")
        print(f"CHR-ROM banks (8KB): {chr_banks} ({chr_banks * 8192} bytes)")
        f.seek(0, 2)
        total_size = f.tell()
        print(f"Total file size: {total_size} bytes")
        expected_size = 16 + prg_banks * 16384 + chr_banks * 8192
        print(f"Expected file size from header: {expected_size} bytes")
        print(f"Difference: {total_size - expected_size} bytes")
else:
    print("ROM file not found.")

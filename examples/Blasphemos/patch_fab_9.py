import sys

def patch():
    with open('src/intro_silent_sorrow.fab', 'r') as f:
        lines = f.readlines()
        
    for i, line in enumerate(lines):
        if 'file(fmt, "../assets/silent_sorrow_9.png")' in line:
            lines[i] = line.replace('file(fmt, "../assets/silent_sorrow_9.png")', 'file(chr, "../assets/silent_sorrow_9_padded.png")')
            
    # Insert SORROW_NAM_9
    insert_idx = 0
    for i, line in enumerate(lines):
        if line.startswith('fn sorrow_setup_nametable'):
            insert_idx = i
            break
            
    lines.insert(insert_idx, 'ct U[960] SORROW_NAM_9 = file(nam, "../assets/silent_sorrow_9_padded.png")\n\n')
    
    # Add current_frame == 9 logic
    for i, line in enumerate(lines):
        if line.strip() == 'else if current_frame == 8':
            # Skip past current_frame == 8 block
            # It's 12 lines long
            block = [
                '    else if current_frame == 9\n',
                '        {PPUSTATUS}()\n',
                '        {PPUADDR}($20)\n',
                '        {PPUADDR}($00)\n',
                '        for U i = 0; i < 960; i += 1\n',
                '            {PPUDATA}(SORROW_NAM_9[i])\n'
            ]
            lines = lines[:i+12] + block + lines[i+12:]
            break

    with open('src/intro_silent_sorrow.fab', 'w') as f:
        f.writelines(lines)
    print("Patched successfully.")

if __name__ == '__main__':
    patch()

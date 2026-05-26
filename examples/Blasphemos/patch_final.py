import sys

def patch():
    with open('extracted_nam_9.txt', 'r') as f:
        nam_lines = f.read().strip().split('\n')
        
    with open('src/intro_silent_sorrow.fab', 'r') as f:
        lines = f.readlines()
        
    # Replace file(fmt, "../assets/silent_sorrow_9_padded.png")
    for i, line in enumerate(lines):
        if 'file(fmt, "../assets/silent_sorrow_9_padded.png")' in line:
            lines[i] = line.replace('file(fmt, "../assets/silent_sorrow_9_padded.png")', 'file(raw, "../assets/silent_sorrow_9.chr")')
            
    # Find SORROW_NAM_9 definition
    delete_start = 0
    delete_end = 0
    for i, line in enumerate(lines):
        if line.startswith('ct U[960] SORROW_NAM_9'):
            delete_start = i
            delete_end = i
            break
            
    # Replace it with our PART_0...3
    lines = lines[:delete_start] + [l + '\n' for l in nam_lines] + lines[delete_end+1:]
    
    # Update the loop in current_frame == 9
    for i, line in enumerate(lines):
        if line.strip() == 'else if current_frame == 9':
            # It currently has:
            # {PPUSTATUS}()
            # {PPUADDR}($20)
            # {PPUADDR}($00)
            # for U i = 0; i < 960; i += 1
            #     {PPUDATA}(SORROW_NAM_9[i])
            block = [
                '    else if current_frame == 9\n',
                '        {PPUSTATUS}()\n',
                '        {PPUADDR}($20)\n',
                '        {PPUADDR}($00)\n',
                '        for U i = 0; i < 240; i += 1\n',
                '            {PPUDATA}(SORROW_NAM_9_PART_0[i])\n',
                '        for U i = 0; i < 240; i += 1\n',
                '            {PPUDATA}(SORROW_NAM_9_PART_1[i])\n',
                '        for U i = 0; i < 240; i += 1\n',
                '            {PPUDATA}(SORROW_NAM_9_PART_2[i])\n',
                '        for U i = 0; i < 240; i += 1\n',
                '            {PPUDATA}(SORROW_NAM_9_PART_3[i])\n'
            ]
            lines = lines[:i] + block + lines[i+6:]
            break

    with open('src/intro_silent_sorrow.fab', 'w') as f:
        f.writelines(lines)
    print("Patched successfully.")

if __name__ == '__main__':
    patch()

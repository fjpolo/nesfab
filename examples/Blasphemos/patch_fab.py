import sys

def patch():
    with open('extracted_nam.txt', 'r') as f:
        nam_lines = f.read().strip().split('\n')
        
    with open('src/intro_silent_sorrow.fab', 'r') as f:
        lines = f.readlines()
        
    start_idx = 0
    end_idx = 0
    for i, line in enumerate(lines):
        if line.startswith('ct U[240] SORROW_NAM_8_PART_0'):
            start_idx = i
        elif line.startswith('ct U[240] SORROW_NAM_8_PART_3'):
            end_idx = i
            break
            
    if start_idx > 0 and end_idx >= start_idx:
        new_lines = lines[:start_idx] + [l + '\n' for l in nam_lines] + lines[end_idx+1:]
        
        with open('src/intro_silent_sorrow.fab', 'w') as f:
            f.writelines(new_lines)
        print("Patched successfully.")
    else:
        print("Could not find SORROW_NAM_8_PART_0...3 to replace.")

if __name__ == '__main__':
    patch()

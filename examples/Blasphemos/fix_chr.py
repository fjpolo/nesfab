import sys
import os

def fix_chr():
    path = r"C:\Workspace\nesfab\nesfab\examples\Blasphemos\assets\silent_sorrow_9.chr"
    with open(path, 'rb') as f:
        data = f.read(4096)
        
    with open(path, 'wb') as f:
        f.write(data)
    print("Truncated to 4KB.")

if __name__ == '__main__':
    fix_chr()

def read_nam(filepath):
    with open(filepath, 'rb') as f:
        data = f.read(960) # Only read the 32x30 tiles
        
    # Find bounding box
    min_x, max_x = 32, 0
    min_y, max_y = 30, 0
    for y in range(30):
        for x in range(32):
            if data[y*32 + x] != 0:
                min_x = min(min_x, x)
                max_x = max(max_x, x)
                min_y = min(min_y, y)
                max_y = max(max_y, y)
                
    print(f"Bounding box: X: {min_x}-{max_x}, Y: {min_y}-{max_y}")
    
    # Extract
    extracted = []
    # If the user drew it at a specific position, extract exactly that 20x12 box.
    # Let's just extract the exact bounds
    for y in range(min_y, min_y + 12):
        for x in range(min_x, min_x + 20):
            if y < 30 and x < 32:
                extracted.append(data[y*32 + x])
            else:
                extracted.append(0)
                
    # Format as NESFab array
    chunks = [extracted[i:i+240] for i in range(0, len(extracted), 240)]
    for i, chunk in enumerate(chunks):
        print(f"ct U[240] SORROW_NAM_8 = U[240]({', '.join(map(str, chunk))})")

if __name__ == '__main__':
    read_nam(r"C:\Workspace\nesfab\nesfab\examples\Blasphemos\assets\TitleScreen.nam")

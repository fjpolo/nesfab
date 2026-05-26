def read_nam(filepath, outpath):
    with open(filepath, 'rb') as f:
        data = f.read(960) # Only read the 32x30 tiles
        
    extracted = list(data)
    chunks = [extracted[i:i+240] for i in range(0, 960, 240)]
    
    with open(outpath, 'w') as out:
        for i, chunk in enumerate(chunks):
            out.write(f"ct U[240] SORROW_NAM_8_PART_{i} = U[240]({', '.join(map(str, chunk))})\n")

if __name__ == '__main__':
    read_nam(r"C:\Workspace\nesfab\nesfab\examples\Blasphemos\assets\TitleScreen.nam", r"C:\Workspace\nesfab\nesfab\examples\Blasphemos\extracted_nam.txt")

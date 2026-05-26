from PIL import Image

def main():
    img = Image.open(r"C:\Workspace\nesfab\nesfab\examples\Blasphemos\assets\silent_sorrow_9.png").convert("RGB")
    colors = [c[1] for c in img.getcolors(maxcolors=256)]
    
    # Sort colors by luminance
    def luminance(c):
        return 0.299*c[0] + 0.587*c[1] + 0.114*c[2]
        
    colors.sort(key=luminance)
    print("Colors sorted by luminance:")
    for c in colors:
        print(c)

if __name__ == "__main__":
    main()

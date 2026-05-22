import os
import urllib.request
import zipfile

def main():
    url = "https://dl.damieng.com/fonts/zx-origins/Byteletter.zip"
    dest_zip = "scratch/Byteletter.zip"
    dest_dir = "scratch/Byteletter"
    
    os.makedirs("scratch", exist_ok=True)
    
    print(f"Downloading {url}...")
    try:
        # Set a user-agent just in case
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        with urllib.request.urlopen(req) as response, open(dest_zip, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
        print("Download complete.")
        
        print(f"Extracting to {dest_dir}...")
        with zipfile.ZipFile(dest_zip, 'r') as zip_ref:
            zip_ref.extractall(dest_dir)
        print("Extraction complete.")
        
        # List files in extracted directory
        print("Files extracted:")
        for root, dirs, files in os.walk(dest_dir):
            for file in files:
                print(os.path.join(root, file))
                
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()

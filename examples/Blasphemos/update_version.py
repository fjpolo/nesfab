import subprocess
import re
import os

def get_git_commit_count():
    try:
        result = subprocess.run(['git', 'rev-list', '--count', 'HEAD'], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except Exception as e:
        print("Could not get git commit count:", e)
        return "0"

def main():
    commit_count = get_git_commit_count()
    version_string = f"v0.0.1.{commit_count}"
    
    with open("VERSION", "w") as f:
        f.write(version_string)
        
    print(f"Version updated to {version_string}")

    files_to_update = ["story_screen.fab", "start_screen.fab"]
    
    for filename in files_to_update:
        if os.path.exists(filename):
            with open(filename, "r") as f:
                content = f.read()
                
            # Replace Blasphemous v... with Blasphemous version_string
            new_content = re.sub(r'Blasphemous v[0-9\.]+', f'Blasphemous {version_string}', content)
            
            if new_content != content:
                with open(filename, "w") as f:
                    f.write(new_content)
                print(f"Updated version in {filename}")

if __name__ == "__main__":
    main()

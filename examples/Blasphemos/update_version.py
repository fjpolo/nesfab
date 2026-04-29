import subprocess
import re
import os
import sys
from datetime import datetime

def get_git_commit_count():
    try:
        result = subprocess.run(['git', 'rev-list', '--count', 'HEAD'], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except Exception as e:
        print("Could not get git commit count:", e)
        return "0"

def get_last_commit_message():
    try:
        result = subprocess.run(['git', 'log', '-1', '--pretty=%B'], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except Exception as e:
        print("Could not get last commit message:", e)
        return "Manual update"

def update_changelog(version, message):
    changelog_path = "CHANGELOG.md"
    if not os.path.exists(changelog_path):
        print("CHANGELOG.md not found.")
        return

    date_str = datetime.now().strftime("%d.%m.%Y")
    new_entry = f"## [{date_str}] - {version}\n- {message}\n\n"

    # Explicitly use utf-8 encoding to handle emojis and special characters
    with open(changelog_path, "r", encoding='utf-8') as f:
        lines = f.readlines()

    # Find the line "# Changes"
    insert_pos = -1
    for i, line in enumerate(lines):
        if line.strip() == "# Changes":
            insert_pos = i + 1
            break

    if insert_pos != -1:
        lines.insert(insert_pos, "\n" + new_entry)
        with open(changelog_path, "w", encoding='utf-8') as f:
            f.writelines(lines)
        print(f"Updated CHANGELOG.md with version {version}")
    else:
        print("Could not find '# Changes' section in CHANGELOG.md")

def main():
    commit_count = get_git_commit_count()
    version_string = f"v0.0.1.{commit_count}"
    
    with open("VERSION", "w", encoding='utf-8') as f:
        f.write(version_string)
        
    print(f"Version updated to {version_string}")

    # Handle commit message for changelog
    if len(sys.argv) > 1:
        commit_message = sys.argv[1]
    else:
        commit_message = get_last_commit_message()

    update_changelog(version_string, commit_message)

    files_to_update = ["story_screen.fab", "start_screen.fab"]
    
    for filename in files_to_update:
        if os.path.exists(filename):
            with open(filename, "r", encoding='utf-8') as f:
                content = f.read()
                
            # Replace Blasphemous v... with Blasphemous version_string
            new_content = re.sub(r'Blasphemous v[0-9\.]+', f'Blasphemous {version_string}', content)
            
            if new_content != content:
                with open(filename, "w", encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated version in {filename}")

if __name__ == "__main__":
    main()

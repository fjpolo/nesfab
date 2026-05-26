import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: python set_build_flag.py [dev|release]")
        sys.exit(1)
        
    mode = sys.argv[1].lower()
    is_dev = "true" if mode == "dev" else "false"
    
    content = f"// Auto-generated build flag\nct Bool IS_DEV_MODE = {is_dev}\n"
    
    os.makedirs("src", exist_ok=True)
    with open("src/build_flags.fab", "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Set IS_DEV_MODE to {is_dev}")

if __name__ == "__main__":
    main()

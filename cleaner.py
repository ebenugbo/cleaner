import os
import shutil
import pathlib

# Folders to clean - safe to delete
TEMP_PATHS = [
    os.path.join(os.environ.get('TEMP', ''), ''),  # Windows temp
    os.path.join(os.environ.get('LOCALAPPDATA', ''), 'Temp'),
    "./__pycache__",
    "./.pytest_cache"
]

def get_size(path):
    total = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            try:
                fp = os.path.join(dirpath, f)
                total += os.path.getsize(fp)
            except:
                pass
    return total

def clean_folder(path):
    if not os.path.exists(path):
        print(f"Skip (not found): {path}")
        return 0
    
    size_before = get_size(path)
    deleted = 0
    
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)
                deleted += 1
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
                deleted += 1
        except Exception as e:
            print(f"Could not delete {item_path}: {e}")
            
    size_mb = size_before / (1024*1024)
    print(f"Cleaned {path} - freed {size_mb:.2f} MB ({deleted} files)")
    return size_mb

def main():
    print("=== PYTHON SYSTEM CLEANER ===")
    print("1. Clean Windows Temp")
    print("2. Clean current project (__pycache__, .pycache)")
    print("3. Find large files > 100MB in Downloads")
    print("4. Full Clean (1+2)")
    
    choice = input("Choose: ")
    
    if choice in ["1","4"]:
        for p in TEMP_PATHS[:2]:
            clean_folder(p)
    
    if choice in ["2","4"]:
        # clean all __pycache__ in current folder
        for p in pathlib.Path(".").rglob("__pycache__"):
            clean_folder(str(p))
    
    if choice == "3":
        downloads = os.path.join(os.path.expanduser("~"), "Downloads")
        print(f"Scanning {downloads}...")
        for dirpath, _, files in os.walk(downloads):
            for f in files:
                fp = os.path.join(dirpath, f)
                try:
                    if os.path.getsize(fp) > 100*1024*1024:
                        print(f"LARGE: {os.path.getsize(fp)/(1024*1024):.0f}MB - {fp}")
                except:
                    pass
    print("\nDone!")

if __name__ == "__main__":
    main()

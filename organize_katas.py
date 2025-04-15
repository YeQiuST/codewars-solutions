import os
import shutil
import re

SOURCE_DIR = "./raw_katas"
DEST_DIR = "./"

def extract_kyu_from_file(filename):
    match = re.search(r'(\d)kyu', filename.lower())
    return f"{match.group(1)}kyu" if match else None

def organize_katas():
    for filename in os.listdir(SOURCE_DIR):
        if filename.endswith(".py"):
            kyu = extract_kyu_from_file(filename)
            if kyu:
                target_folder = os.path.join(DEST_DIR, kyu)
                os.makedirs(target_folder, exist_ok=True)
                src_path = os.path.join(SOURCE_DIR, filename)
                dst_path = os.path.join(target_folder, filename)
                shutil.move(src_path, dst_path)
                print(f"✅ {filename} → {kyu}/")

if __name__ == "__main__":
    organize_katas()

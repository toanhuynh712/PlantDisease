import os
import hashlib
from PIL import Image

valid_ext = ('.jpg', '.jpeg', '.png')

def count_images(folder):
    count = 0
    for _, _, files in os.walk(folder):
        count += len(files)
    return count

def clean_data(folder):
    hashes = {}

    removed_corrupt = 0
    removed_dup = 0
    removed_format = 0

    total_before = count_images(folder)

    for root, _, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)

            # ❌ sai format
            if not file.lower().endswith(valid_ext):
                os.remove(path)
                removed_format += 1
                continue

            # ❌ ảnh hỏng
            try:
                img = Image.open(path)
                img.verify()
            except:
                os.remove(path)
                removed_corrupt += 1
                continue

            # ❌ ảnh trùng
            try:
                with open(path, 'rb') as f:
                    h = hashlib.md5(f.read()).hexdigest()
                if h in hashes:
                    os.remove(path)
                    removed_dup += 1
                else:
                    hashes[h] = path
            except:
                pass

    total_after = count_images(folder)

    print("\n===== CLEAN REPORT =====")
    print(f"Tổng ảnh ban đầu: {total_before}")
    print(f"Ảnh sai format: {removed_format}")
    print(f"Ảnh hỏng: {removed_corrupt}")
    print(f"Ảnh trùng: {removed_dup}")
    print(f"Tổng bị xoá: {removed_format + removed_corrupt + removed_dup}")
    print(f"Tổng còn lại: {total_after}")
    print("========================\n")
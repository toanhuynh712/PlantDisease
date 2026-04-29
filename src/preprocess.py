import os
import cv2
import numpy as np

IMG_SIZE = 224

mean = np.array([0.485, 0.456, 0.406])
std  = np.array([0.229, 0.224, 0.225])

def preprocess(input_dir, output_dir):
    count = 0

    for root, _, files in os.walk(input_dir):
        for file in files:
            in_path = os.path.join(root, file)

            # giữ structure
            rel = os.path.relpath(root, input_dir)
            out_folder = os.path.join(output_dir, rel)
            os.makedirs(out_folder, exist_ok=True)

            out_path = os.path.join(out_folder, file)

            try:
                img = cv2.imread(in_path)

                # 🔥 thêm dòng này
                if img is None:
                    print("Không đọc được ảnh:", in_path)
                    continue

                img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                img = img / 255.0
                img = (img - mean) / std

                np.save(out_path + ".npy", img)

                count += 1

                # log nhẹ
                if count % 1000 == 0:
                    print("Đã xử lý:", count)

            except Exception as e:
                print("Lỗi:", in_path, e)

    print("Tổng ảnh đã xử lý:", count)
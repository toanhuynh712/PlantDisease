# 🌿 Plant Disease Classification

## 📌 Mô tả
Project xử lý dataset PlantVillage để phục vụ bài toán phân loại bệnh cây bằng Deep Learning.

## ⚙️ Pipeline
- Clean data:
  - Xoá ảnh lỗi
  - Xoá ảnh trùng
  - Lọc định dạng
- Preprocess:
  - Resize về 224x224
  - Normalize theo ImageNet
- Output:
  - Lưu dạng `.npy`

## cách chạy:
- Tải dataset:  https://www.kaggle.com/datasets/mohitsingh1804/plantvillage và giải nén bỏ vào thư mục
- chạy pip install -r requirement.txt để tải những thư viện cần thiết có trong file requirement.txt
- chạy pipeline.py và đợi cỡ 10 phút là sẽ hiện file proccessed chứa data sạch

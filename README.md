# FaceRecognition_MTCNN_FaceNet
## Prepare
1. Chuẩn bị dữ liệu khuôn mặt
```c
Trong thư mục dataset
|-FaceData
   |---raw
   |-----Thư mục chứa ảnh nv1
   |-----Thư mục chứa ảnh nv2
   |----- .....
   |---processed
   |-----Thư mục chứa ảnh sau align nv1
   |-----Thư mục chứa ảnh sau align nv2
   |----- .....
```
2. Cài đặt các thư viện cần thiết
```c
pip install -r requirements.txt
```
3. Tải về models của FaceNet   
   Tải các model từ link https://drive.google.com/file/d/1EXPBSXwTaqrSC0OhUdXNmKSh9qJUQ55-/view    
   Tạo thư mục Models và extract các file vào thư mục này .
## Tiền xử lí dữ liệu cắt khuôn mặt từ ảnh gốc
```c
python src/align_dataset_mtcnn.py  dataset/FaceData/raw dataset/FaceData/processed --image_size 160 --margin 32  --random_order --gpu_memory_fraction 0.25
```
## Train model
```c
python src/classifier.py TRAIN dataset/FaceData/processed Models/20180402-114759.pb Models/facemodel.pkl --batch_size 1000
```
## Kết quả
### Nhận dạng qua camera
```c
python src/face_rec_cam.py
```
### Nhận dạng qua video
```c
python src/face_rec.py --path video/jenna.mp4
```

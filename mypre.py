from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO("runs/detect/train67/weights/best.pt")
# Define path to the image file
#source = "E:/wll/ultralytics-20240330/ultralytics-main/datasets/images/val"

# Run inference on the source
result = model.predict(source="D:/下载/ultralytics-20240303/ultralytics-main/datasets/images/val",show=False,save=True)
print(result)

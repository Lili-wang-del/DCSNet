from ultralytics import YOLO

# 断点续训
# Load a model
model = YOLO('D:/下载/ultralytics-20240303/ultralytics-main/runs/detect/train5/weights/last.pt')  # load a partially trained model

# Resume training
results = model.train(resume=True)
from ultralytics import YOLO
import torch.optim as optim
# Load a model
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
model = YOLO("D:/下载/ultralytics-20240303/ultralytics-main/ultralytics/cfg/models/v8/yolov8-GFPN.yaml")  # build a new model from scratch
#model = YOLO("D:/下载/ultralytics-20240303/ultralytics-main/train21/weights/best.pt")


# Use the model
result=model.train(data="D:/下载/ultralytics-20240303/ultralytics-main/datasets/alldta.yaml", epochs=200, batch=6, workers=0, device=0,optimizer='SGD',lr0=0.01)  # train the mode

#results =model.train(resume=True)

result = model.val()  # evaluate model performance on the validation set
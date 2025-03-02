import warnings
warnings.filterwarnings('ignore')
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('runs/detect/train39/weights/best.pt')
    model.val(data='D:/下载/ultralytics-20240303/ultralytics-main/datasets/alldta.yaml',
              split='val',
              imgsz=640,
              batch=6,
              # rect=False,
              # save_json=True, # if you need to cal coco metrice
              project='runs/val',
              name='exp',
              )
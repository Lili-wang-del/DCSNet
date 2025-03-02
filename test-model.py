
from pathlib import Path

import cv2
from PIL import Image

from ultralytics import RTDETR, YOLO
from ultralytics.utils import ASSETS, DEFAULT_CFG, LINUX, MACOS, ONLINE, ROOT, SETTINGS, WINDOWS

CFG = 'ultralytics/cfg/models/v8/yolov8-GFPN.yaml'
SOURCE = ROOT /'assets/bus.jpg'



def test_model_forward():
    model = YOLO(CFG)
    model (SOURCE)
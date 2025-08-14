from IPython.display import Image
import ultralytics
ultralytics.checks()
from ultralytics import YOLO



# Load a model
model = YOLO('yolov8n-seg.pt')
model.train(data='/home/sislam1/LIMU/config.yaml', epochs=500, imgsz=640)
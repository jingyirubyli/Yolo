from ultralytics import YOLO

model = YOLO('./runs/segment/train2/weights/last.pt')
model("./datasets/tumor/images/val",save=True, conf=0.2, iou=0.5, imgsz =479,classes =0)
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO("yolov8l-seg.pt")
    model.train(data="liver_tumor_16.yaml", epochs=300, batch=8, workers=4, degrees=90.0,imgsz=480)
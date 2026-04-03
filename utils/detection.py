# utils/detection.py (YOLOv8)
from ultralytics import YOLO

# Load YOLO model once
model = YOLO("yolov8n.pt")

def detect_food(image_path):
    """
    Detect objects in an image using YOLOv8.
    Returns a list of detected food/objects.
    """
    results = model(image_path)

    ingredients = []

    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            ingredients.append(label)

    # Remove duplicates
    ingredients = list(set(ingredients))

    if not ingredients:
        return ["No food detected 😢"]

    return ingredients
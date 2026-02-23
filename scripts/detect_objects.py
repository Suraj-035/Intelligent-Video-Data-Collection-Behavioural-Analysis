# scripts/detect_objects.py

from ultralytics import YOLO
import os

model = YOLO("yolov8n.pt")

ACCESSORY_CLASSES = {
    "backpack": "bag",
    "handbag": "bag",
    "sunglasses": "spectacles",
    "tie": "tie",
    "helmet": "helmet"
}

def detect_accessories(frame_dir, max_frames=3):
    frames = sorted(os.listdir(frame_dir))[:max_frames]
    detected = set()
    person_boxes = [] 

    for frame in frames:
        frame_path = os.path.join(frame_dir, frame)
        results = model(frame_path, verbose=False)

        for r in results:
            for box in r.boxes:
                cls = model.names[int(box.cls)]

                if cls == "person": 
                    person_boxes.append(box.xyxy[0].tolist())

                if cls in ACCESSORY_CLASSES:
                    detected.add(ACCESSORY_CLASSES[cls])

    return list(detected), person_boxes 

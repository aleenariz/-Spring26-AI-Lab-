from ultralytics import YOLO
import cv2
import os

model = YOLO("yolov8n.pt")

def detect_animals(image_path):
    results = model(image_path)

    image = cv2.imread(image_path)

    animal_classes = ["cow", "sheep", "horse", "elephant", "bear", "zebra", "giraffe"]

    count = 0

    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]

            if label in animal_classes:
                count += 1
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(image, (x1, y1), (x2, y2), (0,255,0), 2)
                cv2.putText(image, label, (x1, y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                            (0,255,0), 2)

    output_path = "static/result.jpg"
    cv2.imwrite(output_path, image)

    return count, output_path
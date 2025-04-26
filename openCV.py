import cv2
from ultralytics import YOLO

model = YOLO("runs/detect/train2/weights/best.pt")  # Load trained model

cap = cv2.VideoCapture(0)  # Open webcam
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    results = model(frame)  # Run YOLO on the frame
    for r in results:
        frame = r.plot()  # Plot detections on the frame

    cv2.imshow("YOLO Inference", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

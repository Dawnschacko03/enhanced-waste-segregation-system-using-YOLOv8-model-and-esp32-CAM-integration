
from ultralytics import YOLO

if __name__ == '__main__':
    # Load trained model
    model = YOLO("runs/detect/train2/weights/best.pt")

    # Validate on test dataset to get testing accuracy
    metrics = model.val(data="data.yaml", split='test', workers=0)  # Set workers=0 to avoid multiprocessing issues

    # Print accuracy metrics
    print(metrics)

from ultralytics import YOLO

if __name__ == '__main__':
    # Load your trained model
    model = YOLO("runs/detect/train2/weights/best.pt")

    # Validate on the training dataset using the correct dataset path
    metrics = model.val(data="data.yaml", split='train', workers=0)  # Set workers=0 to prevent multiprocessing errors

    # Print accuracy metrics
    print(metrics)

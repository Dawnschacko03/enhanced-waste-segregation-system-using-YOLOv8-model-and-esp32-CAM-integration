import wandb
from ultralytics import YOLO

# Log in with your Wandb API key
wandb.login(key='d159aadc772cb0275c92252eaef4705424beca2a')

# Define the training function
def train_model():
    model = YOLO("yolov8n.pt")  # Load YOLOv8 model
    model._check_is_pytorch_model()
    model.train(
        data="data.yaml",  # Path to your dataset config file
        epochs=50,         # Increase if needed
        imgsz=640,         # Image size
        lr0=0.001,  # Learning rate
        weight_decay=0.0005,
        conf=0.35,  # Confidence threshold
        iou=0.6,  # IoU threshold for NMS
        device="cuda"      # Use GPU (CUDA)
    )

# Add the safe main check
if __name__ == '__main__':
    train_model()


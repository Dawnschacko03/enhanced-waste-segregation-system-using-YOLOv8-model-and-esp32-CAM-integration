import torch
print("CUDA Available:", torch.cuda.is_available())  # Should return True
print("CUDA Version:", torch.version.cuda)  # Should return 12.1
print("GPU Name:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU detected")
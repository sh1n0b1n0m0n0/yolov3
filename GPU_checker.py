import torch

print('Using torch %s %s' % (torch.__version__, torch.cuda.get_device_properties(0) if torch.cuda.is_available() else 'CPU'))
print("Cuda is available:", torch.cuda.is_available())
print("Device number:", torch.cuda.current_device())
print("Device name:", torch.cuda.get_device_name(0))

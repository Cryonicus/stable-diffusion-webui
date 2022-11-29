###Convert dropped CKPT file to Tensor
import torch
import sys
from safetensors.torch import save_file

print(sys.argv)
weights = torch.load(sys.argv[1])["state_dict"]
save_file(weights,f"{sys.argv[1][:-5]}.safetensors")
# Pytorch imports
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from torchsummary import summary

# Huggingface imports
from transformers import AutoModelForCausalLM, AutoConfig

# Miscellaneous ML library imports
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import warnings
warnings.filterwarnings('ignore') # To ignore the big red future warnings (for now and convenience)

# Version checks
assert sys.version_info >= (3,10)

# to make this notebook's output stable across runs
SEED=42
np.random.seed(SEED)
torch.manual_seed(SEED)

# Get available device for training
device = ( "cuda"     # CUDA for GPU compute
           if torch.cuda.is_available()
           else "cpu" )   # CPU won't cut it. :P

print(f"{device} device available")


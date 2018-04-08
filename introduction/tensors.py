from __future__ import print_function
import torch
import numpy as np

x = torch.randn(5,3)
y = torch.randn(5,3)
if torch.cuda.is_available():
    x = x.cuda()
    y = y.cuda()
    print(x + y)


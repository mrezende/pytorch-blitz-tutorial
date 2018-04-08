from __future__ import print_function
import torch
import numpy as np

a = np.ones(5)
b = torch.from_numpy(a)
np.add_(a, 1, out=a)
print(a)
print(b)


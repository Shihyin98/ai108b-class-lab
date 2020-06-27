import torch
import numpy as np

a = np.ones(5)
b = torch.from_numpy(a)
np.add(a, 1, out=a)
print('a = ', a)
print('b = ', b, '\n')

x = torch.zeros(2, 1, 2, 1, 2)
print('x = ', x.size(), '\n')

y = torch.squeeze(x)
print('y = ', y.size())

y = torch.squeeze(x, 0)
print('y = ', y.size())

y = torch.squeeze(x, 1)
print('y = ', y.size())

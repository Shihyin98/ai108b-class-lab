import torch

c = torch.abs(torch.FloatTensor([-1, -2, 3]))
print('c = ', c)

a = torch.randn(4)
print('a = ', a)

b = torch.add(a, 20)
print('b = ', b)

import torch

a = torch.randn(1, 3)
print('a = ', a)

b = torch.mean(a)
print('b = ', b)

c = torch.randn(4, 4)
print('c = ', c)

d = torch.mean(c, 1)
print('d = ', d)

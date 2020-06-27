import torch

a = torch.eq(torch.Tensor([[1, 2], [3, 4]]), torch.Tensor([[1, 1], [4, 4]]))
print('a = ', a)

b = torch.equal(torch.Tensor([1, 2]), torch.Tensor([1, 2]))
print('b = ', b)

c = torch.ge(torch.Tensor([[1, 2], [3, 4]]), torch.Tensor([[1, 1], [4, 4]]))
print('c = ', c)

d = torch.gt(torch.Tensor([[1, 2], [3, 4]]), torch.Tensor([[1, 1], [4, 4]]))
print('d = ', d)

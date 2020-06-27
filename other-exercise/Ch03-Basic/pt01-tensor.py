import torch

z = torch.Tensor(4, 5)
print('z = ', z)

y = torch.rand(4, 5)  # 產生一個4列5行的矩陣
print('\nz + y = ', z + y)
print('\nz + y = ', torch.add(z, y))

b = z.numpy()
print('\nb = ', b, '\n')

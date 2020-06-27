# :eyes: Outline
1. pt01-tensor.py
2. pt02-tensor.py
3. pt03-math.py
4. pt04-math.py
5. pt05-operator.py
<br>

~ ~ ~ ~ ~ 

# [1. pt01-tensor.py](Ch03-Basic/pt01-tensor.py)
## 1.1- Terminal
```
D:\dl-and-nlp-with-pytorch\Ch03-Basic> py .\pt01-tensor.py
```

## 1.2- Output
```
# Output 1: Create the matrices 4*5
z =  tensor([[8.9082e-39, 6.9796e-39, 9.0919e-39, 9.9184e-39, 7.3470e-39],
        [1.0194e-38, 1.0469e-38, 1.0010e-38, 8.4490e-39, 1.1112e-38],
        [9.5511e-39, 1.0102e-38, 7.3470e-39, 1.0653e-38, 1.0194e-38],
        [4.6838e-39, 8.4489e-39, 9.6429e-39, 8.4490e-39, 1.0561e-38]])

# Output 2: Sum of two matrices
z + y =  tensor([[0.0522, 0.6687, 0.5638, 0.8213, 0.5958],
        [0.8571, 0.5176, 0.9698, 0.6022, 0.1823],
        [0.8429, 0.2876, 0.8568, 0.1773, 0.3517],
        [0.7189, 0.5443, 0.2081, 0.4788, 0.9083]])

# Output 3: Sum of two matrices with add()
z + y =  tensor([[0.0522, 0.6687, 0.5638, 0.8213, 0.5958],
        [0.8571, 0.5176, 0.9698, 0.6022, 0.1823],
        [0.8429, 0.2876, 0.8568, 0.1773, 0.3517],
        [0.7189, 0.5443, 0.2081, 0.4788, 0.9083]])

# Output 4: Convert a Tensor into a numpy array
b =  [[8.9082057e-39 6.9796266e-39 9.0918697e-39 9.9183695e-39 7.3469686e-39]
 [1.0193900e-38 1.0469391e-38 1.0010205e-38 8.4490268e-39 1.1112207e-38]
 [9.5510542e-39 1.0102060e-38 7.3469686e-39 1.0653087e-38 1.0193886e-38]
 [4.6837644e-39 8.4489427e-39 9.6428784e-39 8.4490030e-39 1.0561243e-38]]
```

## 1.3- Solution
* Output 1:
  ```
  z =  tensor([[8.9082e-39, 6.9796e-39, 9.0919e-39, 9.9184e-39, 7.3470e-39],
               [1.0194e-38, 1.0469e-38, 1.0010e-38, 8.4490e-39, 1.1112e-38],
               [9.5511e-39, 1.0102e-38, 7.3470e-39, 1.0653e-38, 1.0194e-38],
               [4.6838e-39, 8.4489e-39, 9.6429e-39, 8.4490e-39, 1.0561e-38]])
  ```
  利用 PyTorch　**隨機** 建立一個 4*5的陣列
<br>

* Output 2, Output 3:
  ```
  z + y =  tensor([[0.0522, 0.6687, 0.5638, 0.8213, 0.5958],
                  [0.8571, 0.5176, 0.9698, 0.6022, 0.1823],
                  [0.8429, 0.2876, 0.8568, 0.1773, 0.3517],
                  [0.7189, 0.5443, 0.2081, 0.4788, 0.9083]])
  ```
* 兩矩陣相加，有兩種方法表達：
  1. 矩陣存於個別變數，並相加。
  2. add() 方法
<br>

* Output 4:
  ```
  b =  [[8.9082057e-39 6.9796266e-39 9.0918697e-39 9.9183695e-39 7.3469686e-39]
        [1.0193900e-38 1.0469391e-38 1.0010205e-38 8.4490268e-39 1.1112207e-38]
        [9.5510542e-39 1.0102060e-38 7.3469686e-39 1.0653087e-38 1.0193886e-38]
        [4.6837644e-39 8.4489427e-39 9.6428784e-39 8.4490030e-39 1.0561243e-38]]
  ```
  將 Tensor 轉換為 numpy 陣列
<br>

## 1.4- Explain
* torch.Tensor(4, 5):　矩陣形式呈現 with Pytorch
* z.numpy(): 陣列形式呈現 with Numpy
<br>

---
# [2. pt02-tensor.py](Ch03-Basic/pt02-tensor.py)
## 2.1- Terminal
```
D:\dl-and-nlp-with-pytorch\Ch03-Basic> py .\pt02-tensor.py
```

## 2.2- Output
```
a =  [2. 2. 2. 2. 2.]                # Output 1: Create the array with Numpy
b =  tensor([2., 2., 2., 2., 2.], dtype=torch.float64)   # Output 2

x =  torch.Size([2, 1, 2, 1, 2])     # Output 3

y =  torch.Size([2, 2, 2])           # Output 4
y =  torch.Size([2, 1, 2, 1, 2])     # Output 5
y =  torch.Size([2, 2, 1, 2])        # Output 6
```

## 2.3- Solution
* Output 1: 
  ```
  a =  [2. 2. 2. 2. 2.]
  ```
* 創建一個 維度5　元素為1　的陣列，並相加。
  * np.ones(5)
  * np.add(a, 1, out=a)
* Output 2: 
  ```
  b =  tensor([2., 2., 2., 2., 2.], dtype=torch.float64)
  ```
  * torch.from_numpy(a)
* Output 3: 
  ```
  x =  torch.Size([2, 1, 2, 1, 2])
  ```
  * torch.zeros(2, 1, 2, 1, 2)
* Output 4: torch.squeeze(x)
* Output 5: torch.squeeze(x, 0)
* Output 6: torch.squeeze(x, 1)
  * x = input
  * 1 = dim (指定對維度1)
<br>

## 2.4- Explain
* Array: dimension(尺寸), shape(形狀), size(大小)
* 方法：
  * np.ones()
  * squeeze() [[1]](-)
    * 作用： 降维 
    * 表達式：　torch.squeeze(input, dim=None, out=None)
    * 参数:
      input (Tensor) – 输入张量
      dim (int, optional) – 如果给定，则input只会在给定维度挤压
      out (Tensor, optional) – 输出张量
    * 将输入张量形状中的1 去除并返回。 
      Ex: 输入是 (A×1×B×1×C×1×D)，输出形状： (A×B×C×D)
    * 当给定dim时，那么挤压操作只在给定维度上。
      Ex: 输入形状: (A×1×B), **squeeze(input, 0) 将会保持张量不变**，只有用 squeeze(input, 1)，形状会变成 (A×B)。
    * 注意： 返回张量与输入张量共享内存，所以改变其中一个的内容会改变另一个。
    * 主要**对数据的维度进行压缩**，去掉维数为1的的维度，比如是一行或者一列这种。
      Ex: 一个一行三列(1,3)的数去掉第一个维数为一的维度之后就变成(3)行。[[4]](-)
* torch.from_numpy(ndarray) → Tensor  
  * 从一个 numpy.ndarray 创建一个 Tensor.
    返回的张量和 ndarry 共享相同的内存。[[2]](-)
* Python numpy函数：zeros()、ones()、empty()[[3]](-)
  * zeros(): **给数组赋初始值**的时候，经常会用到 0数组。
  * ones(): 创建**任意维度和元素个数**的数组，其元素值均为1。
  * empty(): 创建数组**最快方法**，数组内所有元素均为空，没有实际意义。
<br>

---
# [3. pt03-math.py](Ch03-Basic/pt03-math.py)
## 3.1- Terminal
```
D:\dl-and-nlp-with-pytorch\Ch03-Basic> py .\pt03-math.py  
```

## 3.2- Output
```
c =  tensor([1., 2., 3.])      # Output 1: float()
a =  tensor([-0.6994,  0.6672, -0.6707, -0.2020])   # Output 2: randn() 
b =  tensor([19.3006, 20.6672, 19.3293, 19.7980])   # Output 3: add()
```

## 3.3- Solution
* c = torch.abs(torch.FloatTensor([-1, -2, 3]))
* a = torch.randn(4)
* b = torch.add(a, 20)
<br>

## 3.4- Explain
* 取絕對值
* 隨機生成
* 相加
<br>

---
# [4. pt04-math.py](Ch03-Basic/pt04-math.py)
## 4.1- Terminal
```
D:\dl-and-nlp-with-pytorch\Ch03-Basic> py .\pt04-math.py
```

## 4.2- Output
```
a =  tensor([[ 0.5486, -0.4855, -2.3697]])           # Output 1
b =  tensor(-0.7689)                                 # Output 2
c =  tensor([[-0.7970, -0.1691, -0.3763,  0.6330], 
        [ 1.0082, -0.6468, -1.1482,  0.1494],
        [ 1.6822,  0.1924, -2.6098,  0.0085],
        [ 0.7658,  1.5994, -1.0221, -0.6464]])       # Output 3
d =  tensor([-0.1774, -0.1593, -0.1817,  0.1742])    # Output 4
```

## 4.3- Solution
* a = torch.randn(1, 3)
* b = torch.mean(a)
* c = torch.randn(4, 4)
* d = torch.mean(c, 1)
<br>

## 4.4- Explain
* 取絕對值
* 取平均值
<br>

---
# [5. pt05-operator.py](Ch03-Basic/pt05-operator.py)
## 5.1- Terminal
```
D:\dl-and-nlp-with-pytorch\Ch03-Basic> py .\pt05-operator.py
```

## 5.2- Output
```
a =  tensor([[ True, False],
        [False,  True]])        # Output 1
b =  True                       # Output 2 
c =  tensor([[ True,  True],
        [False,  True]])        # Output 3 
d =  tensor([[False,  True],
        [False, False]])        # Output 4
```

## 5.3- Solution
* a = torch.eq(torch.Tensor([[1, 2], [3, 4]]), torch.Tensor([[1, 1], [4, 4]]))
* b = torch.equal(torch.Tensor([1, 2]), torch.Tensor([1, 2]))
* c = torch.ge(torch.Tensor([[1, 2], [3, 4]]), torch.Tensor([[1, 1], [4, 4]]))
* d = torch.gt(torch.Tensor([[1, 2], [3, 4]]), torch.Tensor([[1, 1], [4, 4]]))
<br>

## 5.4- Explain
* 相等比較
* 大小比較
<br>

-----
## Reference
[[1] torch.unsqueeze() 和 torch.squeeze()_Medium_李小伟_2019](https://zhuanlan.zhihu.com/p/86763381)<br>
[[2] Tensors](https://pytorch.apachecn.org/docs/1.0/torch_tensors.html)<br>
[[3] Python numpy函数：zeros()、ones()、empty()](https://blog.csdn.net/qq_28618765/article/details/78085457)<br>
[[4] pytorch学习 中 torch.squeeze() 和torch.unsqueeze()的用法](https://blog.csdn.net/xiexu911/article/details/80820028)<br>
[[5] torch.gt函数的用法](https://blog.csdn.net/JIEJINQUANIL/article/details/49590771)


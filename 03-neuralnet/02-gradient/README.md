# :eyes: Outline
1. [vecGradient.py](vecGradient.py)
2. [npGradient.py](npGradient.py)

# 1. vecGradient.py
## 1.1- Terminal
```
D:\ai108b\03-neuralnet\02-gradient> py .\vecGradient.py
```

## 1.2- Output
```
x= 1 y= 3
df(f(x,y), 0) =  2.009999999999934
df(f(x,y), 1) =  6.009999999999849
grad(f)= [2.009999999999934, 6.009999999999849]
```

## 1.3- Solution
* 我們想找函數 f 的最低點
  ```
  def f(p):
    [x,y] = p
    return x * x + y * y
  ```
<br>

* 函數 f 對變數 p[k] 的偏微分: df / dp[k]
* 例如在上述 f 範例中，k=0, df/dx, k=1, df/dy
  ```
  def df(f, p, k):
    p1 = p.copy()
    p1[k] = p[k]+step
    return (f(p1) - f(p)) / step
  ```
<br>

* 函數 f 在點 p 上的梯度
  ```
  def grad(f, p):
    gp = p.copy()
    for k in range(len(p)):
        gp[k] = df(f, p, k)
    return gp
  ```
<br>


## 1.4- Explain
* 偏微分 (多變數)
* 梯度
<br>


--

# 2. diff2.py
## 2.1- Terminal
```
D:\ai108b\03-neuralnet\02-gradient> py .\npGradient.py
```

## 2.2- Output
```
x,y= 1.01 3.0
x,y= 1.0 3.0
df(f, p, 0) =  2.009999999999934
x,y= 1.0 3.01
x,y= 1.0 3.0
df(f, p, 1) =  6.009999999999849
x,y= 1.01 3.0
x,y= 1.0 3.0
x,y= 1.0 3.01
x,y= 1.0 3.0
grad(f)= [2.01 6.01]
```

## 2.3- Solution
* 使用　Numpy
<br>


## 2.4- Explain
* 偏微分 (多變數)
* 梯度
<br>

--

## Reference




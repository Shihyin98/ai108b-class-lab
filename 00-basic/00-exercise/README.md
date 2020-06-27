# :eyes: Outline
1. [norm2.py](norm2.py)
2. [poly1.py](poly1.py)

# 1. norm2.py
## 1.1- Terminal
```
D:\ai108b\00-basic_w1-0305-Python\00-exercise> py .\norm2.py
```

## 1.2- Output
```
1.7320508075688772    # Output 1:  norm2(v)
1.7320508075688772    # Output 2:  norm(v,2)
3.0                   # Output 3:  norm(v,1)
1.4422495703074083    # Output 4:  norm(v,3)
```

## 1.3- Solution
* Initial-Variables:
  * v = [1, 1, 1]
  * s, x, k
<br>

* Output 1:
  * ``1.7320508075688772``
    對 3 開平方根號
    <br>

    [$$\sqrt{3}$$](https://latex.codecogs.com/gif.latex?\sqrt{3})
    <!-- $$\sqrt{3}$$ -->
  * Variables:
    | Var  |  s  |  x  |
    | :--: | :--:| :--:|
    | init |s = 0|x = 1|
    |final |s = 3|x = 1|
<br>

* Output 2:
  * ``1.7320508075688772``
    3 的 1/2 次方 (對 3 開平方根號)
    <br>

    [$$3^{\tfrac{1}{2}}$$](https://latex.codecogs.com/gif.latex?3^{\tfrac{1}{2}})
    <!-- $$3^{\tfrac{1}{2}}$$ -->
  * Variables:
    | Var  |  s  |  x  |  k  |
    | :--: | :--:| :--:| :--:|
    | init |s = 0|x = 1|k = 2|
    |final |s = 3|x = 1|k = 2|
<br>

* Output 3:
  * ``3.0``
    3 的 1 次方
    <br>

    [$$3^{1}$$](https://latex.codecogs.com/gif.latex?3^{1})
    <!-- $$3^{1}$$ -->
  * Variables:
    | Var  |  s  |  x  |  k  |
    | :--: | :--:| :--:| :--:|
    | init |s = 0|x = 1|k = 1|
    |final |s = 3|x = 1|k = 1|
<br>

* Output 4:
  * ``1.4422495703074083``
    3 的 1/3 次方 (對 3 開立方根號) 
    <br>

    [$$\sqrt[3]{3}$$](https://latex.codecogs.com/gif.latex?\sqrt[3]{3})
    <!-- $$\sqrt[3]{3}$$ -->
  * Variables:
    | Var  |  s  |  x  |  k  |
    | :--: | :--:| :--:| :--:|
    | init |s = 0|x = 1|k = 3|
    |final |s = 3|x = 1|k = 3|

## 1.4- Explain
* Library: **math**
  * sqrt() 平方根[[2]](-)
  * abs() 絕對值[[3]](-)
<br>

* 表達式[[1]](-)

  | 運算子 | 說明 | 舉例 | 結果 |
  | :--:  | :--: | :--: | :--: |
  |   **  |  次方| A=5**2| A=25|
  |   /   |浮點除法|A=5/2| A=2.5|
  |  //  |整數除法(去除小數點)| A=5//2| A=2|
  |   %  |相除後求餘數|A=5%2| A=1|
  

# 2. poly1.py
## 2.1- Terminal
```
D:\ai108b\00-basic_w1-0305-Python\00-exercise> py .\poly1.py
```

## 2.2- Output
```
pmul([1, 2], [1, 1]) =  [1, 3, 2]                                        # Output 1:  pmul([1, 2], [1, 1])
pdiv([3, 3, 2], [1, 1]) =  {'r': [2.0], 'q': [3.0, 0.0]}                 # Output 2:  pdiv([3, 3, 2], [1, 1]))
pdiv([1, 3, 2], [1, 1, 1]) =  {'r': [2.0, 1.0], 'q': [1.0]}              # Output 3:  pdiv([1, 3, 2], [1, 1, 1]))
pdiv([1.0, 4.0, 3.0], [1.0, 3.0, 2.0]) =  {'r': [1.0, 1.0], 'q': [1.0]}  # Output 4:  pdiv([1.0, 4.0, 3.0], [1.0, 3.0, 2.0]))
xy =  [1, 3, 2]                     # Output 5:  pmul(x, y)
xz =  [1, 4, 3]                     # Output 6:  pmul(x, z)
d= {'r': [1.0, 1.0], 'q': [1.0]}    # Output 7:  pgcd(xz, xy)
d= {'r': [0.0], 'q': [1.0, 2.0]}    
gcd(xz, xy) =  [1.0, 1.0]           
```

## 2.3- Solution
* Initial-Variables:
  * aa
<br>

* Output 1:
  * ``pmul([1, 2], [1, 1]) =  [1, 3, 2]``
  * 交叉相乘、十字相乘法
  * Variables:
    | Var    |  a   |  b   |   c     | c[i+j] += a[i]* b[j] |       Memo      |
    | :--:   | :---:| :---:|:-------:| :-------------------:| :------------:  |
    | init   |[1, 2]|[1, 1]|[0, 0, 0]|            -         |        -        |
    |i=0; j=0|[1, 2]|[1, 1]|[1, 0, 0]| c[0+0] += a[0]* b[0] | c[0] = 0 + 1* 1 |
    |i=0; j=1|[1, 2]|[1, 1]|[1, 1, 0]| c[0+1] += a[0]* b[1] | c[1] = 0 + 1* 2 |
    |i=1; j=0|[1, 2]|[1, 1]|[1, 3, 0]| c[1+0] += a[1]* b[0] | c[1] = 1 + 2* 1 |
    |i=1; j=1|[1, 2]|[1, 1]|[1, 3, 2]| c[1+1] += a[1]* b[1] | c[2] = 0 + 2* 1 |
    | final  |[1, 2]|[1, 1]|[1, 3, 2]|            -         |        -        |
<br>

* Output 2:
  * ``pdiv([3, 3, 2], [1, 1]) =  {'r': [2.0], 'q': [3.0, 0.0]}``
  * Variables:
    | Var    |   a     |  b   |  la  |  lb |       r       |    q     | scale |      Memo      |
    | :--:   |  :----: |:----:| :--: | :--:|  :----------: | :------: |:----: | :-----------:  |
    | init   |[3, 3, 2]|[1, 1]|  3   |  2  |   [3, 3, 2]   |  [0, 0]  |   -   |       -        |
    |i=0; j=0|[3, 3, 2]|[1, 1]|  3   |  2  |  [0.0, 3, 2]  | [3.0, 0] |  3.0  |       -        |
    | final  |[3, 3, 2]|[1, 1]|  3   |  2  |[0.0, 0.0, 2.0]|[3.0, 0.0]|  0.0  |       -        |
<br>

* Output 3:
  * ``pdiv([1, 3, 2], [1, 1, 1]) =  {'r': [2.0, 1.0], 'q': [1.0]}``
  * Variables:
    | Var    |   a     |    b    |  la  |  lb |       r       |    q     | scale |      Memo      |
    | :--:   |  :----: |  :----: | :--: | :--:|  :----------: | :------: |:----: | :-----------:  |
    | init   |[1, 3, 2]|[1, 1, 1]|  3   |  3  |   [1, 3, 2]   |    [0]   |  1.0  |       -        |
    |i=0; j=0|[1, 3, 2]|[1, 1, 1]|  3   |  3  |  [0.0, 3, 2]  |   [1.0]  |  1.0  |       -        |
    | final  |[1, 3, 2]|[1, 1, 1]|  3   |  3  |[0.0, 2.0, 1.0]|   [1.0]  |  1.0  |       -        |
<br>

* Output 4:
  * ``pdiv([1.0, 4.0, 3.0], [1.0, 3.0, 2.0]) =  {'r': [1.0, 1.0], 'q': [1.0]}``
  * Variables:
    | Var    |       a       |       b       |  la  |  lb |       r       |    q     | scale |      Memo      |
    | :--:   |  :----------: |  :----------: | :--: | :--:|  :----------: | :------: |:----: | :-----------:  |
    | init   |[1.0, 4.0, 3.0]|[1.0, 3.0, 2.0]|  3   |  3  |[1.0, 4.0, 3.0]|    [0]   |   -   |       -        |
    |i=0; j=0|[1.0, 4.0, 3.0]|[1.0, 3.0, 2.0]|  3   |  3  |[1.0, 4.0, 3.0]|   [1.0]  |  1.0  |       -        |
    | final  |[1.0, 4.0, 3.0]|[1.0, 3.0, 2.0]|  3   |  3  |[1.0, 1.0, 1.0]|   [1.0]  |  1.0  |       -        |
<br>

* Output 5:
  * ``xy =  [1, 3, 2]``
* Output 6:
  * ``xz =  [1, 4, 3]``
  * Variables:
    |    Var   |   x  |   y  |   z  |   xy    |   xz    |
    | :------: | :--: | :--: | :--: | :-----: | :-----: |
    |pmul(x, y)|[1, 1]|[1, 2]|[1, 3]|[1, 3, 2]|     -   |
    |pmul(x, z)|[1, 1]|[1, 2]|[1, 3]|     -   |[1, 4, 3]|
<br>

* Output 7:
  * ``d= {'r': [1.0, 1.0], 'q': [1.0]}``
  * ``d= {'r': [0.0], 'q': [1.0, 2.0]}``
  * ``gcd(xz, xy) =  [1.0, 1.0]``
<br>

## 2.4- Explain
* The [0] * x creates a list with x elements. So,[[4]](-)
    ```
    >>> [ 0 ] * 5
    #output
    [0, 0, 0, 0, 0]
    ```
<br>

--

## Reference
[1] [Python資料型別、變數與運算子_高中資訊科技概論教師黃建庭的教學網站](https://sites.google.com/site/zsgititit/home/python-cheng-shi-she-ji/python-bian-shu-yu-yun-suan-zi)<br>
[2] [Python sqrt()方法_極客書](http://tw.gitbook.net/python/number_sqrt.html)<br>
[3] [Python abs()方法_極客書](http://tw.gitbook.net/python/number_abs.html)<br>
[4] [What does the [0]*x syntax do in Python?_stackoverflow](https://stackoverflow.com/questions/6007881/what-does-the-0x-syntax-do-in-python)<br>


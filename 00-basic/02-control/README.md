# :eyes: Outline
1. [break.py](break.py)
2. [continue.py](continue.py)
3. [for.py](for.py)
4. [for2.py](for2.py)
5. [if.py](if.py)

# 1. if.py
## 1.1- Terminal
```
D:\ai108b\00-basic\02-control> py .\if.py
Enter an integer : 40  
```

## 1.2- Output
```
No, it is a little lower than that
Done
```

## 1.3- Solution
* 判斷式，判斷數字大小。
* Enter an integer : 40 
<br>

* Output:
  * ``No, it is a little lower than that``
  * 提示猜的數字再小一點
<br>


## 1.4- Explain
* if..
* if.. else..
* if.. elif.. elif.. else..
<br>


# 2. for.py
## 2.1- Terminal
```
D:\ai108b\00-basic\02-control> py .\for.py
```

## 2.2- Output
```
1
2
3
4       
```

## 2.3- Solution
* 迴圈打印
  * range(1, 5)
  * 1, 2, 3, 4 (不包含 5)
<br>


## 2.4- Explain
* for
* while
<br>



# 3. break.py
## 3.1- Terminal
```
D:\ai108b\00-basic\02-control> py .\break.py 
```

## 3.2- Output
```
Enter something : rrr
Length of the string is 3

Enter something : hhhh
Length of the string is 4

Enter something : kikiki
Length of the string is 6

Enter something : 567
Length of the string is 3

Enter something : 123ac
Length of the string is 5

Enter something : quit
Done
```

## 3.3- Solution
* 計算輸入的字元單位
<br>


## 3.4- Explain
* break 強制跳開 (迴圈)
<br>

# 4. continue.py
## 4.1- Terminal
```
D:\ai108b\00-basic\02-control> py .\continue.py
```

## 4.2- Output
```
Enter something : 5
Too small

Enter something : 20
Too small

Enter something : 50
Too small

Enter something : 100
Input is of sufficient length

Enter something : asdf
Input is of sufficient length

Enter something : a
Too small

Enter something : aa
Too small

Enter something : quit
```

## 4.3- Solution
* 計算輸入的字元單位
* 回報訊息：
  * 輸入字元單位 >= 3
    * Input is of sufficient length
  * 輸入字元單位 < 3
    * Too small
<br>


## 4.4- Explain
* continue 繼續執行
<br>



--

## Reference




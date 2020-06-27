# :eyes: Outline
1. [googlemt1.py](googlemt1.py)


# 1. googlemt1.py
## 1.1- Terminal
```
D:\11-deepLearning_w16\07-nlp\mt\googlemt> py .\googlemt1.py
```

## 1.2- Output
```
======== 英文 ========
The number of micro operations is minimized without impacting the quality of the generated code much. For example, instead of generating every possible move between every 32 PowerPC registers, we just generate moves to and from a few temporary registers. These registers T0, T1, T2 are typically stored in host registers by using the GCC static register variable extension.

======== 中文 ========
微操作的數量被最小化，而不會很大程度地影響所生成代碼的質量。例如，我們沒有在每個32個PowerPC寄存器之間生成所有可能的移動，而是僅生成了一些臨時寄存器之間的移動。這些寄存器T0，T1，T2通常通過使用GCC靜態寄存器變量擴展存儲在主機寄存器中。
```

## 1.3- Solution
* 引用 Google翻譯，翻譯一段文字。


## 1.4- Explain
* 呼叫 Google API，使用高品質，且強大的套件。
* 不需要甚麼都自己寫，自己寫的不會比現在線上的翻譯軟體牛逼。
* 善用線上現成的模型或套件，透過 API進行接口對對接。

<br>

--

## Reference
[1] [No module named 'googletrans'_pip install googletrans](https://pypi.org/project/googletrans/)

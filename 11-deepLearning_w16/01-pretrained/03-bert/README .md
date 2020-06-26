# :eyes: Outline
1. [bert1.py](bert1.py)


# 1. bert1.py
## 1.1- Terminal
```
D:\11-deepLearning_w16\01-pretrained\03-bert> py .\bert1.py
```

## 1.2- Output
```
Top 1 (67%)：['[CLS]', '等', '到', '潮', '水', '來', '了', '，', '就', '知'] ...
Top 2 (25%)：['[CLS]', '等', '到', '潮', '水', '濕', '了', '，', '就', '知'] ...
Top 3 ( 2%)：['[CLS]', '等', '到', '潮', '水', '過', '了', '，', '就', '知'] ...
```

## 1.3- Solution
* 推測遮罩部分的文字
```
[CLS] 等到潮水 [MASK] 了，就知道誰沒穿褲子。
['[CLS]', '等', '到', '潮', '水', '[MASK]', '了', '，', '就', '知'] ...
```

<br>

* Output:
  * ``來``、``濕``、``過``
  * 推測前三名，**適合填充** 至遮罩部分的字。
  * 盡量不失語意

<br>


## 1.4- Explain
* 此模型用於 **克漏字**、**預測下一個字**。

<br>

--
## Reference
[1] [進擊的 BERT：NLP 界的巨人之力與遷移學習](https://leemeng.tw/attack_on_bert_transfer_learning_in_nlp.html)
[2] [No module named 'transformers'_pip install transformers](https://nomodulenamed.com/zh/m/transformers.convert_pytorch_checkpoint_to_tf2)
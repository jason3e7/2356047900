### 第一次練習
# PPC
### 就上手

jason3e7 20190105

Note:title:"第一次練習 PPC 就上手"

---

## calculator
### 200

* 你能幫我解一些方程式嗎？

* nc 140.110.112.29 5119

---

## hurry-up
### 200

* nc 140.110.112.29 5123

---

## lambda
### 200

* nc 140.110.112.29 5124

---

## temperature
### 200

* 我需要你幫忙把華氏轉攝氏

* nc 140.110.112.29 5127

---

## ooxx
### 200

* 來玩圈圈叉叉吧nc 140.110.112.29 5126

* [server.py-0e207766c3283f7f62f6f057cbf222c57970086b](PPC/ooxx/server.py-0e207766c3283f7f62f6f057cbf222c57970086b)

---

## ooxx 心得
* 一開始以為要贏一定數量的場次, 在思考必勝演算法.
* 對 recvuntil 使用更熟練一點了, 但是 recvline 為什麼有些情境不能用, 還不知道原因.
* `base(int.from_bytes(flag, 'big'), 9)`
* 對編碼法還不太熟

Note:
* 技術債
  * [#!/usr/bin/python3 和 #!/usr/bin/env python3 的作用](https://www.jianshu.com/p/400c612381dd)
  * int.from_bytes
  * [How to Convert Int to Bytes in Python 2 and Python 3](https://www.delftstack.com/howto/python/how-to-convert-int-to-bytes-in-python-2-and-python-3/)
  * [3.5 字節到大整數的打包與解包](https://python3-cookbook.readthedocs.io/zh_CN/latest/c03/p05_pack_unpack_large_int_from_bytes.html)
  * b'\x??', 是什麼呢? 怎麼解讀和轉換
  * [Python Bytearray Printing](https://stackoverflow.com/questions/17093700/python-bytearray-printing)
  * [[Python初學起步走-Day13] - bytes & bytearray](https://ithelp.ithome.com.tw/articles/10159609)
  * [What's the correct way to convert bytes to a hex string in Python 3?](https://stackoverflow.com/questions/6624453/whats-the-correct-way-to-convert-bytes-to-a-hex-string-in-python-3/6624521)
* [數制](https://www.convertworld.com/zh-hant/numerals/)
* [Is there a way to substring a string?](https://stackoverflow.com/questions/663171/is-there-a-way-to-substring-a-string)

---

## alphabet
### 200

* 可以幫我數一下有幾個英文字母嗎 ?

* nc 140.110.112.29 5128

---

## pi
### 200

* 幫我算算圓周率

* nc 140.110.112.29 5130

Note:
* [Python 計算任意位數的圓周率π](https://blog.csdn.net/lnotime/article/details/82319973)
  * 馬青公式
  * 其實最多100位, 可以 hard code.
* `**`, 冪
* `//`, 取整除

---

## vending-machine
### 200

* 來買一些 flags 或是食物飲料

* nc 140.110.112.29 5132

Note:
* 猜數字, 二分搜尋法

---

# The End
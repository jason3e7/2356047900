### 第一次練習
# reverseLevel2
### 就上手

jason3e7 20190102

Note:title:"第一次練習 reverseLevel2 就上手"

---

## 林思辰_base64
### 100

* 欸 H0w 哥，base64 是什麼壓
* 哼 阿明，你連貝斯 64 都不知道 就讓我來教教你吧
* 喔白癡喔，不是那個貝斯啦
* 好啦其實我知道就是這個

* [base64](reverseLevel2/file/base64)

Note:
* ELF 64-bit LSB shared object

---

## 林思辰_base64 心得
* 用很髒的解法解的, 應該不是原本的作法.
  * strings
  * base64
  * hex-to-ascii

Note:
* cHVzaCAweDdkMjEyMTIxCnB1c2ggMHg0NzZlNjk1MgpwdXNoIDB4NzQ1MzVmNjMKcHVzaCAweDMxNDczNDZkCnB1c2ggMHg1ZjQ0NmU2YwpwdXNoIDB4NDY1ZjU1MzAKcHVzaCAweDU5N2I0NjU0CnB1c2ggMHg0Mzc0NzM3MgpwdXNoIDB4Njk0Njc5NGQK
* [Hex to ASCII text converter](https://www.rapidtables.com/convert/number/hex-to-ascii.html)
* [Reverse a string](http://string-functions.com/reverse.aspx)

---

## 林思辰_encrypt
### 100

* 小美，妳看這不是古羅馬嗎
* 難不成我們穿越回到古代了嗎
* 好像是喔，妳看那個人長的是不是很像凱薩阿
* 好帥喔 OwO

* 找出加密的方法並解密一個特別的字串

* [encrypt](reverseLevel2/file/encrypt)

Note:
* ELF 64-bit LSB shared object

---

## 林思辰_encrypt 心得
* 用很髒的解法解的, 可能不是原本的作法.
  * strings
  * exec, find rule.
  * decrypt

Note:
* zGs7@ABp"sIp/3bn@-:A-G]CllNNK
* shift, 0x1f < char < 0x7f
* [Caesar Cipher](https://www.dcode.fr/caesar-cipher)

---

## 林思辰_encode
### 100

* 欸阿明，你知道怎麼把英文字母轉成數字嗎
* 就是把 ABC 變成 123 壓
* 喔喔很簡單啊
* 難道阿明知道 flag ????!!!!
* Note : 將解出的字串放入 MyFirstCTF{} 中，若為數字則以十六進制表示 0x 開頭

* 試著找出編碼的方法

* [encode](reverseLevel2/file/encode)

Note:
* ELF 64-bit LSB shared object

---

## 林思辰_encode 心得
* 需要好好讀 code 的題目.
* %, mod.
* 開頭的 A 要去掉.

Note:
* 要學習從 gdb 去了解, F5大絕招

---

# The End
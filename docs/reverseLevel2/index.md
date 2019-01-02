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

# The End
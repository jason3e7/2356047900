### 第一次練習
# reverseLevel2
### 就上手

jason3e7 20190107

Note:title:"第一次練習 reverseLevel2 就上手"

---

## 陳廷宇_XorZero
### 100

* [Encrypted](reverseLevel2/file/Encrypted)

---

## 陳廷宇_XorZero 心得
* text 檔案要怎麼解碼.
* [XOR cipher](https://www.wikiwand.com/en/XOR_cipher)
* 要花時間思考一下, 自己要怎麼撰寫 encrypt, decrypt 程式.

Note:
* [XOR Cracker](https://wiremask.eu/tools/xor-cracker/)
  * ELF 64-bit LSB executable
* text 檔案要怎麼解碼, 其他題目也會遇到, 要思考怎麼思考.
  * file analysis
    * exec analysis
* XOR cipher, 大部分是文字加解密.
  * [xortool](https://github.com/hellman/xortool)
  * [Xortool](https://www.aldeid.com/wiki/Xortool)
  * [XORSearch](https://blog.didierstevens.com/programs/xorsearch/)
  * [XOR Files With Python](https://www.megabeets.net/xor-files-python/)
  * [XOR Cipher](https://www.dcode.fr/xor-cipher)
  * [XOR Online Encrypt & Decrypt](https://md5decrypt.net/en/Xor/)
  * [XOR Decryptor](https://www.browserling.com/tools/xor-decrypt)
* [Nowhere to Hide: Three methods of XOR obfuscation](https://blog.malwarebytes.com/threat-analysis/2013/05/nowhere-to-hide-three-methods-of-xor-obfuscation/), 好像是不錯的文章, 有空可以看看.

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

## 林思辰_mutate
### 100

* H0w 哥，你知道邏輯設計嗎
* 喔喔我知道阿 就那個 and or not 還有一個什麼的 我忘了
* 哈哈不知道齁 笑你

* 試著找出 mutate 字串的方法

* [mutate](reverseLevel2/file/mutate)

Note:
* ELF 64-bit LSB shared object

---

## 林思辰_mutate 心得
* 需要好好讀 code 的題目.
* `(i + 32) ^ byte_201120[i]) != *((_DWORD *)&off_201020 + i)`
* 手動解會比較慢, 要寫程式解比較快.

Note:
* 要學習從 gdb 去了解, F5大絕招

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
```
num = 0
num = x[i] + 26 * num
```

---

# The End
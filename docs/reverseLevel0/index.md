### 第一次練習
# reverseLevel0
### 就上手

jason3e7 20190101

Note:title:"第一次練習 reverseLevel0 就上手"

---

## EasyCTF_hexedit
### 25

* flag 格式為 easyctf{...}

* [hexedit](reverseLevel0/file/hexedit)

Note:
* strings 就有答案了
  * `strings hexedit | grep ctf`

有很多 hex 的編輯器可以用
* vim
* notepad++
* sublime text

---

## EasyCTF_Hexable
### 25

* flag 格式為 easyctf{...}

* [hexable](reverseLevel0/file/hexable)

Note:
* strings 就有答案了
  * `strings hexedit | grep ctf`
* 不知道和上一題的差異是什麼 !?

---

## CSIE_strace
### 25

* flag 格式為 FLAG{...}

* [strace](reverseLevel0/file/strace)

Note:
* [strace](http://man7.org/linux/man-pages/man1/strace.1.html)
* linux cmd, file, 基本判斷這個檔案是什麼

---

## CSIE_strace 心得
* file ./starce
  * `./strace: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), statically linked, for GNU/Linux 2.6.32, BuildID[sha1]=5d905db040e676a3979ba0f3afaa101acb5e37a6, stripped`
* ./strace
  * `find the flag in system call!`
* strace ./strace

Note:
* [strace](https://linuxtools-rst.readthedocs.io/zh_CN/latest/tool/strace.html)
* strace, 可以做什麼
  * strsize
* 這個題目是怎麼寫出來的

---

# The End
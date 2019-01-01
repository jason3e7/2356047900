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

## EasyCTF_adder
### 25

* ﬂag 格式為 easyctf{...}

* [adder](reverseLevel0/file/adder)

Note:
* ELF 64-bit LSB executable

---

## EasyCTF_adder 心得
* ./adder
  * `Enter three numbers!`
* objdump
  * main

Note:
* `objdump -d -M intel --no-show-raw-insn`
  * `cmp  eax,0x539`

---

## EasyCTF_LuckyGuess
### 25

* flag 格式為 easyctf{...}

* [LuckyGuess](reverseLevel0/file/LuckyGuess)

Note:
* ELF 64-bit LSB executable

---

## EasyCTF_LuckyGuess 心得
* objdump
``` 
400b8d:	cmp    eax,DWORD PTR [rbp-0x94]
400b93:	jne    400bf3 <main+0xfb>
```
* gdb, 在執行中 show rbp-0x94

Note:有參考IDA
* gdb 操作要整個在另外一篇
  * b main
  * r
  * ni
  * `p *(int *)($rbp-0x94)`
  * n
* [如何使用 GDB Debug](https://www.puritys.me/docs-blog/article-329-%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8-GDB-Debug.html)
* [How to print -0x4(%rbp) in gdb?](https://stackoverflow.com/questions/5455832/how-to-print-0x4rbp-in-gdb)

---

## picoCTF2017_Coffee
### 25

* flag 格式為 flag_{...}

* [Coffee.class](reverseLevel0/file/Coffee.class)

Note:
* compiled Java class data

---

## picoCTF2017_Coffee 心得
* [Command line Java Decompiler](https://github.com/kwart/jd-cmd)
  * [jd-cli](reverseLevel0/file/jd-cli-0.9.2-dist.zip) 
* copy code
* fix code
* javac
* java

Note:
* problem.java

---

## EasyCTF_liar
### 25

* flag 格式為 easyctf{...}

* [liar](reverseLevel0/file/liar)

Note:
* ELF 64-bit LSB shared object
* [Linux 執行時尋找 symbol 的流程以及 shared library 相關知識](https://medium.com/fcamels-notes/linux-%E5%9F%B7%E8%A1%8C%E6%99%82%E5%B0%8B%E6%89%BE-symbol-%E7%9A%84%E6%B5%81%E7%A8%8B%E4%BB%A5%E5%8F%8A-shared-library-%E7%9B%B8%E9%97%9C%E7%9F%A5%E8%AD%98-b0cf1e19cbf3)

---

## EasyCTF_liar 心得
* the flag is %s

---

# The End
### 第一次練習
# reverseLevel1
### 就上手

jason3e7 20190103

Note:title:"第一次練習 reverseLevel1 就上手"

---

## Reverse
### 50

* 程式開發是許多資訊人員必備的技術，但開發安全的程式更是極度欠缺高階程式師。 一般程式可能被逆向工程技術破解，請利用你所知道的逆向工程技術破解以下程式。

* 提示1:此題有多種方法破解，你可以嘗試看看
* 提示2:可利用一般debugger工具輕鬆找出flag

* [reverse](reverseLevel1/file/reverse)

Note:
* strings 就有答案了
  * `strings reverse | grep CTF`

---

## 陳廷宇_Baby_Assembly
### 50

* [BabyAssembly.exe](reverseLevel1/file/BabyAssembly.exe)

Note:
* PE32 executable for MS Windows (console) Intel 80386 32-bit

---

## 陳廷宇_Baby_Assembly 心得
* 大部分問題都在處理 VCRUNTIME140D.DLL
  * 放在和執行檔同一層
* code review
  * open file

Note:
* [THE ONE-CLICK FIX FOR DLL ERRORS](https://www.dll-files.com/)
* 還好這次只有兩個 dll, 其他的 case 是不是直接安裝 Visual Studio, 比較快解決問題.
  * vcruntime140d.dll
  * ucrtbased.dll

---

## 林思辰_find
### 50

* 阿明，你看看我撿到的神祕檔案
* 滾啦
* 嗚嗚...嗚...
* 傷心的 H0w 哥獨自一人打開了檔案
* 突然有一個聲音說道
* 找出 flag 吧！ H0w 哥

* strings 是個好用的工具

* [find](reverseLevel1/file/find)

Note:
* strings 就有答案了
  * `strings find | egrep 'MyFirstCTF{[a-zA-Z0-9_]+}'`
* [三分鐘教你輕鬆掌握 grep 命令中的正則表達式](https://linuxstory.org/grep-regular-expressions/)
* [Regular Expressions In grep examples](https://www.cyberciti.biz/faq/grep-regular-expressions/)
* [Searching Files on UNIX](http://www.robelle.com/smugbook/regexpr.html)
* [Linux的正則表達式grep,egrep](https://kknews.cc/zh-tw/other/g8o22ne.html)

---

## 林思辰_read-asm
### 50

* 「在 _start 中 call foo (line 32) 後 rax 的值為何？」
* Note : 將解出的字串放入 MyFirstCTF{} 中，若為數字則以十六進制表示 0x 開頭
* 可以試著編譯完再用 gdb 觀察
* [read-asm.asm](reverseLevel1/file/read-asm.asm)

Note:
```
欸阿明，你在幹嘛
喔我在讀組合語言壓
齁那個又不會考讀X喔
可...可是自從我讀了之後考試都考 100 分欸
像是老師出的這題
「在 _start 中 call foo (line 32) 後 rax 的值為何？」
花了我 0.0001 秒就答完惹，然後帥氣地轉身離開了呢
```

---

## 林思辰_read-asm 心得
* 可以以用 objdump, 觀察各階段產出的狀態
* ld, The GNU linker
  * -s, Omit all symbol information from the output file.
* gdb
  * `b *_start`
    * `b *0x4000f5` 
  * `disas *_start`
  * `ni`, `si`
  * `info all-registers`

Note:
* uname -a
  * `Linux ubuntu 4.15.0-43-generic #46~16.04.1-Ubuntu SMP Fri Dec 7 13:31:08 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux`
* `nasm -f elf64 run-asm.asm`, 加上 -g 好像沒什麼差, 使用 objdump, 可以看到完整的程式碼.
* `ld -s -o read-asm read-asm.o && ./read-asm`, 使用 objdump, \_start 不見了.
  * Segmentation fault (core dumped)
* `ld -o read-asm read-asm.o && ./read-asm`, 使用 objdump, 程式碼都在.
  * nothing

---

## 林思辰_read-asm tools
* [Using gdb for Assembly Language Debugging](https://www.cs.umb.edu/~cheungr/cs341/Using_gdb_for_Assembly.pdf)
* [GNU 的連結工具 (ld, nm, objdump, ar)](http://sp1.wikidot.com/gnulinker)
* [Linker Script初探 - GNU Linker Ld手冊略讀](http://wen00072.github.io/blog/2014/03/14/study-on-the-linker-script/)
* [[心得] 個人的 x86 組合語言觀念筆記](https://www.ptt.cc/bbs/ASM/M.1286960542.A.5B9.html)
* [A quick primer for those who prefer to use a command line debugger.](http://ece-research.unm.edu/jimp/310/nasm/gdb.pdf), gcc 那一段會失敗.
* [計算機體系結構與NASM入門](https://www.smwenku.com/a/5b859fe02b71775d1cd36868/), 看了這段有 ld -s, 卡了一小段時間.

Note:
* [How to debug NASM Assembly that produces segfault before hitting _start](https://stackoverflow.com/questions/47357224/how-to-debug-nasm-assembly-that-produces-segfault-before-hitting-start), 奇特的技巧.

---

## 林思辰_run-asm
### 50

* 跑跑跑向前跑
* 阿...阿呃
* H0w 哥你怎麼了
* 我...我...我快不行了，跑完 asm 這項重責大任就交給你了

* 編譯 asm 檔案並執行

* [run-asm.asm](reverseLevel1/file/run-asm.asm)

---

## 林思辰_run-asm 心得
* analysis code
  * `global _star`, nasm
  * `mov rax, 1`, elf64

Note:
* [What is global _start in assembly language?](https://stackoverflow.com/questions/17898989/what-is-global-start-in-assembly-language)
* uname -a
  * `Linux ubuntu 4.15.0-43-generic #46~16.04.1-Ubuntu SMP Fri Dec 7 13:31:08 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux`
* `nasm -f elf64 run-asm.asm`
* `ld -s -o run-asm run-asm.o`
* `./run-asm`

---

## 林思辰_run-asm nasm
* [NASM Hello World for x86 and x86_64 Intel Mac OS X (get yourself an updated nasm with brew)](https://gist.github.com/FiloSottile/7125822)
* [Hello, world!](http://asm.sourceforge.net/intro/hello.html)
* [x86_64 NASM Assembly Quick Reference ("Cheat Sheet")](https://www.cs.uaf.edu/2017/fall/cs301/reference/x86_64.html)
* online compile
  * [compile nasm online](https://rextester.com/l/nasm_online_compiler)
  * [Assembler - NASM](https://www.jdoodle.com/compile-assembler-nasm-online)
  * [godbolt](https://godbolt.org/)

Note:
* [8.20 How to get GCC to generate assembly code](http://www.delorie.com/djgpp/v2faq/faq8_20.html)

---

# The End
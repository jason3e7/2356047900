### 第一次練習
# reverseLevel1
### 就上手

jason3e7 20190102

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

# The End
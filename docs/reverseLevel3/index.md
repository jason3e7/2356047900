### 第一次練習
# reverseLevel3
### 就上手

jason3e7 20190109

Note:title:"第一次練習 reverseLevel3 就上手"

---

## AIS3_Pre_exam_2016-Binary1
### 150

* [binary1](reverseLevel3/file/binary1)

---

## AIS3_Pre_exam_2016-Binary1 心得
* 需要好好讀 code 的題目.
* `if ( encrypted[i] != ((unsigned __int8)((i ^ *(unsigned __int8 *)(i + a1)) << ((i ^ 9) & 3)) | (unsigned __int8)((i ^ *(unsigned __int8 *)(i + a1)) >> (8 - ((i ^ 9) & 3)))) + 8 )`
* 手動解會比較慢, 要寫程式解比較快.

Note:
* 要學習從 gdb 去了解, F5大絕招

---

## AIS3_Pre_exam_2015-Bin2
### 150

* [bin2.txt](reverseLevel3/file/bin2.txt)

---

## 陳廷宇_Equation
### 150

* [Equation](reverseLevel3/file/Equation)

---

## 陳廷宇_Equation 心得
* 需要好好讀 code 的題目.
```
for ( i = 0; i <= 3; ++i )
    *(&v11 + i) = *(_DWORD *)&v31[4 * i];
for ( j = 0; j <= 3; ++j )
    *(&v15 + j) -= v11 + (v12 & (unsigned int)~(255 << 8 * j));
for ( k = 0; k <= 3; ++k )
    *(&v15 + k + 4) -= v12 + (v11 & (unsigned int)~(255 << 8 * k));
for ( l = 0; l <= 3; ++l )
    *(&v15 + l + 8) -= v13 + (v14 & (unsigned int)~(255 << 8 * l));
for ( m = 0; m <= 3; ++m )
    *(&v15 + m + 12) -= v14 + (v13 & (unsigned int)~(255 << 8 * m));
v9 = 0;
for ( n = 0; n <= 15; ++n )
    v9 |= *(&v15 + n);
if ( !v9 )
    printf("MyFirstCTF{%s}", v31);
```

Note:
* 要學習從 gdb 去了解, F5大絕招
* [C Operator Precedence](https://en.cppreference.com/w/c/language/operator_precedence)
  * `255 << 8 \* x`
  * `255 << (8 \* m)`
* hex to ascii, 建議不要自行 decode, 有可能會看錯.

---

## 陳廷宇_TableNChair
### 150

* [TableNChair](reverseLevel3/file/TableNChair)

---

## 陳廷宇_TableNChair 心得
* 需要好好讀 code 的題目.
```
__int64 __fastcall sub_4006F6(unsigned int a1)
{
  __int64 result; // rax
  signed int i; // [rsp+10h] [rbp-4h]

  result = a1;
  for ( i = 0; i <= 758; i += 2 )
  {
    result = (unsigned __int8)byte_601080[i];
    if ( (_BYTE)result == (_BYTE)a1 )
      return (unsigned __int8)byte_601080[i + 1];
  }
  return result;
}
```

Note:
* 要學習從 gdb 去了解, F5大絕招
* find s1, byte_601080

---

# The End
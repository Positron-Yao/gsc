# 原神自动弹琴编译器

将按照给定格式写的曲谱文件(.sc~~(.txt)~~)编译成AutoHotkey文件(~~也算是编译(?)~~).

后面交给万能的AHK力.

### 曲谱格式

第一行第一位是模式，有sequenced和timed两种.

- sequenced: 序列模式，只描述音符序列，不写长度，用于琴.
- timed: 计时模式，需加上音符时长，用于圆号.

第二位是每两个音符的最小间隔，可以直接写数字或写成 60000/x.

之后的部分为乐谱主体，音符之间由 **/** 分隔，音符范围为 **c3~b5** (原琴音域)，同一时刻演奏多个音符直接用空格分隔，空行、换行、多余的空格会被忽略。注释写在 **/\* ... \*/** 之间，单行注释为 #.

### 编译

```powershell
python gsc.py ***.sc
:: 或
gsc.exe ***.sc
```

输出文件名自动为 输入文件 + ".ahk"

### 乐谱示例

``` gsc
sequenced 160
/* 结束乐队，启动! */
c5/b4/a4/b4/0/g4/0/e4/0/c5/0/b4/0/0/b4/0/
```

```gsc
timed 60000/160
/* 芙芙~ */
a53///g52//f51/e54////a41/b41/
c51/d51/e51/d51/c51/a41/c53///b43///
```
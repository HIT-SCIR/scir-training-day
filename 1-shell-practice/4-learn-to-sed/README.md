学习Sed
=======

推荐阅读
-------

* [sed学习笔记](http://www.centos.bz/2012/07/sed-notes/)

题目
----

请使用sed完成下列任务。当然，你也可以使用之前的shell命令（比如awk、grep）与sed配合。

Quize 1
-------

**任务** 去掉文件中的空行

**数据**[1.dat](https://github.com/Oneplus/scir-training-day/blob/master/1-shell-practice/4-learn-to-sed/1.dat)

Quiz 2
------

**任务**某个文件包含三列，第三列是文本，但是文本被`'`扩了起来，请用提取出这一列并去掉开头和结尾的`'`符号。

**数据**[2.dat](https://github.com/Oneplus/scir-training-day/blob/master/1-shell-practice/4-learn-to-sed/2.dat)

Quiz 3 Sed批量去拓展名
----------------------

**任务**现在有如下文件
```
dev.gb.conll06.raw
test.gb.conll06.raw
train.gb.conll06.raw
```
请用sed和for配合，将文件名的后缀.raw去掉

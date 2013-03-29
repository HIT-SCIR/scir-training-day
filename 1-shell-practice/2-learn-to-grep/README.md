学习Grep
========

推荐阅读
--------

* [Grep笔记](http://man.chinaunix.net/newsoft/grep/open.htm)

题目
----
你需要用grep脚本(或者用grep和其他shell命令配合)实现如下一些功能

Quiz 1
------

**任务** 请完成脚本`1.sh`，统计文件中的空行个数并输出

**数据** [1.dat](https://github.com/Oneplus/scir-training-day/blob/master/1-shell-practice/2-learn-to-grep/1.dat)

**测试命令**
```
sh 1.sh 
```

Quiz 2
------
**任务** 请完成脚本`2.sh`，统计文件中不包含".txt"的行的行数并输出

**数据** [2.dat](https://github.com/Oneplus/scir-training-day/blob/master/1-shell-practice/2-learn-to-grep/2.dat)

**测试命令**
```
sh 2.sh
```

Quiz 3
------
**任务** 请完成脚本`3.sh`，求两个文件的差集(3a.txt-3b.txt)并排序输出到标准io中

**数据** [3a.dat](https://github.com/Oneplus/scir-training-day/blob/master/1-shell-practice/2-learn-to-grep/3a.dat),[3b.dat](https://github.com/Oneplus/scir-training-day/blob/master/1-shell-practice/2-learn-to-grep/3b.dat)

**测试命令**
```
sh 3.sh
```

Quiz 4
------
**任务** 在log文件中，有表示各轮迭代模型性能的报告（如下所示），
```
Total:      P=0.97198463(7841/8067) R=0.97914585(7841/8008) F=0.97555210
```
请将他们提取出来，并以如下格式输出。

```
P=0.97 R=0.98 F=0.98
```

**数据** [4.dat](https://github.com/Oneplus/scir-training-day/blob/master/1-shell-practice/2-learn-to-grep/4.dat)

**测试命令**
```
sh 4.sh
```

学习Grep
========

首先推荐阅读一篇有关Grep的入门[文章](http://man.chinaunix.net/newsoft/grep/open.htm)，然后你需要用grep脚本(或者用grep和其他shell命令配合)实现如下一些功能

1. 统计文件中的空行个数，[数据1.dat](https://github.com/Oneplus/scir-training-day/blob/master/1-shell-practice/2-learn-to-grep/1.dat)
2. 统计文件中不包含".txt"的行的行数，[数据2.dat](https://github.com/Oneplus/scir-training-day/blob/master/1-shell-practice/2-learn-to-grep/2.dat)
3. 求两个文件的差集，[数据3a.dat](https://github.com/Oneplus/scir-training-day/blob/master/1-shell-practice/2-learn-to-grep/3a.dat),[数据3b.dat](https://github.com/Oneplus/scir-training-day/blob/master/1-shell-practice/2-learn-to-grep/3b.dat)
4. 在log文件中，有表示各轮迭代模型性能的报告（如下所示），请将他们提取出来，[数据4.dat](https://github.com/Oneplus/scir-training-day/blob/master/1-shell-practice/2-learn-to-grep/4.dat)

```
Total:      P=0.97198463(7841/8067) R=0.97914585(7841/8008) F=0.97555210
```

Linux Shell入门
===============

推荐阅读
-------

* [Learn UNIX in 10 minutes](http://freeengineer.org/learnUNIXin10minutes.html)

实用命令
-------

1. ctrl+r
2. cut, paste, tr, wc, grep, sort, uniq, find
3. vimdiff -O
4. screen
5. ps, killall -9, top
6. iconv
7. du -sch * | sort -n, df -h
8. tail -f

题目
----

###1 一个接受命令行参数的shell脚本

编写一个shell脚本a.sh，这个脚本接受一个命令行参数，并把这个参数打印两次到标准输出。
如果输入没有参数输入，输出"error"。

样例
1.
```
./a.sh hello
hello
```

2.
```
./a.sh
error
```

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
9. time

Quiz 1 一个接受命令行参数的shell脚本
------------------------------------

**任务** 编写一个shell脚本1.sh，这个脚本接受一个命令行参数，并把这个参数打印两次到标准输出。
如果输入没有参数输入或者有多于一个参数输入，输出"error"。

样例 1.
```
./1.sh hello
hellohello
```

样例 2.
```
./1.sh
error
```

**运行命令**
```
sh 1.sh [ARGUMENT]
```

Quiz 2 生成时间相关文件夹
------------------------

**任务** 编写一个shell脚本2.sh，无论脚本在任何位置用绝对路径执行都能完成这样的任务，在脚本2.sh所在目录新建一个空文件tmp_YYYYMMDD YYYYMMDD为当前日期

**运行命令**
命令：

```
sh src/2.sh; ls src
```

输出：

```
2.sh tmp_20130329
```


学习Uniq和Sort
==============


Quiz 1
------
Find out the most frequency 100 queries from the query log

有用户日志文件，每行记录了一个用户查询串，长度为1-255字节，共1千万行，请排出查询最多的前100条。

Quiz 2
------
**任务** 根据词在文档中出现的频率从高到低对词进行排序

**数据** 文档中每行一个句子，句子分好词，词与词之间使用\t断开。

**提示**
* 使用uniq -c 可以统计词频
* 使用sort -k <column>可以指定对输入按照第<column>列进行排序
* 使用sort -n 可以指定采用数值方法进行排序
* 使用sort -r 可以指定逆序排序
* 使用sed将空格替换为\n

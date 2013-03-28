最大正向匹配算法
================

题目描述
--------

最大正向匹配算法是一种非常基础的中文分词算法。
关于算法如何运行，可以参考[这篇](http://www.52nlp.cn/maximum-matching-method-of-chinese-word-segmentation)文章。
现在，请用python实现一个最大正向匹配中文分词算法的脚本。
脚本接受两个参数，一个是输入文件的路径，另一个是词典的路径。
请注意，词典已经使用cPickle库进行了 _序列化_，`dic`加载进来后是一个字符串的`set`
程序结构已经在max-match.py中实现，你只需要实现`max_match_segment( line, dic )`这个函数。

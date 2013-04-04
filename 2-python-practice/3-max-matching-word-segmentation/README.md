最大正向匹配算法
================

阅读资料
--------

* [数学之美系列二 谈谈中文分词](http://product.dangdang.com/product.aspx?product_id=22754640)
* [漫话中文自动分词和语义识别（上）：中文分词算法](http://www.matrix67.com/blog/archives/4212)
* [中文分词入门之最大匹配法](http://www.52nlp.cn/maximum-matching-method-of-chinese-word-segmentation)

题目描述
--------

最大正向匹配算法是一种非常基础的中文分词算法。
关于算法如何运行，阅读资料中已经写得相当清楚了=)

现在，请用python实现一个最大正向匹配中文分词算法的脚本。
脚本接受两个参数，一个是输入文件的路径，另一个是词典的路径。

它的运行方法如下：

```
python max-match.py <data> <dict>
```

---

请注意
* 词典已经使用cPickle库进行了 _序列化_，`dic`加载进来后是一个字符串的`set`
* 程序结构已经在max-match.py中实现，你只需要实现`max_match_segment( line, dic )`这个函数。

---

自动测试
--------

### 生成词典

build-dict.py是一个生成字典（序列化）的脚本，项目中提供了一个1000行的分好词的语料train.dat。
你可以使用如下命令生成一个字典。

```
python build-dict.py train.dat vocab.bin 
```

同时，项目中提供了一个更大的字典vocab.large.bin。
用`gunzip vocab.large.bin.gz`解压后就可以使用。
也可以使用这个字典试一试效果。

### 测试

---

确保你使用了`git submodule init`命令获得了py-corpusproc这个项目

---

假设你的分词结果存储在output.dat中
你可以使用如下命令来测试你的分词结果的准确率。

```
python eval.py --format=segment --mode=segment --eval=output.dat --gold=eval.dat
```
可以看到
```
1906    3478    2594    54.80161012%    73.47725520%    62.77997365%
```
这些输出结果表示
```
正确切分的词的个数 输出词个数 正确词个数 P值 R值 F值
```
这些数值是如何评价的，可以自行搜索。

如果使用小词典，可以达到62%的F值，使用大字典，可以达到94%的F值

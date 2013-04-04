训练日
=====

简介
----
我们想通过这样一个项目，给新进实验室的同学提供一些简单的和自然语言处理相关的Linux命令，脚本的训练。
希望做题的同时，能够掌握一些基础的shell和脚本，同时又能对数据有一定的认识，同时能够接触一些nlp的基础问题。

现在，我们的大部分题目集中在shell和python的使用，未来可能会加入一些其他语言的练习。
当然，未来，我们也希望程序用程序自动完成判题。

内容
----

### 参考资源

* 自然语言处理相关参考书和在线课程

### shell练习

1. [shell基础练习](https://github.com/Oneplus/scir-training-day/tree/master/1-shell-practice/1-fundamental-of-shell)
2. [grep练习](https://github.com/Oneplus/scir-training-day/tree/master/1-shell-practice/2-learn-to-grep)
3. [awk练习](https://github.com/Oneplus/scir-training-day/tree/master/1-shell-practice/3-learn-to-awk)
4. [sed练习](https://github.com/Oneplus/scir-training-day/tree/master/1-shell-practice/4-learn-to-sed)
5. [sort练习](https://github.com/Oneplus/scir-training-day/tree/master/1-shell-practice/5-sort)

### python练习

1. [BI标注词序列转换](https://github.com/Oneplus/scir-training-day/tree/master/2-python-practice/1-bi-label-to-words)
2. [NGram统计](https://github.com/Oneplus/scir-training-day/tree/master/2-python-practice/2-ngram-count)
3. [正向最大匹配分词](https://github.com/Oneplus/scir-training-day/tree/master/2-python-practice/3-max-matching-word-segmentation)
4. [HMM词性标注](https://github.com/Oneplus/scir-training-day/tree/master/2-python-practice/4-hmm)
5. NumPy向量处理与SciPy稀疏矩阵(sparse matrix)操作

用法
----

### 使用Git

首先需要将训练题下载下来，这个过程中，可能需要一些git的知识。
具体来讲，你需要做如下几件事：

1. 下载一个和自己的操作系统相符的git
2. 注册一个github账号
3. 将这个项目fork到自己的账户下
4. 将项目clone到本地

然后开始做题吧！

---

* 用10分钟了解一下[git简易指南](http://rogerdudler.github.com/git-guide/index.zh.html)，磨刀不误砍柴工。

---

### 例题

举shell练习中的第一题为例，来说明应该如何做题。

首先，题目写在对应文件夹的README.md中。这道题要写

> 编写一个shell脚本1.sh，这个脚本接受一个命令行参数，并把这个参数打印两次到标准输出。 如果输入没有参数输入或者有多于一个参数输入，输出"error"。

我们可以编写一个脚本1.sh

```
if [ $# != 1 ] ; then 
  echo "error"
else
	echo $1$1
fi
```

然后，为了验证程序的正确性，可以运行自动测试脚本run.py进行测试。由于脚本调用1.sh文件，所以为了使用自动评测文件名一定要正确命名。

看到运行结果

```
Test  0
=======
+ RUNNING
 -- sh 1.sh yes
+ RESULT
 -- Passed!

Test  1
=======
+ RUNNING
 -- sh 1.sh
+ RESULT
 -- Passed!

2 Runs, 2 Pass
```

表明进行了两个测试，并且都通过了。

保持更新
--------
由于题目、数据都会不断更新，所以使用者应该注意与原项目保持更新。

具体做法可以参考有如下两种。

### 被动更新

在题目、数据获得更新之后，我们会主动向使用者发起pull request。使用者可以通过merge主干来保持更新。
所以需要注意一点，尽量不要在自己的项目中修改题目，以免更新题目时产生不必要的冲突。

### 主动更新

除了接受Pull Request，Fork这一项目的用户还可以通过fetch的方式主动与原项目保持一致。
具体做法可以参考以下链接。

* [Fork A Repo · github:help](https://help.github.com/articles/fork-a-repo)

自动评测(开发者)
----------------
现在已经实现了一些自动评测的功能，其中包括

* stdout与制定字符串对比 
* stdout与文件对比

计划是可以做成像[这个](https://github.com/Oneplus/scir-training-day/blob/master/1-shell-practice/1-fundamental-of-shell/run.py)这样，这部分还在完善。

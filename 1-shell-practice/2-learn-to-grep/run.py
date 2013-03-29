#!/usr/bin/env python

import sys, os

try:
    from judge import Judge
    from judge import STDIO, FILE
except:
    path = os.path.realpath(__file__)
    path = os.path.split(path)[0]
    path = os.path.join(path, "..")
    path = os.path.join(path, "..")
    sys.path.append(path)
    from judge import Judge
    from judge import STDIO, FILE

if __name__=="__main__":
    judge = Judge()
    judge.add_test(["sh", "1.sh",], "11",       style=STDIO)
    judge.add_test(["sh", "2.sh",], "17",       style=STDIO)
    judge.add_test(["sh", "3.sh",], "b\ne",     style=STDIO)
    judge.add_test(["sh", "4.sh",], "4.out",    style=FILE)
    judge.run()

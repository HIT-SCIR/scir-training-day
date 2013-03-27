#!/usr/bin/env python

import sys, os

try:
    from judge import Judge
except:
    path = os.path.realpath(__file__)
    path = os.path.split(path)[0]
    path = os.path.join(path, "..")
    path = os.path.join(path, "..")
    sys.path.append(path)
    from judge import Judge

if __name__=="__main__":
    judge = Judge()
    judge.add_test(["sh", "a.sh", "yes"], "yesyes", style="I")
    judge.run()

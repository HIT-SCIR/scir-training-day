from timeout_command import TimeoutCommand
from random import sample
from string import lowercase 

import filecmp
import os

STDIO = 0
FILE  = 1

class Judge(object):

    def __init__(self):
        self.tests = []

    def add_test(self, args, expected, timelimit=None, style=0):
        self.tests.append( {
            "args":         args,
            "expected" :    expected,
            "timelimit" :   timelimit,
            "type" :        style} )

    def run(self):
        corr = 0
        for i, test in enumerate(self.tests):
            print "Test %2d\n=======" % i
            cmd = "+ RUNNING\n -- %s" % " ".join(test["args"])
            print cmd
            if test["type"] == STDIO:
                corr += self._run_io_check( test )
            elif test["type"] == FILE:
                corr += self._run_file_diff( test )

            print

        print "%d Runs, %d Pass" % (i + 1, corr)

    def _run_io_check(self, test):
        p = TimeoutCommand( test["args"], test["timelimit"] ).exe()
        out = p.stdout.read().strip()

        result = ""
        if out == test["expected"]:
            result = "+ RESULT\n -- Passed!"
            ret = 1
        else:
            err = p.stderr.read().strip()
            result = "+ RESULT\n -- Failed!\n"
            result += "+ STDERR OUTPUT\n"
            result += "\n".join([" -- %s" % l for l in err.split("\n")])
            ret = 0

        print result
        return ret

    def _run_file_diff(self, test):
        p = TimeoutCommand( test["args"], test["timelimit"] ).exe()
        filename = sample(lowercase, 8)
        filename = "".join(filename)
        try:
            fp=open(filename, "w")
        except:
            return 0

        print >> fp, p.stdout.read()
        fp.close()

        if filecmp.cmp(test["expected"], filename):
            result = "+ RESULT\n -- Passed!"
            ret = 1
        else:
            err = p.stderr.read().strip()
            result = "+ RESULT\n -- Failed!\n"
            result += "+ STDERR OUTPUT\n"
            result += "\n".join([" -- %s" % l for l in err.split("\n")])
            ret = 0

        os.remove(filename)
        print result
        return ret

if __name__=="__main__":
    from sys import stderr
    print >> stderr, "library is not runnable"

from timeout_command import TimeoutCommand

class Judge(object):

    def __init__(self):
        self.tests = []

    def add_test(self, args, expected, timelimit=None, style="I"):
        self.tests.append( {
            "args":         args,
            "expected" :    expected,
            "timelimit" :   timelimit,
            "type" :        style} )

    def run(self):
        for i, test in enumerate(self.tests):
            if test["type"] == "I":
                self._run_io_check( test )
            elif test["type"] == "F":
                self._run_file_diff( test )

    def _run_io_check(self, test):
        out = TimeoutCommand( test["args"], test["timelimit"] ).exe()
		
		if out == self.expected:
			print "bingo!"
		else:
			print "failed!"

    def _run_file_diff(self, test):
        TimeoutCommand( test["args"], test["timelimit"] ).exe()

if __name__=="__main__":
	from sys import stderr
	print >> stderr, "library is not runnable"
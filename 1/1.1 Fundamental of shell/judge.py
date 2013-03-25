import sys

try:
	import judge
except:
	sys.path.append("../../../")
	import judge
	

if __name__=="__main__":
	judge = Judge()
	judge.add_test(["sh", "yes"], "yesyes", style="I")
	judge.run()
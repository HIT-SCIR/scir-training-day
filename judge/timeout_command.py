import threading
import subprocess

class TimeoutCommand(threading.Thread):
    def __init__(self, args, timeout = None):
        threading.Thread.__init__(self)
        self.args    = args
        self.timeout = timeout

    def run(self):
        self.p = subprocess.Popen(self.args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.p.wait()

    def exe(self):
        self.start()
        self.join(self.timeout)

        if self.is_alive():
            self.p.terminate()
            self.join()
        
        return self.p
            
if __name__=="__main__":
    import stderr
    print >> stderr, "library is not runnable"

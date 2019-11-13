import threading
import time
  
class MyThead(threading.Thread):
    "继承式多线程"
    def __init__(self,n,sleep_time):
        super(MyThead,self).__init__()
        self.n = n
        self.sleep_time = sleep_time
  
    def run(self):
        "这个方法不能叫别的名字，只能叫run方法"
        print("runinit task",self.n)
        time.sleep(self.sleep_time)
  
t1 = MyThead("t1", 2)
t2 = MyThead("t2", 4)
  
t1.start()
# t1.join()   #等待t1线程的执行结果，相当于于其他语言里面的 t1.wait()
t2.start()

t1.join()
print("main thread....")

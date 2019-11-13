import threading
import time

class MyThread(threading.Thread):   # 继承threading.Thread
    """继承式多线程"""
    def __init__(self, n):
        threading.Thread.__init__(self)  # 也可以写成这样super(MyThread,self).__init__()
        self.n = n
 
    def run(self):     # 重写run方法
        """这个方法不能叫别的名字，只能叫run方法"""
        print("run", self.n)
        time.sleep(2)
  
t1 = MyThread("t1")   # 实例化
t2 = MyThread("t2")
  
t1.start()   # 启动一个多线程
t2.start()
import threading
import time
 
 
def run(n):
    lock.acquire()  # 添加线程锁
    global num   # 把num变成全局变量
    time.sleep(0.1)  # 注意了sleep的时候是不占有cpu的，这个时候cpu直接把这个线程挂起了，此时cpu去干别的事情去了
    num += 1   # 所有的线程都做+1操作
    lock.release()  # 释放线程锁
 
 
num = 0   # 初始化num为0
lock = threading.Lock()  # 生成线程锁实例
t_obj = list()
for i in range(10):
    t = threading.Thread(target=run, args=("t-{0}".format(i),))
    t.start()
    t_obj.append(t)
 
for t in t_obj:
    t.join()   # 为join是等子线程执行的结果，如果不加，主线程执行完，下面就获取不到子线程num的值了，共享数据num值就错误了
 
 
print("--------all thread has finished")
print("num:", num)   # 输出最后的num值
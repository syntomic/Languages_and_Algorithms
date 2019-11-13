import threading
import time
 
 
def run(n):
    semaphore.acquire()   # 加信号量锁
    time.sleep(5)
    print("run the thread: %s\n" % n)
    semaphore.release()   # 释放信号量锁
 
 
if __name__ == '__main__':
 
    semaphore = threading.BoundedSemaphore(5)  # 最多允许5个线程同时运行(Bounded:绑定，Semaphore：信号量)
    for i in range(20):
        t = threading.Thread(target=run, args=(i,))
        t.start()
 
while threading.active_count() != 1:
    pass
else:
    print('----all threads done---')
import threading
import queue
 
 
def producer():
    """
    模拟生产者
    :return:
    """
    for i in range(10):
        q.put("骨头 %s" % i)
 
    print("开始等待所有的骨头被取走...")
    q.join()  # 等待这个骨头队列被消费完毕
    print("所有的骨头被取完了...")
 
 
def consumer(n):
    """
    模拟消费者
    :return:
    """
    while q.qsize() > 0:
        print("%s 取到" % n, q.get())
        q.task_done()  # 每去到一个骨头，便告知队列这个任务执行完了
 
q = queue.Queue()
 
p = threading.Thread(target=producer,)
p.start()
 
c1 = consumer("QQ")
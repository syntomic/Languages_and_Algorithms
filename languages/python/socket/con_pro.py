import time, random
import queue, threading

q = queue.Queue()

"""
生产者生产完毕，消费者再消费例子

def producer():
    for i in range(10):
        q.put(i)

    print("wait....")
    q.join()
    print("done.")

def consumer(n):
    while q.qsize() > 0:
        print('{} get'.format(n), q.get())
        q.task_done()

p = threading.Thread(target=producer, )
p.start()

c1 = consumer("Q")

"""
"""
边生产边消费
def producer(name):
    count = 0

    while count < 20:
        time.sleep(random.randrange(3))
        q.put(count)
        print("Producer %s has produced %s pie..." % (name, count))
        count += 1

def consumer(name):
    count = 0
    while count < 20:
        time.sleep(random.randrange(4))
        if not q.empty():
            data = q.get()
            print(data)
            print('\033[32;1mConsumer %s has eat %s pie...\033[0m' % (name, data))
            count += 1
        else:
            print("-----no pie anymore----")
        
 
p1 = threading.Thread(target=producer, args=('A',))
c1 = threading.Thread(target=consumer, args=('B',))
p1.start()
c1.start()
"""
import time
 
 
def consumer(name):
    print("--->starting eating baozi...")
    while True:
        new_baozi = yield   # yield设置生成器
        print("[{0}] is eating baozi {1}".format(name, new_baozi))
 
 
def producer():
    r = con.send(None)  # 调用生成器
    #r = con2.__next__()
    n = 0
    while n < 5:
        n += 1
        print("\033[32m[producer]\033[0m is making baozi {0}".format(n))
        con.send(n)  # 唤醒生成器，并且向生成器传值
        #con2.send(n)
        time.sleep(1)
        
if __name__ == '__main__':
    con = consumer("c1")   # 创建一个生成器c1
    #con2 = consumer("c2")   # 创建一个生产器C2
    p = producer()
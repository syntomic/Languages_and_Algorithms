import threading, time
  
def run(n):   #这边的run方法的名字是自行定义的，跟继承式多线程不一样，那个是强制的
    print("task:",n)
    time.sleep(2)
    print("task done",n)
  
start_time = time.time()  #开始时间
t_obj = [] # 存放子线程实例
for i in range(5):   #一次性启动5个线程
    t = threading.Thread(target=run,args=("t-{0}".format(i),))
    t.start()
    t_obj.append(t)  # 为了不阻塞后面线程的启动,不在这里join,先放到一个列表中

for t in t_obj:
    t.join()
  
print("--------all thead has finished")
print("cost:",time.time()-start_time)  #计算总耗时
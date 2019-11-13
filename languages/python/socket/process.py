from multiprocessing import Process,Queue
 
 
def f(q):
    q.put([66, None, 'hello word'])
 
if __name__ == '__main__':
    q = Queue()   # 把这个q传给了子进程
    p = Process(target=f, args=(q,))   # 子线程访问父进程的q
    p.start()
    print(q.get())
    p.join()
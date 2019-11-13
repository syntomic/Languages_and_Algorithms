from multiprocessing import Process, Manager
import os
 
 
def f(d, l):
    d[os.getpid()] = os.getpid()
    l.append(os.getpid())
    print(l)
 
if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()   # 声明一个字典，这个字典是用manger声明的，不是用dict()声明的
        # manger.dict()是用专门的语法生产一个可在多进程之间进行传递和共享的一个字典
        l = manager.list(range(5))  # 同样声明一个列表
        p_list = []
        for i in range(10):
            p = Process(target=f, args=(d, l))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()
        print(d)
        print(l)
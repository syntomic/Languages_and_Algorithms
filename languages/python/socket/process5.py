from multiprocessing import Process,Pool
import time,os
 
 
def foo(i):
    time.sleep(2)
    print("in process", os.getpid())  # 打印子进程的进程号
 
 
def bar(arg):
    print('-->exec done:', arg, os.getpid())   # 打印进程号
 
if __name__ == "__main__":
    pool = Pool(processes=2)
    print("主进程", os.getpid())   # 主进程的进程号
    for i in range(3):
        pool.apply_async(func=foo, args=(i,), callback=bar)   # 执行回调函数callback=Bar
    print('end')
    pool.close()
    pool.join()  # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。
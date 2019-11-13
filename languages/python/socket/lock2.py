import threading
 
 
def run1():
    print("grab the first part data")
    #lock.acquire()  # 修改num前加锁
    global num
    num += 1
    #lock.release()   # 释放锁
    return num
 
 
def run2():
    print("grab the second part data")
    #lock.acquire()   # 修改num2前加锁
    global num2
    num2 += 1
    #lock.release()   # 释放锁
    return num2
 
 
def run3():
    lock.acquire()  # 加锁
    res = run1()   # 执行run1函数
    print('--------between run1 and run2-----')
    res2 = run2()  # 执行run2函数
    lock.release()  # 释放锁
    print(res, res2)
 
 
if __name__ == '__main__':
    num, num2 = 0, 0
    lock = threading.Lock()  # 设置锁的全局变量
    for i in range(10):
        t = threading.Thread(target=run3)
        t.start()
        t.join()
 
 
    while threading.active_count() != 1:  # 判断是否只剩主线程了
        print(threading.active_count())
    else:
        print('----all threads done---')
        print(num, num2)
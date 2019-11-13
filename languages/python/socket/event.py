import threading
import time
 
event = threading.Event()  # 生成线程事件实例
 
 
def lighter():
    """
    模拟红绿灯
    :return:
    """
    count = 0
    event.set()   # 先设置标志位,代表绿灯
    while True:
        if count > 5 and count < 10:   # 改成红灯
            event.clear()    # 清除标志位，变成红灯
            print("\033[41m red light is on ....\033[0m")
        elif count > 10:
            event.set()   # 创建标志位，变成绿灯
            count = 0
        else:
            print("\033[42m green light is on ....\033[0m")
 
        time.sleep(1)
        count += 1
 
 
def car(name):
    """
    模拟车子
    :param name:
    :return:
    """
    while True:
        if event.is_set():   # 有标志位，代表是绿灯
            print("{0} running ....".format(name))
            time.sleep(1)
        else:   # 如果不是绿灯就代表红灯
            print("{0} sees red light ,waiting ....".format(name))
            event.wait()   # 阻塞
            print("\033[32m green light is on , start going ...\033[0m")
 
 
light = threading.Thread(target=lighter,)  # 启动代表红绿灯的线程
light.start()
 
car1 = threading.Thread(target=car, args=("car1",))  # 启动代表车的线程
car1.start()

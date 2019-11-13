import threading
import time
import random
 
 
def door():
    door_open_time_counter = 0
    while True:
        if door_swiping_event.is_set():
            print("\033[32;1m door opening....\033[0m")
            door_open_time_counter +=1
 
        else:
            print("\033[31;1m door closed...., swipe to open.\033[0m")
            door_open_time_counter = 0  # 清空计时器
            door_swiping_event.wait()
 
        if door_open_time_counter > 3:  # 门开了已经3s了,该关了
            door_swiping_event.clear()
 
        time.sleep(0.5)
 
 
def staff(n):
 
    print("staff [%s] is coming..." % n )
    while True:
        if door_swiping_event.is_set():
            print("\033[34;1m door is opened, passing.....\033[0m")
            break
        else:
            print("staff [%s] sees door got closed, swiping the card....." % n)
            print(door_swiping_event.set())
            door_swiping_event.set()
            print("after set ", door_swiping_event.set())
        time.sleep(0.5)
 
 
if __name__ == "__main__":
 
    door_swiping_event = threading.Event()  # 设置事件
    door_thread = threading.Thread(target=door)
    door_thread.start()
 
    for i in range(20):
        p = threading.Thread(target=staff, args=(i,))
        time.sleep(random.randrange(3))
        p.start()

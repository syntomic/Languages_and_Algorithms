import threading, time

def run(n):
    print("run", n)
    time.sleep(2)

t1 = threading.Thread(target=run, args=("t1",))
t2 = threading.Thread(target=run, args=("t2",))

t1.start()
t2.start()
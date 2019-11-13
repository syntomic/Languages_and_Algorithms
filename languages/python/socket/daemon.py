import threading
import time

def run(n):
    print("task:", n)
    time.sleep(2)
    print("task done.", n, threading.current_thread())

start_time = time.time()
for i in range(5):
    t = threading.Thread(target=run, args=("t-{}".format(i),))
    t.setDaemon(True)
    t.start()

print("--------all thread has finished", threading.current_thread(), threading.active_count())
print("cost:", time.time() - start_time)
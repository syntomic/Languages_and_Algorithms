import gevent
 
 
def foo():
    print("Running in foo")
    gevent.sleep(3)  # 模仿io操作，一遇到io操作就切换
    print("Explicit context switch to foo again")
 
 
def bar():
    print("Explicit context to bar")
    gevent.sleep(1)
    print("Implicit context switch back to bar")
 
 
def fun3():
    print("running fun3")
    gevent.sleep(0)   # 虽然是0秒，但是会触发一次切换
    print("running fun3 again")
    
gevent.joinall([
    gevent.spawn(foo),  # 生成协程
    gevent.spawn(bar),
    gevent.spawn(fun3)
])

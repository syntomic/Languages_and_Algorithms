from greenlet import greenlet
 
 
def test1():
    print(12)
    gr2.switch()  # 切换到test2
    print(34)
    gr2.switch()   # 切换到test2
 
 
def test2():
    print(56)
    gr1.switch()   # 切换到test1
    print(78)
 
gr1 = greenlet(test1)  # 启动一个协程
gr2 = greenlet(test2)
gr1.switch()   # 切换到test1，这个switch不写的话，会无法输出打印
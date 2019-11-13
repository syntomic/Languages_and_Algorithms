from multiprocessing import Process, Pipe
 
 
def f(conn):
    conn.send([66, None, 'hello,word'])  # 发送消息给父进程
    conn.send("QQ")  # 发送消息给父进程
    print(conn.recv())   # 接收父进程的消息
    conn.close()
 
if __name__ == '__main__':
    parent_conn, child_conn = Pipe()  # 管道生成返回两个实例，是双向的，这边把第1个作为父连接，第2个作为子连接。也可以，两者角色调换一下
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    print(parent_conn.recv())  # 接收两次
    parent_conn.send("微信")   # 发送给子进程
    p.join()
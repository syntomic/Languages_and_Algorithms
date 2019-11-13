import selectors,socket
 
sel = selectors.DefaultSelector()
 
def accept(sock,mask):
    "接收客户端信息实例"
    conn,addr = sock.accept()
    print("accepted",conn,'from',addr)
    conn.setblocking(False)
    sel.register(conn,selectors.EVENT_READ,read)  #新连接注册read回调函数
 
def read(conn,mask):
    "接收客户端的数据"
    data = conn.recv(1024)
    if data:
        print("echoing",repr(data),'to',conn)
        conn.send(data)
    else:
        print("closing",conn)
        sel.unregister(conn)
        conn.close()
 
server = socket.socket()
server.bind(('localhost',9999))
server.listen(500)
server.setblocking(False)
sel.register(server,selectors.EVENT_READ,accept)  #注册事件，只要来一个连接就调accept这个函数,
#sel.register(server,selectors.EVENT_READ,accept) == inputs=[server,]
 
while True:
    events = sel.select()  #这个select,看起来是select，有可能调用的是epoll，看你操作系统是Windows的还是Linux的
                           #默认阻塞，有活动连接就返回活动连接列表
    print("事件：",events)
    # [(SelectorKey(fileobj=<socket.socket fd=12, family=AddressFamily.AF_INET, type=2049, proto=0, laddr=('127.0.0.1', 9999)>, 
    #               fd=12, 
    #               events=1, 
    #               data=<function accept at 0x7f7f7d6d4e18>), 1)]
    for key,mask in events:
        callback = key.data  # 相当于调accept了
        callback(key.fileobj,mask)  # key.fileobj=文件句柄
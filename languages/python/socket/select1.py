import select,socket,queue
server = socket.socket()
server.bind(("localhost",9000))
server.listen(1000)
server.setblocking(False) #设置为非阻塞
msg_dic = dict() #定义一个队列字典
inputs = [server,]  #由于设置成非阻塞模式，accept和recive都不阻塞了，没有值就会报错，因此最开始需要最开始需要监控服务端本身，等待客户端连接
outputs = [] 
while True:
    #exceptional表示如果inputs列表中出现异常，会输出到这个exceptional中
    readable,writeable,exceptional = select.select(inputs,outputs,inputs)#如果没有任何客户端连接，就会阻塞在这里 
    for r in readable:# 每个r代表一个socket链接
        if r is server:  #如果这个socket是server的话，就说明是是新客户端连接了
            conn,addr = r.accept() #新连接进来了,接受这个连接，生成这个客户端实例
            print(conn)
            print("来了一个新连接",addr)
            inputs.append(conn) #为了不阻塞整个程序,我们不会立刻在这里开始接收客户端发来的数据, 把它放到inputs里, 下一次loop时,这个新连接
            #就会被交给select去监听
            msg_dic[conn] = queue.Queue() #初始化一个队列，后面存要返回给这个客户端的数据
        else: #如果不是server，就说明是之前建立的客户端来数据了
            data = r.recv(1024)
            print("收到数据：",data)
            msg_dic[r].put(data)#收到的数据先放到queue里,一会返回给客户端
            outputs.append(r)#为了不影响处理与其它客户端的连接 , 这里不立刻返回数据给客户端
            # r.send(data)
            # print("send done....")
    for w in writeable:  #要返回给客户端的链接列表
        data_to_client = msg_dic[w].get()
        w.send(data_to_client)   #返回给客户端的源数据
        outputs.remove(w)  #确保下次循环的时候writeable,不返回这个已经处理完的这个连接了
 
    for e in exceptional:  #处理异常的连接
        if e in outputs:   #因为e不一定在outputs，所以先要判断
            outputs.remove(e)
        inputs.remove(e)   #删除inputs中异常连接
        del msg_dic[e]   #删除此连接对应的队列
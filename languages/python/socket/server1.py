import socket,os
import time
  
server = socket.socket()
server.bind(("localhost",9999))
server.listen(5)
while True:
    conn,addr = server.accept()
    print("new addr:",addr)
    while True:
        data = conn.recv(1024)
        if not data:
            print("客户端已断开")
            break
        print("执行指令：",data)
        cmd_res = os.popen(data.decode()).read()
        print("before send:",len(cmd_res))
        if len(cmd_res) == 0:
            cmd_res = "cmd has no output...."
        conn.send( str(len(cmd_res.encode())).encode() )  # 发送服务端发送给客户端数据的长度
        # 等待客户端确认, 解决粘包问题
        client_acknowledge = conn.recv(1024) # time.sleep(0.5)
        conn.send(cmd_res.encode("utf-8"))   # 发送服务端的数据
        print("send done")
server.close()
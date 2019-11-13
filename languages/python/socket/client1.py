import socket
  
client = socket.socket()
client.connect(("localhost",9999))
  
while True:
    cmd = input(">>>:").strip()
    if len(cmd) == 0:continue
    client.send(cmd.encode("utf-8"))
    cmd_res_size = client.recv(1024)  #接收命令的长度
    print("命令结果大小：",cmd_res_size.decode())
    # 发个响应给服务端,告诉服务端，客户端已经准备好了
    client.send("客户端准备好接收数据内容了".encode())
    recevied_size  = 0   #接收客户端发来数据的计算器
    recevied_data = b''  #客户端每次发来内容的计数器
    while recevied_size < int(cmd_res_size.decode()):  #当接收的数据大小 小于 客户端发来的数据
        cmd_res = client.recv(1024)
        recevied_size += len(cmd_res)  #每次收到的服务端的数据有可能小于1024，所以必须用len判断
        recevied_data += cmd_res
    else:
        print(recevied_data.decode("utf-8","ignore"))
        print("cmd res receive done ....",recevied_size)

client.close()
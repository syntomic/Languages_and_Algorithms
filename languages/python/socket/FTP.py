# server
import socket, os, hashlib
 
server = socket.socket()
server.bind(('localhost',2222))
 
server.listen()
 
while True:
    conn,addr = server.accept()
    print("一个新的连接：",addr)
    while True:
        print("等待新指令")
        data = conn.recv(1024)
        if not data:
            print("客户端已经断开")
            break
        cmd, file_name = data.decode().split()  # 接收客户端发过来的命令和文件名
        print("执行指令:%s, 文件名:%s" % (cmd, file_name))
        if os.path.isfile(file_name): 
            m = hashlib.md5()  # 生成MD5对象
            with open(file_name, "rb") as f:
                file_size = os.stat(file_name).st_size  # 获取一个文件的大小：os.stat(文件名).st_size
                conn.send(str(file_size).encode())
                conn.recv(1024)  # 等待客户端确认，防止发生粘包
                for line in f:
                    m.update(line) # 不断更新计算MD5值
                    conn.send(line)
                print("md5值", m.hexdigest())
            conn.recv(1024)  # 等待客户端确认，防止发生粘包,准备发送MD5值
            conn.send(m.hexdigest().encode())  # 发送MD5值给客户端
        print("send done")
server.close()

# client
import socket
 
client = socket.socket()
 
client.connect(("localhost", 2222))
 
while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0:continue
    print(cmd)
    if cmd.startswith("get"):
        client.send(cmd.encode("utf-8"))  # 发送下载命令和文件名
        file_size = client.recv(1024)  # 接收文件大小
        print("即将接收数据大小:", file_size.decode())
        client.send("客户端准备好接收数据内容了".encode())
        revived_size = 0
        file_name = cmd.split()[1]  # 文件名
        m = hashlib.md5()  # 生成MD5对象
        with open(file_name + "_new", "wb",) as f:
            while revived_size < int(file_size.decode()):
                if int(file_size.decode()) - revived_size > 1024:  # 只要剩余文件字节大于1024字节，就默认最大值接收
                    size = 1024
                else:
                    size = int(file_size.decode()) - revived_size   # 最后一次，剩多少收多少
                    print("last receive:", size)
                file_data = client.recv(size)
                revived_size += len(file_data)
                m.update(file_data)  # 不断更新计算接收数据的文件值
                f.write(file_data)
            else:
                print(file_size, revived_size)
                client_md5_value = m.hexdigest()  # 生成接收数据的MD5值16进制形式
            server_md5_value = client.recv(1024)  # 接收服务端的MD5值
            print("client接收文件MD5值：%s,server发送文件的MD5值:%s" % (client_md5_value, server_md5_value))
client.close()
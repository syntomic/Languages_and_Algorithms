import socket
from wsgiref.simple_server import make_server

client = socket.socket()
client.connect(("localhost",9999))
  
while True:
    cmd = input(">>>:").strip()
    if len(cmd) == 0:continue
    a = client.send(cmd.encode("utf-8"))
    cmd_res = client.recv(500) # 可能导致客户端数据接收不完整
    print(cmd_res.decode("utf-8",'ignore'))
  
client.close()
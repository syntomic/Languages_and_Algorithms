import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024)
                print('{0} write:'.format(self.client_address[0]))
                print(self.data.decode())
                self.request.send(self.data.upper())
            except ConnectionResetError as e:
                print("error",e)
                break

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = socketserver.TCPServer((HOST, PORT), MyServer)
    #server = socketserver.ForkingTCPServer((HOST, PORT), MyServer) 多进程
    #server = socketserver.ThreadingTCPServer((HOST, PORT), MyServer) 多线程
    server.serve_forever()
    server.server_close()

'''
class SocketServer.BaseServer：这是模块中的所有服务器对象的超类。它定义了接口，如下所述，但是大多数的方法不实现，在子类中进行细化。
 
BaseServer.fileno()：返回服务器监听套接字的整数文件描述符。通常用来传递给select.select(), 以允许一个进程监视多个服务器。
 
BaseServer.handle_request()：处理单个请求。处理顺序：get_request(), verify_request(), process_request()。如果用户提供handle()方法抛出异常，将调用服务器的handle_error()方法。如果self.timeout内没有请求收到， 将调用handle_timeout()并返回handle_request()。
 
BaseServer.serve_forever(poll_interval=0.5): 处理请求，直到一个明确的shutdown()请求。每poll_interval秒轮询一次shutdown。忽略self.timeout。如果你需要做周期性的任务，建议放置在其他线程。
 
BaseServer.shutdown()：告诉serve_forever()循环停止并等待其停止。python2.6版本。
 
BaseServer.address_family: 地址家族，比如socket.AF_INET和socket.AF_UNIX。
 
BaseServer.RequestHandlerClass：用户提供的请求处理类，这个类为每个请求创建实例。
 
BaseServer.server_address：服务器侦听的地址。格式根据协议家族地址的各不相同，请参阅socket模块的文档。
 
BaseServer.socketSocket：服务器上侦听传入的请求socket对象的服务器。
 
<br><br>#服务器类支持下面的类变量：
 
BaseServer.allow_reuse_address：服务器是否允许地址的重用。默认为false ，并且可在子类中更改。
 
BaseServer.request_queue_size
 
请求队列的大小。如果单个请求需要很长的时间来处理，服务器忙时请求被放置到队列中，最多可以放request_queue_size个。一旦队列已满，来自客户端的请求将得到 “Connection denied”错误。默认值通常为5 ，但可以被子类覆盖。
 
BaseServer.socket_type：服务器使用的套接字类型; socket.SOCK_STREAM和socket.SOCK_DGRAM等。
 
BaseServer.timeout：超时时间，以秒为单位，或 None表示没有超时。如果handle_request()在timeout内没有收到请求，将调用handle_timeout()。
 
<br><br><br><br>#下面方法可以被子类重载，它们对服务器对象的外部用户没有影响。
 
BaseServer.finish_request()：实际处理RequestHandlerClass发起的请求并调用其handle()方法。 常用。
 
BaseServer.get_request()：接受socket请求，并返回二元组包含要用于与客户端通信的新socket对象，以及客户端的地址。
 
BaseServer.handle_error(request, client_address)：如果RequestHandlerClass的handle()方法抛出异常时调用。默认操作是打印traceback到标准输出，并继续处理其他请求。
 
BaseServer.handle_timeout()：超时处理。默认对于forking服务器是收集退出的子进程状态，threading服务器则什么都不做。
 
BaseServer.process_request(request, client_address) :调用finish_request()创建RequestHandlerClass的实例。如果需要，此功能可以创建新的进程或线程来处理请求,ForkingMixIn和ThreadingMixIn类做到这点。常用。
 
BaseServer.server_activate()：通过服务器的构造函数来激活服务器。默认的行为只是监听服务器套接字。可重载。
 
BaseServer.server_bind()：通过服务器的构造函数中调用绑定socket到所需的地址。可重载。
 
BaseServer.verify_request(request, client_address)：返回一个布尔值，如果该值为True ，则该请求将被处理，反之请求将被拒绝。此功能可以重写来实现对服务器的访问控制。默认的实现始终返回True。client_address可以限定客户端，比如只处理指定ip区间的请求。 常用。

'''
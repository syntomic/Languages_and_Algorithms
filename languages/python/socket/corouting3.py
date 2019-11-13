from urllib import request
import gevent, time
from gevent import monkey

monkey.patch_all()

def run(url):
    print("GET:{0}".format(url))
    resp = request.urlopen(url)    # request.urlopen()函数 用来打开网页
    data = resp.read()    # 读取爬到的数据
    with open("url.html", "wb") as f:
        f.write(data)
    print('{0} bytes received from {1}'.format(len(data), url))
 
urls = [
    'https://www.163.com/',
    'https://www.yahoo.com/',
    'https://github.com/'
]
 
time_start = time.time()    # 开始时间
gevent.joinall([                     # 用gevent启动协程
    gevent.spawn(run, 'https://www.163.com/'),  # 第二个值是传入参数，之前我们没有讲，因为前面没有传参
    gevent.spawn(run, 'https://www.yahoo.com/'),
    gevent.spawn(run, 'https://github.com/'),
])
print("同步cost", time.time() - time_start)  # 程序执行消耗的时间
<p align="right">参考 Python教程 廖雪峰</p>

## 简介
- 优点
    - 网络应用
    - 日常小工具
    - 包装其他语言开发的程序
- 缺点
    - 运行速度慢
    - 代码不能加密
- 解释器
    - Cpython
    - Ipython
    - PyPy
    - Jpython
    - IronPython
## 基础
- 变量；**引用语义** 指向对象 
- 数据类型
    - 整数和浮点数：无大小限制
    - 字符串：强大的处理方法
        - 编码
            - 计算机内存，统一使用Unicode编码
            - 保存到硬盘或需要传输，采用utf-8
    - list 和 tuple
        - 查找和插入慢
        - 占用空间少
    - dict 和 set
        - 查找和插入快
        - 占用内存
    - 类型定义：`def greeting(name: str) -> str:`
- 条件判段和循环
- 函数：`fun(*args, **kw)`
    - 递归：尾递归优化=循环
- 高级特性
    - 切片
    - 迭代
    - 列表生成式
    - 生成器
    - 迭代器
        - `Iterable`：`for`
        - `Iterator`：`next()`
- [代码风格](https://github.com/syntomic/Languages_and_Algorithms/tree/master/python/pythonic/)
## 函数式编程：面向过程
- 高阶函数
    - map/reduce
    - filter
    - sorted：`sorted([1,-2,3], key=abs)`
- 返回函数：共享参数`f()`
    - 返回闭包：返回函数不要引用任何循环变量，或者后续会发生变化的变量
- 装饰器：代码运行期间动态增加功能的方式
    - `now = log(text)(now)` + `@functools.wraps(func)`
- 偏函数：把函数的某些参数固定住，返回一个新函数
    - `int2 = functools.partial(int, base=2)`

## 面向对象编程：一切皆对象(一系列消息在各个对象之间传递)

- 类和实例
    - 访问限制：`__name`
    - 继承和多态：静态语言vs静态语言
    - 获取信息：`isinstance()` `dir()` `hasattr(obj, attr)`
- 高级
    - `__slots__`: 限制实例属性
    - `@property`: 对参数进行必要的检查
    - 多重继承：`class MyTCPServer(TCPServer, ForkingMixIn)`
    - 定制类
        - `__repr__` vs `__str__`
        - `__getattr__`：动态调用 REST API
        - `__call__`
    - 枚举类：`from enum import Enum` + `member.value`
    - 元类 
        - `type(class, (object,), dict(method, attr))`
        - metaclass到class到实例
            - `ListMetaclass(type)`
            - `metaclass=ListMetaclass`
            - `__new__(cls, name, bases, attrs)`
## 错误、调试和测试
- 错误
    - 捕获：`try...except...finally`
    - 调用栈
    - 记录：`logging.exception()`
    - 抛出：`raise`
- 调试
    - `assert` + `python -O err.py`
    - `logging.basicConfig(level=logging.INFO)`+`logging.info()`
    - `pdb.set_trace()`
- 单元测试TDD：`python -m unittest mydict_test`
- 文档测试：`doctest.testmod()`

## IO编程
- 同步：简单
    - 文件读写：`with open() as f: f.read() `
    - 内存中读写
        - StringIO
        - BytesIO
    - 操作文件和目录：`os.path.join()`
    - 序列化
        - 内存到可存储或传输(pickling)：`pickle.dumps()` `json.dumps()`
        - 序列化对象重新读到内存里(unpicking)：`picle.loads()` `json.loads()`

- [进程和线程](https://github.com/syntomic/Languages_and_Algorithms/tree/master/python/process_thread/)：同步和数据共享
    - 多进程
        - `os.fork()`
        - `p=multiprocessing.Process(target=func, args=(,))`+`p.join()`同步
        - `p=multiprocessing.Pool(4)`+`p.apply_async(target, args=(,))`
        - 子进程：`subprocess.call([,])`
        - 进程间通信：`multiprocessing.Queue()`
    - 多线程
        - `tread.Thread(target=func, name='')`
        - 所有变量都由所有线程共享
        - `lock=threading.Lock()`+`lock.acquire()`+`lock.release()`
        - 死锁
        - GIL锁
    - TreadLocal：解决参数在各个函数之间互相传递的问题
        - `threading.local()`
    - 多线程vs多进程：Master-Worker
        - 多进程：Apache
            - 稳定性高
            - 创建进程代价大
        - 多线程：IIS
            - 任何线程出问题可能导致整个进程崩溃
            - 效率稍高
        - 多线程+多进程
        - 任务切换
        - 计算密集型vsIO密集型：C vs Python
        - 分布式进程：`multiprocessing.managers` + `queue`
- 异步：单进程单线程执行多任务 Nginx
    - [协程(Coroutine)](https://github.com/syntomic/Languages_and_Algorithms/tree/master/python/process_thread/)：多进程+协程
        - 极高执行效率
        - 不需要锁机制
    - python通过generator实现：`yield`
        - `asyncio`: async + await
        - `aiohttp`: 基于asyncio实现的HTTP框架

## 常用模块
- 模块和包
    - `sys.path`
- 内建模块
    - `datetime`
    - `collections`：`namedtuple(name, [attr])` `defaultdict` `orderedDict` `ChainMap`
    - `base64`：3字节的二进制数据编码位4字节的文本数据
    - `struct`：`bytes`和其他二进制数据类型的转换
    - `hashlib`
    - `hmac`：Keyed-Hashing for Message Authentication
    - `itertools`
    - `contextlib`：上下文管理(`with`)
    - `tkinter`：图形用户界面(GUI)
    - `urllib`
    - `XML`
    - `HTMLParser`
- 第三方模块
    - `Pillow`：图像处理标准库
    - `request`
    - `chardet`：检测编码
    - `psutil`：系统监控
    - `virtualenv`：运行环境

## [网络编程](https://github.com/syntomic/Languages_and_Algorithms/tree/master/python/web/)
- TCP编程：`s = socket.socket()`
    - 客户端：`s.connect()` + `s.send()`
    - 服务器：`s.bind()` + `s.listen()`
- UDP编程：不需要listen方法
- 电子邮件：MUA MTA MDA MUA
    - 编写MUA把邮件发到MTA：协议 SMTP
    - 编写MUA从MDA上收邮件：协议 POP3 IMAP
- 访问数据库
    - ORM框架：`SQLSALchemy`
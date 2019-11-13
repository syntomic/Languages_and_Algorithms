- 特性
    - 封装
    - 继承
        - `super(子类, self).__init__(name, age)`
        - 多继承: 宽度优先查询
    - 多态: 一个基类中派生出了不同的子类，且每个子类在继承了同样的方法名的同时又对父类的方法做了不同的实现, 接口重用
- 使用场景
    - 提取公共功能
    - 根据一个模板去创建某些东西
    - 多个函数传入共同参数
- 实例化过程: 申请地址->把地址和参数传递给类->创建实例
    - `__init__`: 初始化函数
    - `__del__`: 析构函数, 引用被清空后自动执行, 程序收尾工作
    - 私有属性 vs 公有属性
- 装饰器方法
    - `@staticmethod`: 只是名义上归类管理，实际上在静态方法里访问不了类或实例中的任何属性, `os.mkdir()`
    - `@classmethod`: 只能访问类变量，不能访问实例变量
    - `@property`: 把一个方法变成一个静态属性
        - `@静态方法名.setter`
        - `@静态方法名.deleter`
- 特殊成员方法
    - `__doc__`: 表示类的描述信息
    - `__module__`: 表示当前操作的对象在哪个模块
    - `__class__`: 表示当前操作的对象的类是什么
    - `__dict__`:  查看类或对象中的所有成员
    - `__str__`: 打印对象时，默认输出该方法的返回值
    - `__getitem__、__setitem__、__delitem__`
- 反射: 实现动装饰器实现态的装配，通过字符串来反射类中的属性和方法
    ```python
    class Dog(object):
  
        def __init__(self,name):
            self.name = name
    
        def eat(self,food):
            print("{0} is eating...{1}".format(self.name,food))
    
    d = Dog("shabi")
    choice = input(">>>:").strip()
    
    if hasattr(d,choice):  #判断d对象中存在属性和方法
        name_value = getattr(d,choice)  #获取属性值
        print(name_value)
        setattr(d,choice,"hong")   #修改属性值
        print(getattr(d,choice))   #重新获取属性的值
    else:
        setattr(d,choice,None)    #设置不存在的属性值为None
        v = getattr(d,choice)
        print(v)
    
    #输出
    >>>:name
    shabi
    hong
    >>>:abc
    None
    ```
- 类的创建
    - 传统: 通过type类创建
    - `type`: `类名 = type('类名',(父类，)，{'方法名'：方法的内存地址})`
    - `__new__`: 实例化, 先于 `__init__`执行, 
    - `__metaclass__`: 类是由谁来帮他实例化创建的
    ```python
    class MyType(type):
        def __init__(self,*args,**kwargs):
    
            print("Mytype __init__",*args,**kwargs)
    
        def __call__(self, *args, **kwargs):
            print("Mytype __call__", *args, **kwargs)
            obj = self.__new__(self)
            print("obj ",obj,*args, **kwargs)
            print(self)
            self.__init__(obj,*args, **kwargs)
            return obj
    
        def __new__(cls, *args, **kwargs):
            print("Mytype __new__",*args,**kwargs)
            return type.__new__(cls, *args, **kwargs)
  
    class Foo(object,metaclass=MyType):  #python3统一用这种
        #__metaclass__ = MyType  #python2.7中的写法
    
        def __init__(self,name):
            self.name = name
    
            print("Foo __init__")
    
        def __new__(cls, *args, **kwargs):
            print("Foo __new__",cls, *args, **kwargs)
            return object.__new__(cls)
    
    f = Foo("shuaigaogao")
    print("f",f)
    print("fname",f.name)
    
    #输出
    Mytype __new__ Foo (<class 'object'>,) {'__new__': <function Foo.__new__ at 0x0000025EF0EFD6A8>,
    '__init__': <function Foo.__init__ at 0x0000025EF0EFD620>, '__qualname__': 'Foo', '__module__': '__main__'}
    Mytype __init__ Foo (<class 'object'>,) {'__new__': <function Foo.__new__ at 0x0000025EF0EFD6A8>,
    '__init__': <function Foo.__init__ at 0x0000025EF0EFD620>, '__qualname__': 'Foo', '__module__': '__main__'}
    Mytype __call__ shuaigaogao
    Foo __new__ <class '__main__.Foo'>
    obj  <__main__.Foo object at 0x0000025EF0F05048> shuaigaogao
    <class '__main__.Foo'>
    Foo __init__
    f <__main__.Foo object at 0x0000025EF0F05048>
    fname shuaigaogao
    ```
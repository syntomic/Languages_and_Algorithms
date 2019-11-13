class MyType(type):
    def __init__(self,*args,**kwargs):
        print(self)
  
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
        return type.__new__(cls, *args, **kwargs) ## type(cls, bases, attrs)
  
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
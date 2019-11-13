class Foo(object):
  
    def __init__(self,name):
        self.name = name
  
        print("Foo __init__")
  
    def __new__(cls, *args, **kwargs):   #cls相当于传入类Foo
        print("Foo __new__",cls, *args, **kwargs)
        return object.__new__(cls)  #继承父类的__new__方法，这边必须以返回值的形式继承
  
f = Foo("shuaigaogao")
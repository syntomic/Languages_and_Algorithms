class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance  

#class MyClass(Singleton):  
    #a = 1

if __name__ == "__main__":
    one = Singleton()
    two = Singleton()
    print(one == two)
    print(one is two)
    print(id(one),id(two))
    #print(id(MyClass()))
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
# Python2
#class MyClass(object):
#    __metaclass__ = Singleton

class MyClass(metaclass=Singleton):
    a = 1

if __name__ == "__main__":
    one = MyClass()
    two = MyClass()
    print(one == two)
    print(one is two)
    print(id(one),id(two))
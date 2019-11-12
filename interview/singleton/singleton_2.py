from functools import wraps

def singleton(cls):
    instances = {}
    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
            print(cls)
        return instances[cls]
    return getinstance

# singleton(MyClass)
@singleton
class MyClass(object):
    a = 1

if __name__ == "__main__":
    one = MyClass()
    two = MyClass()
    print(one == two)
    print(one is two)
    print(id(one),id(two))


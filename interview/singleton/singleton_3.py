class Singleton(type):
    def __call__(self, *args, **kwargs):
        if not hasattr(self, '_instance'):
            self._instance = object.__new__(self)
            print(isinstance(self, Singleton))
        return self._instance

class MyClass(metaclass=Singleton):
    a = 1

if __name__ == "__main__":
    one = MyClass()
    two = MyClass()
    print(MyClass._instance)
    print(one == two)
    print(one is two)
    print(id(one),id(two))
    print(object())
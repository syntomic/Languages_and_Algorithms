class Chain(object):
    """动态实现API"""
    def __init__(self, path=''):
       self.__path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self.__path, path))

    def __call__(self, path):   # self(path)
        return Chain('%s/%s' % (self.__path, path))

    def __str__(self):
        return self.__path

    __repr__ = __str__

#print(Chain().sh.users('michael').repos)

from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

#print(Weekday(1).value)

import functools

def log(text):
    def decorator(func):
        @functools.wraps(func) ## 保证__name__一致
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-3-25')

now()
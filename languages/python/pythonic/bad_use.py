def extendList(val, list=[]):
    """默认参数最好不要为可变对象"""
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList( 'a' )

print("list1 = %s" % list1)
print("list2 = %s" % list2)
print("list3 = %s" % list3)


def multipliers():
    """惰性"""
    return [lambda x : i * x for i in range(4)]

#print(multipliers())

print([m(2) for m in multipliers()])

def multipliers_2():
    for i in range(4):
        yield lambda x : i * x

print([m(2) for m in multipliers_2()])

def multipliers_3():
    return [lambda x, i=i : i * x for i in range(4)]

from functools import partial
from operator import mul

def multipliers_4():
    return [partial(mul, i) for i in range(4)]



a = {}
a[1] = "A"
a[1.0] = "B"
a[2] = "C"
print(a)

#hash(1)==hash(1.0)==hash(True)
#hash(0) == hash(False) == hash("")
print(isinstance(True, int))

class A_1():
    def __init__(self,dicts):
        self.name = dicts["name"]
        self.age = dicts["age"]
        self.sex = dicts["sex"]
        self.hobby = dicts["hobby"]

dicts = {"name":"lisa","age":23,"sex":"women","hobby":"hardstyle"}
a = A_1(dicts)

class A_2():
    def __init__(self,dicts):
        self.__dict__.update(dicts)
        print(self.__dict__)

dicts = {"name":"lisa","age":23,"sex":"women","hobby":"hardstyle"}
a = A_2(dicts)



list = ['a', 'b' , 'c' , 'd' , 'e' ]
print(list[10:])


[x for x in list[::2] if x % 2 == 0]
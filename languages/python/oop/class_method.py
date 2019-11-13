class Dog(object):
 
    name = "honggege"  #定义类变量
    def __init__(self,name):
        self.name = name
 
    @classmethod
    def eat(self,food):
        print("{0} is eating {1}".format(self.name,food))
 
d = Dog("shabihong")
d.eat("hotdog")
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
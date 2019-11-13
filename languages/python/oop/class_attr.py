class dog(object):
    "dog class"
 
    nationality = "JP"
 
    def __init__(self,name):
        self.name = name
 
d1 = dog("AAAA")
d2 = dog("sanjiang")
print("firsthand change...")
print(d1.nationality,d2.nationality)
print("brfore change ...")
d1.nationality = "CN"    #对象的d1修改公共属性得值
print(d1.nationality,d2.nationality)
print("after change ....")
dog.nationality = "US"    #dog类本省修改公共属性的值
print(d1.nationality,d2.nationality)
 
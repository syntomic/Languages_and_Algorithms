class SchoolMember(object):
    '''学校成员基类'''
 
    member = 0  #设置类属性
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex =sex
        self.enroll()  #每次生成一个对象注册一次
    def enroll(self):
        "注册"
        print("just enroll a new school member [{0}]".format(self.name))
        SchoolMember.member += 1
 
    def tell(self):
        print("------info:{0}-----".format(self.name))
        for k,v in self.__dict__.items():  #__dict__()函数是获取对象的属性，以字典的形式返回
            print("\t",k,v)
        print("------end--------")
 
    def __del__(self):
        print("开除了[{0}]...".format(self.name))
        SchoolMember.member -= 1
 
class Teacher(SchoolMember):
    "讲师类"
 
    def __init__(self,name,age,sex,salary,course):
        SchoolMember.__init__(self,name,age,sex)
        self.salary = salary
        self.course = course
 
    def teaching(self):
        "讲课方法"
        print("Teacher [{0}] is teaching [{1}]".format(self.name,self.course))
 
class Student(SchoolMember):
    "学生类"
    def __init__(self,name,age,sex,couser,tuition):
        SchoolMember.__init__(self,name,age,sex)
        self.couser = couser
        self.tuition = tuition
        self.amount = 0
 
    def pay_tuition(self,amount):
        print("student [{0}] has just paied [{1}]".format(self.name,amount))
        self.amount += amount
 
t1 = Teacher("xiaogao",18,"F*M",3000,"Python")
s1 = Student("shuaigao",19,"M","PYS15",300000)
s2 = Student("gaogao",12,"M","PYS15",11000)
 
print(SchoolMember.member)

del s1  #删除一个变量
t1.tell()
s2.tell()
#print(SchoolMember.member) #会执行__del__函数
 
import datetime

from .person import Person

class Staff(Person):
    _id_num = 0

    @classmethod
    def _id_gen(cls, birthday):
        cls._id_num += 1
        birth_year = datetime.date(*birthday).year
        return "0{:04}{:05}".format(birth_year, cls._id_num)

    def __init__(self, name, sex, birthday, entry_date = None):
        super().__init__(name, sex, birthday, Staff._id_gen(birthday))
        if entry_date:
            try:
                self._entry_date = datetime.date(*entry_date)
            except:
                raise ValueError("Wrong date: ", entry_date)
        else:
            self._entry_date = datetime.date.today()
        self._salary = 1720
        self._department = "未定"
        self._position = "未定"

    def set_salary(self, amount):
        if not type(amount) is int:
            raise TypeError
        self._salary = amount

    def set_position(self, position):
        self._position = position
    
    def set_department(self, department):
        self._department = department

    def details(self):
        return ", ".join((super().details(), 
                        "入职日期: " + str(self._entry_date),
                        "院系: " + self._department,
                        "职位: " + self._position,
                        "工资: " + str(self._salary)))

if __name__ == "__main__":
    p1 = Staff("张子玉", "女", (1974, 10, 16))
    p2 = Staff("李国栋", "男", (1962, 5, 24))

    print(p1)
    print(p2)

    p1.set_department("数学")
    p1.set_position("副教授")
    p1.set_salary(8400)

    print(p1.details())
    print(p2.details())
        
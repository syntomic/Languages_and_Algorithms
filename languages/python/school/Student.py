from .person import Person
import datetime


class Student(Person):
    _id_num = 0

    @classmethod
    def _id_gen(cls):
        cls._id_num += 1
        year = datetime.date.today().year
        return "1{:04}{:05}".format(year, cls._id_num)

    def __init__(self, name, sex, birthday, department):
        Person.__init__(self, name, sex, birthday, Student._id_gen())
        self._department = department
        self._enroll_date = datetime.date.today()
        self._courses = {}

    def set_course(self, course_name):
        self._courses[course_name] = None

    def set_score(self, course_name, score):
        if course_name not in self._courses:
            raise ValueError("No this course selected: ", course_name)
        self._courses[course_name] = score

    def scores(self):
        return [(cname, self._courses[cname]) for cname in self._courses]

    def details(self):
        return ", ".join((super().details(),
                         "入学日期: " + str(self._enroll_date),
                         "院系: " + self._department,
                         "课程记录: " + str(self.scores())))

if __name__ == "__main__":
    p1 = Student("谢雨洁", "女", (1995, 7, 30), "数学系")
    p2 = Student("王立强", "男", (1990, 2, 17), "计算机系")

    print(p1)
    print(p2)

    p1.set_course("数据结构")
    p1.set_score("数据结构", 90)

    print(p1.details())
    print(p2.details())
        
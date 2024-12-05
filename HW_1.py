class person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married
    def introduce_myself(self):
        print(f'My name is {self.full_name}, i`m {self.age}. I am {self.is_married}')


aisuluu = person('aisuluu', 16, 'not married')
aisuluu.introduce_myself()


class Student(person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks

    def average_marks(self):
        return sum(self.marks.values())/len(self.marks)

    def create_student(self):
        student_1 = Student('asema', 16, 'not married',marks={'math': 5, 'biology': 4, 'geography':4})
        student_2 = Student('aruuke', 15, 'not married',marks={'math': 2, 'biology': 3, 'geography':3})
        student_3 = Student('aisuluu', 16, 'not married',marks={'math': 4, 'biology': 4, 'geography':5})

        students_list = [student_1, student_2, student_3]
        return students_list

students_list =Student.create_student(Student)

for char in students_list:
        char.introduce_myself()
        print(f'marks: {char.marks}')
        print(f'average marks: {char.average_marks()}')



class teacher(person):
    base_salary = 27000
    def __init__(self, full_name, age, is_married,experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        bonus_year= max(0, self.experience-3)
        bonus_salary = self.base_salary*0.05* bonus_year
        return bonus_salary+self.base_salary

math_teacher = teacher('Tamara viktorovna', 48, 'married', 15)
math_teacher.introduce_myself()
print(f'My salary before``base salary``: {math_teacher.base_salary}')
print(f'my salary now: {math_teacher.calculate_salary()}')





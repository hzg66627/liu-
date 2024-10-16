class Student:
    def __init__(self, group_number, average_score, name, age):
        self.group_number = group_number
        self.average_score = average_score
        self.name = name
        self.age = age

    def display_info(self):
        print(f"ФИО: {self.name}, Возраст: {self.age}, Группа: {self.group_number}, Средний балл: {self.average_score}")

    def scholarship(self):
        if self.average_score == 5:
            return 6000
        elif self.average_score < 5:
            return 4000
        else:
            return 0

    def compare_scholarship(self, other):
        if self.scholarship() > other.scholarship():
            return "мой размер стипендии больше"
        elif self.scholarship() < other.scholarship():
            return "мой размер стипендии меньше"
        else:
            return "размеры стипендий равны"


class GraduateStudent(Student):
    def __init__(self, group_number, average_score, name, age, research_work):
        super().__init__(group_number, average_score, name, age)
        self.research_work = research_work

    def display_info(self):
        super().display_info()
        print(f"Название научной работы: {self.research_work}")

    def scholarship(self):
        if self.average_score == 5:
            return 8000
        elif self.average_score < 5:
            return 6000
        else:
            return 0


# Example usage:
student = Student(group_number=12, average_score=4.8, name="Иванов Иван", age=20)
graduate_student = GraduateStudent(group_number=12, average_score=5, name="Петров Петр", age=24, research_work="Название научной работы")

print(student.display_info())
print(f"Размер стипендии: {student.scholarship()}р")

print(graduate_student.display_info())
print(f"Размер стипендии: {graduate_student.scholarship()}р")

print(student.compare_scholarship(graduate_student))
class Student:
    max_grade = 5

    def __init__(self, name: str, surname: str, record_book_number: int, grades: list):
        self.name = name
        self.surname = surname
        self.record_book_number = record_book_number
        for grade in grades:
            if grade < 0 or grade > self.max_grade:
                raise ValueError('Grade is out of range')
        self.grades = grades

    def __str__(self):
        return f"{self.name} {self.surname}"

    def calculate_average(self):
        return sum(self.grades)/len(self.grades)


class Group:
    max_students = 20

    def __init__(self, name: str):
        self.__group_name = name
        self.__group = []

    def print_group(self):
        for student in self.__group:
            return student

    def __str__(self):
        return f"{self.__group_name} {self.__group}"

    def add_student(self, student: Student):
        if len(self.__group) > self.max_students:
            raise ValueError("group can include only 20 students")
        for group_student in self.__group:
            if (student.name, student.surname) == (group_student.name, group_student.surname):
                raise Exception(f"student {student.name} {student.surname} already exists in the group")
        self.__group.append(student)

    def calculate_highest(self):
        average_list = []
        for student in self.__group:
            average_list.append(student)

        average_list.sort(key=lambda student: student.calculate_average())
        return average_list[-5:]


group1 = Group("TB-12")
student1 = Student("Rick", "Astley", 0, [5, 5, 5, 5])
print(student1)
group1.add_student(Student("Rick", "Astley", 0, [5, 5, 5, 5]))
group1.add_student(Student("Ivan", "Dot", 1, [1, 2, 3, 4]))
group1.add_student(Student("Nick", "Pop", 2, [3, 3, 3, 5]))
group1.add_student(Student("Jasmine", "Jo", 3, [1, 3, 3, 3]))
group1.add_student(Student("Hulk", "Benner", 4, [5, 5, 5, 5]))
group1.add_student(Student("Chris", "Evans", 5, [4, 5, 4, 5]))
group1.add_student(Student("Bucky", "Barnes", 6, [5, 5, 4, 4]))
group1.add_student(Student("Scarlet", "Johansson", 7, [4, 3, 3, 4]))
good_students = group1.calculate_highest()
for student in good_students:
    print(f"{student.name} {student.surname}", sep="\n")

print(group1)

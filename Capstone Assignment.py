# a) Base class Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# b) Derived class Student
class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display(self):
        super().display()
        print("Course:", self.course)


# c) Derived class Exam
class Exam(Student):
    def __init__(self, name, age, course, a1, a2, a3):
        super().__init__(name, age, course)
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.total = self.a1 + self.a2 + self.a3

    def display(self):
        super().display()
        print("Marks:")
        print("  Subject 1:", self.a1)
        print("  Subject 2:", self.a2)
        print("  Subject 3:", self.a3)
        print("Total Marks:", self.total)


# d) Instantiation and display
e = Exam("Sneha Kumari", 18, "Computer Science", 88, 92, 85)
e.display()

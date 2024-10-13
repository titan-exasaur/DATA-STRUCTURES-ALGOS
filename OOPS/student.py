class Student:

    class_year = 2024 # <-- class variable
    num_students = 0 # <-- class variable

    def __init__(self, name, age):
        self.name = name # <-- instance variable
        self.age = age # <-- instance variable
        Student.num_students += 1

student1 = Student('John', 20)
student2 = Student('Jane', 21)
student3 = Student('Joe', 22)
student4 = Student('Jill', 23)
student5 = Student('Jack', 24)
student6 = Student('Jenny', 25)

# accessing class variable
print(Student.class_year) 
print(Student.num_students)

# accessing instance variable
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)
print(student5.name)
print(student6.name)
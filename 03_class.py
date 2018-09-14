class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person_1 = Person("Vaijyant", 24)
print(person_1.name)


class Teacher(Person):
    def __init__(self, name, age, subject):
        Person.__init__(self, name, age)
        self.subject = subject

teacher_English = Teacher("James", 34, "English")

print(teacher_English.name)
print(teacher_English.age)
print(teacher_English.subject)
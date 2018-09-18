class Person:
    def Person():
        print("hi Person")

    def __init__(self, first, last):
        print("hi form __init__")
        self.firstname = first
        self.lastname = last
    
    def name(self):
        return self.firstname + " " + self.lastname


class Employee(Person):
    def __init__(self, first, last, staffnumber):
        Person.__init__(self, first, last)
        self.staffnumber = staffnumber
    
    def getEmployee(self):
        return self.name() + ", " + self.staffnumber

x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson", "1007")

print(x.name())
print(y.getEmployee())
class Person:
    greeting = "Hello"
    def __init__(self, name):
        self.first_name = name.split(" ")[0]
        self.last_name = name.split(" ")[1]



james = Person("James Potter")
print(james.first_name)
print(james.last_name)
print(james.greeting)

print("================")

kim = Person("Kim Possible")
print(kim.first_name)
print(kim.last_name)
print(kim.greeting)

print("================")

Person.greeting = "Ola"
print(james.greeting)
print(kim.greeting)

print("================")

james.greeting = "Namaste"
print(james.greeting)
print(kim.greeting)


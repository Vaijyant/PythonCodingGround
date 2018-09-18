class Animal:
    kind = 'Canine'
    def __init__(self, name):
        self.name = name
    
    def getName(self):
        return self.name

    def getKind(self):
        return self.kind

    def setKind(self, kind):
        self.kind = kind


animal1 = Animal('Bowwow')
print(animal1.getName())
print(animal1.getKind())

animal2 = Animal('Fiddo')
print(animal2.getName())
print(animal2.getKind())

Animal.kind = 'Feline' # notice animal kind
print(animal1.getKind())
print(animal2.getKind())


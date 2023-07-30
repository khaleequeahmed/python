class Animals:
    animalType = "Mammal"

class Pets(Animals):
    color = "White"

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow bow!")


a=Animals()
p=Pets()
# print(p.color)
print(p.animalType)
d=Dog
print(d.color)
d.bark()
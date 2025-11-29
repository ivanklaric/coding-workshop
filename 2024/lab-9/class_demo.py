class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("An animal called " + self.name +" speaks")

class Dog(Animal):        
    def speak(self):
        print(f"{self.name} says woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows")


list_of_animals = [Dog("Floki", 1), Cat("Micko", 3), Cat("Mica", 5), Dog("Rex", 7)]

print("printing speak() calls here:")
for animal in list_of_animals:
    animal.speak()
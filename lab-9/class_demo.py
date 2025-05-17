class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def bark(self):
        return f"{self.name} says woof!"

# Create an instance of the Dog class
my_dog = Dog("Rex", 3)
floki = Dog("Floki", 1)

# Access attributes and methods
print(my_dog.name)  # Rex
print(my_dog.age) # 3
print(my_dog.bark())  # Rex says woof!
print(floki.bark())
print(f"Floki is {floki.age} years old")
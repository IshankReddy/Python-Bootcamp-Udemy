class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

# Creating an object of Dog class
my_dog = Dog("Buddy", 3)

# Accessing attributes
print(f"My dog's name is {my_dog.name} and he is {my_dog.age} years old.")
print(my_dog.bark())
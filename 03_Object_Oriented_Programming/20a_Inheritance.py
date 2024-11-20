# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Child class (inherits from Animal)

class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent class's constructor
        self.breed = breed

    def speak(self):
        return f"{self.name} says Woof!"

# Child class (inherits from Animal)

class Cat(Animal):

    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers")

print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!
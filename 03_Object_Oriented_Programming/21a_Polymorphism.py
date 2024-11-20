class Animal:

    def speak(self):
        return "Some generic sound"

class Dog(Animal):

    def speak(self):
        return "Bark"

class Cat(Animal):
    
    def speak(self):
        return "Meow"

# Polymorphism in action
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())  # Output: Bark, Meow

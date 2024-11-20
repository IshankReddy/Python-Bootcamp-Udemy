class Dog:
    
    # Constructor method to initialize the object
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    # Method to describe the dog
    def bark(self):
        return f"{self.name} says: Woof!"

    # Method to get the dog's details
    def get_details(self):
        return f"{self.name} is a {self.age}-year-old {self.breed}."

# Creating instances (objects) of the class Dog
dog1 = Dog("Buddy", "Golden Retriever", 3)
dog2 = Dog("Max", "Bulldog", 5)

# Calling methods on the objects
print(dog1.bark())
print(dog2.get_details())
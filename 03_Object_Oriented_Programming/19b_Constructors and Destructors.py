class Dog:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"{self.name} is being destroyed.")

# Creating an object of Dog class
my_dog = Dog("Buddy")

# Deleting the object
del my_dog

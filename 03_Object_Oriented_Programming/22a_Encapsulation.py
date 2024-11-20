class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self._mileage = 0
        self.__engine_status = "Off"

    def start_engine(self):
        self.__engine_status = "On"
        print(f"The engine is now {self.__engine_status}")

    def drive(self, miles):
        self._mileage += miles
        print(f"The car has now driven {self._mileage} miles")

my_car = Car("Toyota", "Camry")
my_car.start_engine()  # Works fine
my_car.drive(10)       # Works fine

print(my_car._mileage)
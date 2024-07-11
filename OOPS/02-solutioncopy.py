
# make attribute read-only
class Car:

    # Class variable
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand  # adding two underscores before the variable name makes it private
        self.__model = model
        Car.total_car += 1 # or self.total_car += 1
    
    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):  # Polymorphism
        return "Petorl or Diesel"
    
    @property            # this decorator used for making attributes read only
    def model(self):
        return self.__model
    
    # static method
    @staticmethod
    def general_description():
        return "Cars are vehicles that are used for transportation."
    

# Inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self): # Polymorphism
        return "Electric charge"

# Encapsulation
my_tesla = ElectricCar("Tesla", "Model S", "100kWh")


my_car = Car("Toyota", "Corolla")
# my_car.model = "City"
print(my_car.model) # Adding property decorator makes the attribute read-only in the class, and now we can access it just by model and not model()



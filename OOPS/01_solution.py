# class Car:
#     brand = None
#     model = None

# my_car = Car()
# print(my_car)

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
    
#     def full_name(self):
#         return f"{self.brand} {self.model}"

# Encapsulation
class Car:
    def __init__(self, brand, model):
        self.__brand = brand  # adding two underscores before the variable name makes it private
        self.model = model
    
    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):  # Polymorphism
        return "Petorl or Diesel"
    

# Inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self): # Polymorphism
        return "Electric charge"


# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.model)

# Inheritance
# my_tesla = ElectricCar("Tesla", "Model S", "100kWh")
# print(my_tesla.model)
# print(my_tesla.full_name())

# Encapsulation
my_tesla = ElectricCar("Tesla", "Model S", "100kWh")
# print(my_tesla.brand) # after making it private by adding two underscores, we can't access it directly: AttributeError: 'ElectricCar' object has no attribute 'brand'
# print(my_tesla.__brand) # Still cannot access it directly: AttributeError: 'ElectricCar' object has no attribute '__brand'
# print(my_tesla.get_brand())

# Polymorphism
print(my_tesla.fuel_type())

safari = Car("Tata", "Safari")
print(safari.fuel_type())
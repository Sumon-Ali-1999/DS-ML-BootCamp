class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass
my_bus = Bus("School Bus", 60, 100000)
print(my_bus.name)     
print(my_bus.max_speed) 
print(my_bus.mileage)   

# ACTIVITY 1
# Design your own class (choosing SmartPhone)
# add attributes, methods to bring class to life
# use constructors to initialize each object with unique values
# add inheritance layer to explore polymorphism or encapsulataion.

class SmartPhone:
    def __init__(self, processor, ram, camera, storage):
        self.processor = processor
        self.ram = ram
        self.camera = camera
        self.storage = storage

    def power_on(self):
        print(f"{self.processor} smartphone is powering on...")

    def make_call(self, number):
        print(f"Calling {number}...")

    def power_off(self):
        print("Powering off...")

# inheritance
class Iphone(SmartPhone):
    def __init__(self, model, processor, ram, camera, storage):
        super().__init__(processor, ram, camera, storage)
        self.model = model

    def power_on(self):
        print(f"{self.model} is booting up with Apple logo...")


# Polymorphism demo
class Iphone14(Iphone):
    def get_ram(self):
        return "256GB"


class Iphone13(Iphone):
    def get_ram(self):
        return "128GB"


# Create and demonstrate
for model in [Iphone14("iPhone 14", "A16 Bionic", "6GB", "48MP", "256GB"),
              Iphone13("iPhone 13", "A15 Bionic", "4GB", "12MP", "128GB")]:
    model.power_on()
    print(f"{model.model} RAM: {model.get_ram()}")

# ACTIVITY 2
# Base class
class Vehicle:
    def move(self):
        print("The vehicle is moving...")

# Subclasses (each defines move() differently)
class Car(Vehicle):
    def move(self):
        print("🚗 The car is driving on the road.")

class Plane(Vehicle):
    def move(self):
        print("✈️ The plane is flying in the sky.")

class Boat(Vehicle):
    def move(self):
        print("⛵ The boat is sailing on the water.")

class Train(Vehicle):
    def move(self):
        print("🚆 The train is running on the rails.")


# List of different vehicle objects (polymorphism in action)
vehicles = [Car(), Plane(), Boat(), Train()]

# Loop through each object and call move()
for vehicle in vehicles:
    vehicle.move()

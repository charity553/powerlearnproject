# classes(blueprint) objects(attributes) methods(actions)

# defining a class
class Car:
    color = "red" # attribute

    # method
    def drive(self):
        print("The car is driving")

# creating an object
my_car = Car()
print(my_car.color)
my_car.drive()
''' class Vehicle:
    def __init__(self,wheels):
        self.wheels= wheels

class Car(Vehicle):
    pass

car =Car(4)
print(car.wheels) '''

# polymorphism
''' class Dog:
    def speak(self):
        return "woof!"
    
class Cat:
    def speak(self):
        return "meaow"
    
for animal in [Dog(), Cat()]:
    print(animal.speak()) '''

# Encpsulation
class SecretStash:
    def __init__(self):
        self.__chocolates = 10 # private attribute

    def take_chocolate(self):
        if self.__chocolates > 0:
            self.__chocolates -= 1
            print("One chocolate taken!")
        else:
            print("No chocolates left")

statsh = SecretStash()
statsh.take_chocolate()
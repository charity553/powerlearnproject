class Car:
    def __init__(self,color,model):
        self.color = color
        self.model = model

# creating objects with unique attributes
car1 = Car("blue","Sedan")
car2 = Car("Gold", "Corolla")

print(car1.color)
print(car2.color)
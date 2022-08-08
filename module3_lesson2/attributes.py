#creating a class called Car
#creating attributes
class Car:
    print("Car Attributes") 
    def __init__(self, name, model, colour, year, amount):
        self.name = name
        self.model = model
        self.colour = colour
        self.year = year
        self.amount =amount
    
#first car
first_car = Car(name= "Benz", model= "Eclass", colour= "Grey", year= "2020", amount= "3000000")

print(first_car.name)
print(first_car.model)
print(first_car.colour)
print(first_car.year)
print(first_car.amount)
  
   
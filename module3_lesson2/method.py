#methods for Car class
class Car ():
    def __init__(self, speed = "60km_per_hour", travel = "Abuja", feul = "10_litres", charge = "phone", park = "car_park"):
       self.speed = speed
       self.travel = travel
       self.feul = feul
       self.charge = charge
       self.park = park
       
       
       
       print("self.speed:" , speed)
       print("self.travel:", travel)
       print("self.feul:", feul)
       print("self.charge:", charge)
       print("self.park:", park)
       
       Car()        

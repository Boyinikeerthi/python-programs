class Vehicle:
    def __init__(self,name,type1):
        self.name=name
        self.type1=type1
    def details(self):
        print(f"vehicle Details:{self.type1} Name:{self.name}")
class Car(Vehicle):
    def __init__(self,name,type1,capacity,millage):
        super().__init__(name,type1)
        self.capacity=capacity
        self.millage=millage
    def car_details(self):
        print(f"Car capacity:{self.capacity} millage:{self.millage}")
bike=Vehicle("Activa","2Wheeler")       
bike.details()
car=Car("skoda","4Wheeler",4,20)
car.details()
car.car_details()

    

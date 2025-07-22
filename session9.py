class Father:
    def __init__(self, fname, lname): 
        self.fname = fname
        self.lname = lname
    haircolor = "Black"
    def work(self):
        return "I want to work 12 hrs a day"
class Son(Father):
    def __init__(self, fname, lname, nick): 
        self.fname = fname
        self.lname = lname
        self.nick=nick
class Daughter(Father):
    def __init__(self, fname, lname): 
        self.fname = fname
        self.lname = lname
    def work(self):
        return "I don't want to work 12 hrs a day" 
f = Father("Parashuram", "Shinde")
s = Son("Om Aryan", "Shinde","Bacchu")
d= Daughter("Adithi","Shinde")
print(f.fname,f.lname)  
print(s.fname,s.lname)
print(d.fname,d.lname)
print(f.work())     
print(s.work())

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats
class Bike(Vehicle):
    def __init__(self, brand, model, bike_type):
        super().__init__(brand, model)
        self.bike_type = bike_type
car = Car("Suzuki", "Breeza", 5)
bike = Bike("Honda", "CBR500R", "Sport")
print(f"Car: {car.brand}, {car.model}, Seats: {car.seats}")
print(f"Bike: {bike.brand}, {bike.model}, Type: {bike.bike_type}")


class A:
    x=3
class B(A):
    pass
class C(B):
    pass
c=C()
print(c.x)

class Add:
    def add(self,x,y,z=None):
        if z is None:
            return x+y
        return x*y*z
a=Add()
print(a.add(3,6,8))

from abc import ABC, abstractmethod
class Appliance(ABC):
    @abstractmethod
    def power_consumption(self):
        pass
class WashingMachine(Appliance):
    def power_consumption(self, hours):
        return f"Washing Machine consumes {hours * 0.5} kWh"
class Refrigerator(Appliance):
    def power_consumption(self, hours):
        return f"Refrigerator consumes {hours * 0.2} kWh"
wm = WashingMachine()
fridge = Refrigerator()
print(wm.power_consumption(5))
print(fridge.power_consumption(24))


class Vehicle(object):
    
    sale_multiplier = 1
    purchase_multiplier = 1
    
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles
        
    def sale_price(self):
        return self.base_price * self.sale_multiplier
    def purchase_price(self):
        return self.sale_price() - (self.purchase_multiplier * self.miles)

class Car(Vehicle):
    sale_multiplier = 1.2
    purchase_multiplier = 0.004
    interest = 1.07
    lease_multiplier = 1.2

class Motorcycle(Vehicle):
    sale_multiplier = 1.1
    purchase_multiplier = 0.009 
    interest = 1.03
    lease_multiplier = 1
    
class Truck(Vehicle):
    sale_multiplier = 1.6
    purchase_multiplier = 0.02
    interest = 1.11
    lease_multiplier = 1.7
 


"""
my_car = Car(maker='ford')
your_car = Car(maker='gmc')

my_truck.my_method()

my_car.maker"""
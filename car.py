class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
    def display_all(self):
        print "Price:", self.price
        print "Speed:", self.speed
        print "Mileage:", self.mileage
        print "Tax:", self.tax
        print ""
        return self

car1 = Car(2000, "45mph", "Not Full", "12mpg")
car2 = Car(22000, "145mph", "Full", "32mpg")
car3 = Car(12000, "95mph", "Kind ofFull", "25mpg")
car4 = Car(2000, "25mph", "Half", "15mpg")
car5 = Car(15000, "100mph", "Full", "47mpg")
car6 = Car(2000, "15mph", "Empty", "22mpg")

car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()
car6.display_all()
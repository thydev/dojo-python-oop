class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print "Bike information: Price: {}, Max Speed: {}, Mileage: {}".format(self.price, self.max_speed, self.miles)
        return self
    def ride(self):
        print "Riding"
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing"
        self.miles -= 5
        if self.miles < 0:
            self.miles = 0
        return self
    def __repr__(self):
        return "<Bike object Price: {} Speed: {} Mileage: {}>".format(self.price, self.max_speed, self.miles)
if __name__ == "__main__":
    bike1 = Bike(200, "20mph")
    bike1.displayInfo()
    bike2 = Bike(400, "30mph")
    bike2.displayInfo()
    bike3 = Bike(1500, "25mph")
    bike3.displayInfo()

    bike1.ride().ride().ride().reverse()
    bike2.ride().ride().reverse().reverse()
    bike3.reverse().reverse().reverse()
    bike1.displayInfo()
    bike2.displayInfo()
    bike3.displayInfo()
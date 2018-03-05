class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self

    def add_tax(self, tax_amount):
        self.price += tax_amount
        return self.price

    def return_product(self, reason):
        if reason == "defective":
            self.price = 0
            self.status = reason
        elif reason == "inthebox":
            self.status = "for sale"
        elif reason == "openedbox":
            self.status = "used"
            self.price -= (self.price * 0.2)
        else:
            pass
        return self
    
    def display_info(self):
        print "Product:", self.item_name
        print "Price:", self.price
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Status:", self.status
        print ""
        return self
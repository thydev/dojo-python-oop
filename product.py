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
    def __repr__(self):
        return "<Product object {} Price: {} Status: {}>".format(self.item_name, self.price, self.status)

if __name__ == "__main__":
    product1 = Product(1200, "Surface Pro 1", "0.5lbs", "Microsoft1")
    product2 = Product(1500, "Surface Pro 2", "0.4lbs", "Microsoft2")
    product3 = Product(1700, "Surface Pro 3", "0.35lbs", "Microsoft3")
    product4 = Product(3000, "Surface Pro 4", "0.25lbs", "Microsoft4")

    product1.add_tax(150)
    product2.add_tax(170)
    product3.return_product("defective")
    product4.return_product("openedbox")
    product1.return_product("inthebox")

    product1.display_info()
    product2.display_info()
    product3.display_info()
    product4.display_info()
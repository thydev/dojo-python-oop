class Store(object):
    def __init__(self, address, owner):
        self.address = address
        self.owner = owner
        self.products = {}
    def add_product(self, obj_product):
        # Set item_name as a key of the dictionary
        self.products[obj_product.item_name] = obj_product
        return self
    def remove_product(self,obj_product):
        #  Remove the product form dictionary by key
        self.products.pop(obj_product.item_name)
        return self
    def inventory(self):
        print "Inventory at", self.address
        for p in self.products.itervalues():
            p.display_info()

if __name__ == "__main__":
    print "Do your local tests"
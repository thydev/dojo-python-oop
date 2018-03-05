import datetime
import dog, dragon
import call_center, bike, hospital, product

dog1 = dog.Dog("Koka")
dog1.walk().walk().walk().run().run().pet()
dog1.display_health()
print dog1

dragon1 = dragon.Dragon("Draga")
dragon1.walk().walk().walk().run().run().fly()
dragon1.display_health()
print dragon1

caller1 = call_center.call.Call("c1", "Toto", "123-123-1234", datetime.datetime.now(), "Reason1")
caller2 = call_center.call.Call("c2", "Fata", "223-223-2234", datetime.datetime.now(), "Reason2")
caller3 = call_center.call.Call("c3", "TDodo", "323-323-1234", datetime.datetime.now(), "Reason3")
caller4 = call_center.call.Call("c4", "Anama", "443-424-2234", datetime.datetime.now(), "Reason4")
caller5 = call_center.call.Call("c5", "Fnema", "453-524-5234", datetime.datetime.now(), "Reason5")

cc1 = call_center.CallCenter()
cc1.add(caller1).add(caller5).add(caller2).add(caller3).add(caller4)
cc1.info()
cc1.remove()
cc1.remove_by_phone("323-323-1234")
cc1.remove_by_phone("555-553-1234") # Do nothing
cc1.info()
cc1.sort().info()
print cc1

bike1 = bike.Bike(200, "20mph")
bike1.displayInfo()
bike2 = bike.Bike(400, "30mph")
bike2.displayInfo()
print bike2

p1 = hospital.patient.Patient("p1", "Dodo", "Milk")
p2 = hospital.patient.Patient("p2", "CoCo", "Coffe")
p3 = hospital.patient.Patient("p3", "Sodo", "Cheese")
p4 = hospital.patient.Patient("p4", "FoFo", "Banana")
p5 = hospital.patient.Patient("p5", "Vodo", "Apple")

h = hospital.Hospital("Ever Green", 3)
h.admit(p1, "bed101")
h.admit(p2, "bed201")
h.admit(p3, "bed1234")
h.admit(p4, "bed1235")
h.admit(p5, "bed1236")

h.discharge("p3")
h.display_info()
print h
print p1

product1 = product.Product(1200, "Surface Pro 1", "0.5lbs", "Microsoft1")
product2 = product.Product(1500, "Surface Pro 2", "0.4lbs", "Microsoft2")
product3 = product.Product(1700, "Surface Pro 3", "0.35lbs", "Microsoft3")
product4 = product.Product(3000, "Surface Pro 4", "0.25lbs", "Microsoft4")

product1.add_tax(150)
product2.add_tax(170)
product3.return_product("defective")
product4.return_product("openedbox")
product1.return_product("inthebox")

product1.display_info()
product2.display_info()
product3.display_info()
product4.display_info()
print product1
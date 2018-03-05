import product
import store 

product1 = product.Product(1200, "Surface Pro 1", "0.5lbs", "Microsoft1")
product2 = product.Product(1500, "Surface Pro 2", "0.4lbs", "Microsoft2")
product3 = product.Product(1700, "Surface Pro 3", "0.35lbs", "Microsoft3")
product4 = product.Product(3000, "Surface Pro 4", "0.25lbs", "Microsoft4")

store1 = store.Store("111 Main St. Bellevue", "Toto Great")
store1.add_product(product1).add_product(product2).add_product(product3).add_product(product4)
store1.remove_product(product2)
store1.inventory()

# import product as p
# import store as s

# product1 = p.Product(1200, "Surface Pro 1", "0.5lbs", "Microsoft1")
# product2 = p.Product(1500, "Surface Pro 2", "0.4lbs", "Microsoft2")
# product3 = p.Product(1700, "Surface Pro 3", "0.35lbs", "Microsoft3")
# product4 = p.Product(3000, "Surface Pro 4", "0.25lbs", "Microsoft4")

# store1 = s.Store("111 Main St. Bellevue", "Toto Great")
# store1.add_product(product1).add_product(product2).add_product(product3).add_product(product4)
# store1.remove_product(product2)
# store1.inventory()
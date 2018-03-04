class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print "Health:", self.health
        return self

animal1 = Animal("Toto", 200)
animal1.walk().walk().walk().run().run()
animal1.display_health()

class Dog(Animal):
    def __init__(self, name, health = 150):
        super(Dog, self).__init__(name,health)
        # self.name = name
        # self.health = health
    def pet(self):
        self.health += 5

dog1 = Dog("Kiki")
dog1.walk().walk().walk().run().run().pet()
dog1.display_health()

class Dragon(Animal):
    def __init__(self, name, health = 170):
        super(Dragon, self).__init__(name, health)
        # self.name = name
        # self.health = health
    def fly(self):
        self.health += 10
    def display_health(self):
        print "I am Dragon"
        super(Dragon, self).display_health()

dragon1 = Dragon("Drogo")
dragon1.walk().walk().walk().run().run().fly()
dragon1.display_health()
# dragon1.pet() # Error
animal2 = Animal("T1ta", 500)
animal2.walk().walk().walk().run().run()
animal2.display_health()
import animal
class Dog(animal.Animal):
    def __init__(self, name, health = 150):
        super(Dog, self).__init__(name,health)
        # self.name = name
        # self.health = health
    def pet(self):
        self.health += 5
    def __repr__(self):
        return "<Dog object {} health {}>".format(self.name, self.health)

if __name__ == "__main__":
    dog1 = Dog("Kiki")
    dog1.walk().walk().walk().run().run().pet()
    dog1.display_health()
    print dog1
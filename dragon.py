import animal
class Dragon(animal.Animal):
    def __init__(self, name, health = 170):
        super(Dragon, self).__init__(name, health)
        # self.name = name
        # self.health = health
    def fly(self):
        self.health += 10
    def display_health(self):
        print "I am Dragon"
        super(Dragon, self).display_health()
    def __repr__(self):
        return "<Dragon object {}, health {}>".format(self.name, self.health)

if __name__ == "__main__":
    dragon1 = Dragon("Drogo")
    dragon1.walk().walk().walk().run().run().fly()
    dragon1.display_health()
    print dragon1
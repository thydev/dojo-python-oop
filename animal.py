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
    def __repr__(self):
        return "<Animal objec {}, health {}>".format(self.name, self.health)
if __name__ == "__main__":
    animal1 = Animal("Toto", 200)
    animal1.walk().walk().walk().run().run()
    animal1.display_health()

    animal2 = Animal("T1ta", 500)
    animal2.walk().walk().walk().run().run()
    animal2.display_health()
    
    print animal1
    print animal2
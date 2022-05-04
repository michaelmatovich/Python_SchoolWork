import ninjaClass

class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
    
    def sleep(self):
        print(f"{self.name} takes a nap.")
    
    def eat(self):
        print(f"{self.name} eats food from the food dish.")

    def play(self):
        print(f"{self.name} is playing around.")
    
    def noise(self):
        print(f"{self.name} makes a loud noise.")

print("Hey Pet")
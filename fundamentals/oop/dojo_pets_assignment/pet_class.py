import random

class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
    
    def sleep():
        print(f"{self.name} takes a nap.")
    
    def eat():
        print(f"{self.name} eats food from the food dish.")



class Dog (Pet):
    def __init__(self, name, tricks, health, energy):
        super().__init__(name, health, energy)
        self.type = "dog"
        self.tricks = ["roll over", "play dead", "fetch"]

    def play():
        rndNum = random.randrange(0,3)
        if(rndNum==0):
            print(f"{self.name} rolls over on the floor.")
        elif(rndNum==1):
            print(f"{self.name} plays dead.")
        else:
            print(f"{self.name} plays fetch.")

    def noise():
        print(f"{self.name} barks loudly!")

class Cat (Pet):
    def __init__(self, name, tricks, health, energy):
        super().__init__(name, health, energy)
        self.type = "cat"
        self.tricks = ["plays with string", "claws the furniture", "ignores you"]

    def play():
        rndNum = random.randrange(0,3)
        if(rndNum==0):
            print(f"{self.name} plays with string on the floor.")
        elif(rndNum==1):
            print(f"{self.name} claws at the furniture.")
        else:
            print(f"{self.name} completely ignores everything.")

    def noise():
        print(f"{self.name} meows!")
    
    
    
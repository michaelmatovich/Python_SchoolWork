from ninja_class import *

# class Ninja:
#     def __init__(self, first_name, last_name, pet, treats, pet_food):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.pet = pet
#         self.treats = treats
#         self.pet_food = pet_food

#     def walk(self):
#         print(f"{self.first_name} takes {self.pet.name} out for a walk.")
#         return self
    
#     def feed(self, food):
#         if(food == self.treats):
#             print(f"{self.first_name} gives {self.pet.name} a treat of {food}.")
#         if(food == self.pet_food):
#             print(f"{self.first_name} gives {self.pet.name} a meal of {food}.")
#         return self
        
#     def bathe(self):
#         if(self.pet.type == "dog"):
#             print(f"{self.first_name} gives {self.pet.name} a bath.\n{self.pet.name} shakes water all over the house to get dry.")
#         if(self.pet.type == "cat"):
#             print(f"{self.first_name} gives {self.pet.name} a bath.\n{self.pet.name} is very displased.")

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

class Dog (Pet):
    def __init__(self, name, type, tricks, health, energy):
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
    def __init__(self, name, type, tricks, health, energy):
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



michael = Ninja("Michael", "Matovich", Pet("Booboo", "cat", ["plays with string","claws furniture","ignores everything"], "Great", "100%"), "cat snacks", "Iams cat food")

michael.walk()
print()
michael.feed("cat snacks")
print()
michael.bathe()















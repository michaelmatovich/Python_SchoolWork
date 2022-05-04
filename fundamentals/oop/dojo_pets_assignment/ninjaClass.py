class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = Pet("Booboo", "cat", ["plays with string","claws furniture","ignores everything"], "Great", "100%")
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        print(f"{self.first_name} takes {self.pet.name} out for a walk.")
        return self
    
    def feed(self, food):
        if(food == self.treats):
            print(f"{self.first_name} gives {self.pet.name} a treat of {food}.")
        if(food == self.pet_food):
            print(f"{self.first_name} gives {self.pet.name} a meal of {food}.")
        return self
        
    def bathe(self):
        if(self.pet.type == "dog"):
            print(f"{self.first_name} gives {self.pet.name} a bath.\n{self.pet.name} shakes water all over the house to get dry.")
        if(self.pet.type == "cat"):
            print(f"{self.first_name} gives {self.pet.name} a bath.\n{self.pet.name} is very displased.")

print("Hey Ninja")





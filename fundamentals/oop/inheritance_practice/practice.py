class Monster:
    def __init__ (self,hp, mp, exp, type, gp):
        self.hp = hp
        self.mp = mp
        self.exp = exp
        self.type = type
        self.gp = gp
        self.test = 500
        self.test2 = 600
        self.test3 = 700
        self.special = "kick"
        
class Undead (Monster):
    def __init__ (self,hp,mp,exp,type,gp):
        super().__init__(hp,mp,exp,gp)
        self.type ="undead"
        




zombie = Monster(200,200,100, "undead", 50)
vampire = Undead(300,300,150,"test",350)



print(zombie.hp)
print(vampire.hp)

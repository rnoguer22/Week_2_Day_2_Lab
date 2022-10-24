# Soldier
class Soldier:
    def __init__(self, health, strength):
        # add code here
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        else:
            pass


# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength): 
        self.name = name
        super().__init__(health, strength)
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health < 0:
            return "{} has died in act of combat".format(self.name)
        else:
            return "{} has received {} points of damage".format(self.name, self.damage)
    
    def battleCry(self):
        return "Odin Owns You All!"
        

# Saxon
class Saxon:

# War
class War:
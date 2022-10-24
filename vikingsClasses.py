# Soldier
class Soldier:
    def __init__(self, health, strength):
        # add code here
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        daño_recibido = self.health - damage
        if daño_recibido < 0:
            self.health = 0
        else:
            pass


# Viking
class Viking:

# Saxon
class Saxon:

# War
class War:
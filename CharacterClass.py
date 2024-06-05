#Character / Unit Classes
import uuid

class Character:
    def __init__(self, name, cost = {}, move = 1, attack = 1, defense = 1, health = 1, abilities = {}, player = None):
            self.name = name
            self.cost = cost            #Cost is a Dictionary object with {"Resource": #}
            self.move = int(move)
            self.attack = int(attack)
            self.defense = int(defense)
            self.health = int(health)
            self.abilities = abilities  #abilities are in a Dictionary object with {"abilityName": abilityFunction}
            self.player = player
            self.id = uuid.uuid4().int  #Unique Identifier for created character
            self.status = "ok"

    def __repr__(self):
        return self.name
    def __str__(self):
        return self.name

    def _attack(self, target):
        print(f"{self} is attacking!")
        target.health = target.health - self.attack
        print(f"{self} deals {self.attack} damage to {target}")
        if target.health <= 0:
            target.status = "dead"
            print(f'{target} has died!')

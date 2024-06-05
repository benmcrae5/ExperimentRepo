#Character / Unit Classes
import uuid

class Character:
    def __init__(self, name, cost = {}, move = 1, attack = 1, defense = 1, health = 1, abilities = {}, player = None):
            self.name = name
            self.cost = cost            #Cost is a Dictionary object with {"Resource": #}
            self.move = move
            self.attack = attack
            self.defense = defense
            self.health = health
            self.abilities = abilities  #abilities are in a Dictionary object with {"abilityName": abilityFunction}
            self.player = player
            self.id = uuid.uuid4().int  #Unique Identifier for created character

    def __repr__(self):
        return self.name
    def __str__(self):
        return self.name

    

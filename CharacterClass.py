#Character / Unit Classes
import uuid
import BoardClass

class Character:
    def __init__(self, name, cost = {}, move = 1, attack = 1, defense = 1, health = 1, abilities = {}, location = None, player = None):
            self._name = name
            self._cost = cost            #Cost is a Dictionary object with {"Resource": #}
            self._move = int(move)
            self._attack = int(attack)
            self._defense = int(defense)
            self._health = int(health)
            self._abilities = abilities  #abilities are in a Dictionary object with {"abilityName": abilityFunction}
            self._location = location
            self._player = player
            self._status = "ok"
            self._id = uuid.uuid4().int  #Unique Identifier for created character
            self._moveOptions = None #determineReach(location, self._move)

    def __repr__(self):
        return self._name
    def __str__(self):
        return self._name

    def attack(self, target):
        print(f"{self} is attacking!")
        target._health = target._health - self._attack
        print(f"{self} deals {self._attack} damage to {target}")
        if target._health <= 0:
            target._status = "dead"
            print(f'{target} has died!')
            
    def determineReach(self, startingNode, move = 1):
        print("I can move to these spaces: (in progress)")
        
    def move(self):
        print(f"{self} is moving {self._move} spaces")
        # Check for available spaces
        # Prompt for choice
        # Change self_location to new location
            

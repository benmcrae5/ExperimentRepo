#Card Class

class CardAbility:
    def __init__(self, player, name, cost = 0, effect1, effect2):
        self.name = name
        self.cost = cost
        self.effects = [effect1, effect2]

    def __repr__(self):
        return self.name
    def __str__(self):
        return self.name
    
    def play(self, player, target = None):
        for effect in self.effects:
            effect(player, target)
        return cost

    
    
class Card:
    def __init__(self, player, name, value, suite, cost, text, abilities = []):
        self.name = name
        self.value = value
        self.suite = suite
        self.cost = cost
        self.text = text
        self.abilities = abilities
        self.player = player

    def __repr__(self):
        return self.name
    def __str__(self):
        return self.name

    def playAbility(self, abilityNum, target):
        self.abilites[abilityNum].play(self.player, target)

    

    

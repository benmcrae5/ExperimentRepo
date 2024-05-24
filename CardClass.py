#Card Class

class CardAbility:
    def __init__(self, name, cost = {}, effects = []):
        self.name = name
        self.cost = cost    #Cost is a Dictionary object with {"Resource": #}
        self.effects = []   #effects are methods with (player, target) parameters

    def __repr__(self):
        return self.name
    def __str__(self):
        return self.name
    
    def play(self, player, target = None):
        for effect in self.effects:
            effect(player, target)
        return cost

    
    
class Card:
    def __init__(self, player, name, value, suite, cost, text = "", abilities = []):
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

    def readCard(self):
        print(self.text)

    def assign(self, player):
        self.player = player

    def payCost(self):
        self.player.payCost(self.cost)

    

    

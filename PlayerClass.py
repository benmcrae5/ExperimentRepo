import DeckRandomizer as DeckR

#Generic player creation class
class Player:
    def __init__(self, name, cardHand= [], points= 0, life= 0, priority= 0, deck= [], resources= {}):
        self.name = name
        self.cardHand = cardHand
        self.points = points
        self.life = life
        self.priority = priority
        self.deck = deck
        self.resources = resources

    def __str__(self):
        return f'{self.name}'
    #note to self: repr prints when printing lists, str prints in print statments
    def __repr__(self):
        return f'Player(\'{self.name}\', {self.points}, {self.life}, {self.priority}) :: {self.cardHand}'

    #comparitive functions between Player Objects based on self.priority
    def __eq__(self, other):
        return self.name == other.name and self.priority == other.priority
    def __lt__(self, other):
        return self.priority < other.priority
    def __le__(self, other):
        return self.priority <= other.priority
    def __gt__(self, other):
        return self.priority > other.priority
    def __ge__(self, other):
        return self.priority >= other.priority

    #Player Functions
    def adjustLife(self, amount):
        self.life = self.life + amount

    def adjustPoints(self, amount):
        self.points = self.points + amount

    def drawCards(self, numCards):
        for x in range(numCards):
            if len(self.deck) <= 0:
                print(f'Not enough cards. You drew {x} instead')
                break
            self.cardHand.append(self.deck.pop())

    def adjustPriority(self, newPriority):
        self.priority = newPriority

    #Deck Operations
    def organizeDeck(self):
        self.deck.sort()

    def shuffleDeck(self):
        self.deck = DeckR.runChainShuffle(self.deck, 3)

    def addCardToDeck(self, card):
        self.deck.append(card)

    def removeCardFromDeck(self, card):
        self.deck.remove(card)

    def payCost(self, cost = {}):
        for key in cost:
            assert key in self.resources, "Resource does not exist"
            assert self.resources[key] >= cost[key], "Insufficient resources"
            self.resources[key] -= cost[key]
        return True
                

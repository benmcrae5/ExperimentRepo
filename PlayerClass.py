#Generic player creation class
class Player:
    def __init__(self, name, cardHand = [], points = 0, life = 0, priority=0):
        self.name = name
        self.cardHand = cardHand
        self.points = points
        self.life = life
        self.priority = priority

    def __str__(self):
        return f'{self.name}'

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

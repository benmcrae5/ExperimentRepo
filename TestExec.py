import DeckRandomizer as DeckR
import DiceRandomizer as DiceR
import PlayerClass as PC

#TEST FILE

p1 = PC.Player("adam", [1,2,3,4], 10, 40, 7, ['a','b','c','d'])

p1.drawCards(3)
print(p1.deck)
print(p1.cardHand)
p1.drawCards(2)
print(p1.deck)
print(p1.cardHand)

p1.adjustPoints(1)
print(p1.points)
p1.adjustPoints(-5)
print(p1.points)

p1.adjustLife(1)
print(p1.life)
p1.adjustLife(-5)
print(p1.life)

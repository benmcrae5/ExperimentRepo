import DeckRandomizer as DeckR
import DiceRandomizer as DiceR
import PlayerClass as PC

#TEST FILE

p1 = PC.Player("adam", [1,2,3,4], 10, 40, 7, ['a','b','c','d'])

p1.addCardToDeck('e')
print(p1.deck)
p1.shuffleDeck()
print(p1.deck)
p1.removeCardFromDeck('c')
print(p1.deck)
p1.organizeDeck()
print(p1.deck)

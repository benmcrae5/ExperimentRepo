import DeckRandomizer as DeckR
import DiceRandomizer as DiceR
import PlayerClass as PC
import CardClass as CC

#TEST FILE

#newAbility = CC.CardAbility("Test Card", 10, 

p1 = PC.Player("Adam", [1,2,3,4], 10, 40, 7, ['a','b','c','d',5,6,7,8], {"Wood": 5, "Stone": 10, "Food": 7} )
p2 = PC.Player("Betty", ['a','b','c','d'], 10, 40, 7, ['e','f','g','h',1,2,3,4], {})

#p1.addCardToDeck('e')
#print(p1.deck)
#p1.shuffleDeck()
#print(p1.deck)
#p1.removeCardFromDeck('c')
#print(p1.deck)
#p1.organizeDeck()
#print(p1.deck)

print(p1.resources)
print(p1.payCost({"Wood": 3}))
print(p1.resources)
print(p1.payCost({"Stone": 10}))
print(p1.resources)
print(p1.payCost({"Stone": 1}))
print(p1.resources)

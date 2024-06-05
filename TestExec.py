import DeckRandomizer as DeckR
import DiceRandomizer as DiceR
import PlayerClass as PC
import CardClass as CC
import CharacterClass as CharCl


#TEST FILE

#newAbility = CC.CardAbility("Test Card", 10, 

p1 = PC.Player("Adam", [1,2,3,4], 10, 40, 7, ['a','b','c','d',5,6,7,8], {"Wood": 5, "Stone": 10, "Food": 7} )
p2 = PC.Player("Betty", ['a','b','c','d'], 10, 40, 7, ['e','f','g','h',1,2,3,4], {})


char1 = CharCl.Character("Elemental", {"food": 10, "magic": 5}, 6, 4, 2, 5)

print(char1)
print(char1.name, char1.cost, char1.move, char1.attack, char1.defense, char1.health)
print(char1.id)


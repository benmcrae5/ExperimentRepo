import DeckRandomizer as DeckR
import DiceRandomizer as DiceR
import PlayerClass as PC
import CardClass as CC
import CharacterClass as CharCl
import BoardClass as BC


#TEST FILE

#newAbility = CC.CardAbility("Test Card", 10, 

p1 = PC.Player("Adam", [1,2,3,4], 10, 40, 7, ['a','b','c','d',5,6,7,8], {"Wood": 5, "Stone": 10, "Food": 7} )
p2 = PC.Player("Betty", ['a','b','c','d'], 10, 40, 7, ['e','f','g','h',1,2,3,4], {})


char1 = CharCl.Character("Elemental",
                         {"food": 10, "magic": 5}, 6, 4, 2, 5)
char2 = CharCl.Character("Goblin",
                         {"food": 2}, 1, 1, 1, 1)

z = char1
print(z._name, z._cost, z._move, z._attack, z._defense, z._health)
z = char2
print(z._name, z._cost, z._move, z._attack, z._defense, z._health)
print(type(char1), type(char2))

char1.attack(char2)

char1.move()
node1 = BC.B_Node("Start")
char1.determineReach(node1)

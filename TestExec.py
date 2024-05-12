import DeckRandomizer as DeckR
import DiceRandomizer as DiceR
import PlayerClass as PC

#TEST FILE

#print(DeckR.StartDeck)
#print(DeckR.runChainShuffle(StartDeck, 4, True))
#print(DeckR.runMultiShuffle(StartDeck, shuffleTopBottom, 4, False))
#print(DeckR.runMultiShuffle(StartDeck, standardShuffle, 4, False))
#print(DeckR.runMultiShuffle(StartDeck, stackShuffle, 4, True))
#print(DeckR.randomShuffler(StartDeck))
#print(DeckR.standardShuffle(StartDeck))
#print(DiceR..rollDice(6))
#print(DiceR.riskDiceBattle())
P1 = PC.Player("adam", priority = 7)
P2 = PC.Player("bob", priority = 4)
P3 = PC.Player("carole", priority = 9)
P4 = PC.Player("dianne", priority = 5)

pa = [P1, P2, P3, P4]
for x in pa:
    print(str(x))
pa.sort()
for x in pa:
    print(str(x))
print(P1)
print(P1>P2)

for x in range(20):
    y=0
    #print(DiceR.dndSkillCheck(15, disadv=True, adv=True, report=True))
    #DiceR.singleDiceBattle(20)

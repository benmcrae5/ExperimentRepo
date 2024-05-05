import random
import math

StartDeck = list(range(52))
#print(StartDeck)

def rollDice(sides, report=False):
    result = int(random.random()*sides)
    if report:
        print(result)
    return result

def stackShuffle(deck, piles=5):
    newDeck=[]
    pileArray = list(range(piles))
    random.shuffle(pileArray)
    for x in pileArray:
        idx = x
        while idx<len(deck):
            newDeck.append(deck[idx])
            idx = idx + piles
    return newDeck    

def shuffleTopBottom(deck, maxCards=5):
    newDeck = []
    idx = 0
    count = 0
    while count <= len(deck):
        randNum = int(random.random()*maxCards)
        currentIdx = count+randNum
        cardHand = deck[count:currentIdx]
        count = currentIdx
        if idx == 0:
            newDeck = newDeck+cardHand
            idx = 1
            continue
        if idx:
            newDeck = cardHand+newDeck
            idx = 0
            continue
    return newDeck

def randomShuffler(deck):
    oldDeck = deck.copy()
    newDeck = []
    for x in range(len(deck)):
        randomNum = int(random.random()*len(oldDeck))
        newDeck.append(oldDeck[randomNum])
        oldDeck.pop(randomNum)
    return newDeck

def standardShuffle(deck):
    newDeck = []
    halfDeck = math.floor(len(deck)/2)
    for x in range(halfDeck):
        newDeck.append(deck[x])
        newDeck.append(deck[x+halfDeck])
    if len(deck)%2 == 1:
        newDeck.append(deck[len(deck)-1])
    return newDeck
        
def runMultiShuffle(deck, shuffleMethod, iterations, reportBool=False):
    #print("Start Multi-Shuffle")
    newDeck = deck.copy()
    for i in range(0, int(iterations)):
        newDeck=shuffleMethod(newDeck)
        if reportBool:
            print("Iteration: " + str(i+1) + " -->")
            print(newDeck)
    return newDeck

def runChainShuffle():
    

    
#print(runMultiShuffle(StartDeck, shuffleTopBottom, 4, False))
#print(runMultiShuffle(StartDeck, standardShuffle, 4, False))
#print(runMultiShuffle(StartDeck, stackShuffle, 4, True))
#print(randomShuffler(StartDeck))
#print(standardShuffle(StartDeck))


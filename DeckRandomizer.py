import random
import math

#Starting Deck is a standard 52 card deck, using simple numbers from 0 to 51
StartDeck = list(range(52))

#Provide the number of sides for a dice, get a random roll.
#TO BE MOVED TO ANOTHER FILE
def rollDice(sides, report=False):
    result = int(random.random()*sides)
    if report:
        print(result)
    return result

#alternate putting cards into piles, then stack the piles in a random order. 
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

#alternate putting cards on top then bottom using variable card amounts
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

#Simple shuffler using python random
def randomShuffler(deck):
    oldDeck = deck.copy()
    newDeck = []
    for x in range(len(deck)):
        randomNum = int(random.random()*len(oldDeck))
        newDeck.append(oldDeck[randomNum])
        oldDeck.pop(randomNum)
    return newDeck

#the "perfect" shuffle - split deck into two piles, alternate cards in a standard shuffle
def standardShuffle(deck):
    newDeck = []
    halfDeck = math.floor(len(deck)/2)
    for x in range(halfDeck):
        newDeck.append(deck[x])
        newDeck.append(deck[x+halfDeck])
    if len(deck)%2 == 1:
        newDeck.append(deck[len(deck)-1])
    return newDeck

#Runs a single shuffle method for a given number of iterations
def runMultiShuffle(deck, shuffleMethod, iterations, reportBool=False):
    #print("Start Multi-Shuffle")
    newDeck = deck.copy()
    for i in range(0, int(iterations)):
        newDeck=shuffleMethod(newDeck)
        if reportBool:
            print("Iteration: " + str(i+1) + " -->")
            print(newDeck)
    return newDeck

#Runs multiple shuffle methods in a sequence at random
def runChainShuffle(deck, iterations, reportBool=False):
    #run multiple shuffle types together
    #functions may only have one parameter (deck), but can have multiple parameters if pre-set
    newDeck = deck.copy()
    ShuffleTypesArray = [stackShuffle, shuffleTopBottom, randomShuffler, standardShuffle]
    x = 0
    while x < iterations:
        randomIdx = int(random.random()*len(ShuffleTypesArray))
        randomFunc = ShuffleTypesArray[randomIdx]
        newDeck = randomFunc(newDeck)
        x+=1
        if reportBool:
            print("Iteration: " + str(x) + " -->")
            print("Random Idx:  " + str(randomIdx) )
            print(newDeck)
    return newDeck


#TEST AREA

#print(StartDeck)
#print(runChainShuffle(StartDeck, 4, True))
#print(runMultiShuffle(StartDeck, shuffleTopBottom, 4, False))
#print(runMultiShuffle(StartDeck, standardShuffle, 4, False))
#print(runMultiShuffle(StartDeck, stackShuffle, 4, True))
#print(randomShuffler(StartDeck))
#print(standardShuffle(StartDeck))



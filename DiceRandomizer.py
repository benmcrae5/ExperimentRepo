import random

#Provide the number of sides for a dice, get a random roll.
def rollDice(sides, report=False):
    result = int(random.random()*sides) + 1
    if report:
        print(result)
    return result

#two players roll an X-sided dice. Compares result and prints answer
def singleDiceBattle(sides=6):
    player1Roll = rollDice(sides)
    player2Roll = rollDice(sides)
    if player1Roll == player2Roll:
        win = 3
    else:
        win = 1 if player1Roll > player2Roll else 2
    print(f'Player 1: {player1Roll}, Player 2: {player2Roll}')
    if win == 3:
        print("It's a tie!")
    else:
        print(f'Player {win} wins!')

#two players roll amounts of dice, compare pairs of highest values to lowest values. 
def riskDiceBattle(p1NumDice = 3, p2NumDice = 2, sides=6):
    p1Rolls = []
    p2Rolls = []
    for x in range(p1NumDice+p2NumDice):
        if x < p1NumDice:
            p1Rolls.append(rollDice(sides))
        else:
            p2Rolls.append(rollDice(sides))
    p1Rolls.sort()
    p2Rolls.sort()
    results = [0,0]
    countDown = (p2NumDice if p1NumDice>p2NumDice else P2NumDice) - 1
    while countDown >= 0:
        if p1Rolls[countDown] > p2Rolls[countDown]:
            results[0] += 1
        else:
            results[1] += 1
        countDown -= 1
    return results

#Basic DnD Rolling, using advantage and disadvantage rules.
def dndSkillCheck(dc, adv=False, disadv=False, report=False):
    rolls = [int(random.random()*20) + 1]
    if adv or disadv:
        rolls.append(int(random.random()*20) + 1)
    if report:
        print(rolls)
    if adv == disadv:
        return True if rolls[0] >= dc else False
    if adv:
        return True if max(rolls) >= dc else False
    if disadv:
        return True if min(rolls) >= dc else False



        

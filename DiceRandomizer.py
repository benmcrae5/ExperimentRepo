import random

#Provide the number of sides for a dice, get a random roll.
def rollDice(sides, report=False):
    result = int(random.random()*sides) + 1
    if report:
        print(result)
    return result

def singleDiceBattle(sides):
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

def riskDiceBattle(p1NumDice = 3, p2NumDice = 2):
    p1Rolls = []
    p2Rolls = []
    for x in range(p1NumDice+p2NumDice):
        if x < p1NumDice:
            p1Rolls.append(rollDice(6))
        else:
            p2Rolls.append(rollDice(6))
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

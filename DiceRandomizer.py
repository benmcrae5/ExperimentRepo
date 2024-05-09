import random

#Provide the number of sides for a dice, get a random roll.
def rollDice(sides, report=False):
    result = int(random.random()*sides)
    if report:
        print(result)
    return result

from random import seed
from random import randint

seed()

randomNumber = randint(1, 6)

guess = int(input('Guess the number from a dice: '))
print(guess == randomNumber)

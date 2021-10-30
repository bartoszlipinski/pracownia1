from random import seed
from random import randint

seed()

roll1 = randint(1, 6)
roll2 = randint(1, 6)
roll3 = randint(1, 6)

print(f'Roll 1: {roll1},\nRoll 2: {roll2},\nRoll 3: {roll3},\nSum of all rolls:  {roll1+roll2+roll3}')

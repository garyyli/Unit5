#Gary Li
#12/4/17
#quiz5.py

from random import randint

randomInt = randint(1,100)
def rand5():
    numbers = []
    for i in range(0,5):
        randomInt = randint(1,100)
        numbers.append(randomInt)
    return numbers

print(rand5())


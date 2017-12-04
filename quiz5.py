#Gary Li
#12/4/17
#quiz5.py

from random import randint

def rand5():
    numbers = []
    for i in range(0,5):
        randomInt = randint(1,100)
        numbers.append(randomInt)
    return numbers

def biggest(help):
    help.sort()
    return help[-1]
    
def lastElement(rip):
    return rip[-1]

print(rand5())
print(biggest([3,-1,5,-2,7,2,1]))
print(lastElement(['cat','dog','rat']))

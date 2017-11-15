#Gary Li
#11/15/17
#middleWord.py

words = input('Enter a list of words: ').split(' ')
words.sort()

middle = len(words)

if middle%2 == 0:
    print(words[(middle/2)-1], words[middle/2])
else:
    print(words[middle//2])
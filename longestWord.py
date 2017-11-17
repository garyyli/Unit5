#Gary Li
#11/17/17
#longestWord.py

words = input('Enter a list of words: ').split(' ')

l = 0
word = ""
for i in words:
    length = len(i)
    if length > l:
        l = length
        word = i
print("The longest word is", word)


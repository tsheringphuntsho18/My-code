#adding ing
word=input('Enter a word: ')
word.capitalize
wordLength=len(word)
if wordLength < 3:
    print(word)
elif wordLength >= 3 and word[-3] != 'i' and word[-2] !='n' and word[-1] !='g':
    ing = word + 'ing'
    print(ing)
elif word[-3] == 'i' and word[-2]=='n' and word[-1]=='g':
    ly = word + 'ly'
    print(ly)
txt=input('Enter any text: ')
vowel=0
for i in txt:
    txt.lower()
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vowel +=1
print(vowel)
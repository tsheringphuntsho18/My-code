
#Loops
list_of_vegs = ['potato','tomato','onion','carrot','cabbage']
for veg in list_of_vegs:
    print(veg)
for veg in list_of_vegs:
    if veg == 'potato':
        print(veg)
string = "Hello World"
for char in string:
    print(char)
for char in string:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        print('Vowel character', char)

#range
for number in range(0,10):
    print(number)
for number in range(1,1):
    if (number / 2) == 0:
        print(number)
for number in range(1,11,2):
    print(number)
for number in range(10,0,-1):
    print(number)
#while loop
counter = 0
while counter < 10:
    print(counter)
    counter += 1
list_of_vegs = ['potato','tomato','onion','carrot','cabbage']
counter = 0
print(len(list_of_vegs))
while counter < len(list_of_vegs):
    print(list_of_vegs[counter])
    counter += 1
#while loop with string
string = "Hello World"
counter = 0
while counter < len(string):
    print(string[counter])
    counter += 1
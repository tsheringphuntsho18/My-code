#even and odd
input = (1,2,3,4,5,6,7,8,9)
even = 0
odd = 0
for i in input:
    if i%2 == 0:
        even +=1
    else:
        odd +=1
print(f'Number of even numbers: {even}\nNumber of odd numbers: {odd}')
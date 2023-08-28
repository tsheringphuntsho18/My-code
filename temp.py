print('Convert temperature using my code')
user_want=input('Enter C for celcius to fahrenheit and Enter F for fahrenheit and E of exit: ')
ans=user_want.capitalize()#it will capitalize uesr input
if ans == 'C':
    print('Celcius to fahrenheit')
    tempC=float(input('Enter celcius value: '))
    result=9*tempC/5+32
    print(f'{tempC} Degree celcius is {result} Degree fahrenheit')

elif ans=='F':
    print('Fahrenheit to celcius')
    tempF=float(input('Enter fahrenheit value: '))
    output=(tempF-32)*5/9
    print(f'{tempF} Degree celcius is {output} Degree fahrenheit')
elif ans!='C'or'F'or'E':
    print('Wrong input')
else:
    print('Thanks for choosing my code')


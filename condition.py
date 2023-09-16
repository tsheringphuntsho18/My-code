#conditionals statement
if True:
    print('The condition is true')
if variable_name == 1:
    print('The value of variable_name is 1')
elif variable_name == 2:
    print('The value of variable_name is 2')
else:
    print('The value of variable_nam is not 1 or 2')
#combining input with condition
user_name = input('What is your name: ')
print('welcome',user_name)
user_age = int(input('What is your age: '))
if user_age < 18:
    print('You are a minor')
elif user_age >= 18 and user_age < 60:
    print('You are adult')
else:
    print('You are senoir citizen')
#Multiple condition(and)
if True and True:
    print('True True')
if True and False:
    print('True False')
if False and True:
    print('False True')
if False and False:
    print('False False')
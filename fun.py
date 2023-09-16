#defining a function
def print_hello():
    print('Hello')
print_hello()

def print_hello_world():
    print_hello()
    print('world')
print_hello_world()

def print_name(name):
    print('Hello', name)
print_name('john')

def calculate_addition(x,y):
    print('Addition results:', x + y)
calculate_addition(10,20)

def calculate_addition(x,y):
    return x + y
result = calculate_addition(10,20)
print('Addition results: ',result)
 # multiple value
def calculate_addition_subtraction(x,y):
    return x + y, x - y
addition_result,subtraction_result = calculate_addition_subtraction(10,20)
print('Addition result:',addition_result)
print('subtraction result:',subtraction_result)
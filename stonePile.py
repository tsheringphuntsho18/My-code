#stone pile
n = int(input("Enter the number of stones in the first pile: "))
def numberStone(n):
    return [n+2*i for i in range(n)]
print(numberStone(n))    




def SumOfSquares(a,b):
    return a*a+b*b
print(SumOfSquares(3,4))
def GM(s):
    print("Good Morning",s)
GM("Adithi")
import math

def CheckPrime(a):
    if a < 2:
        return False 
    for i in range(2, int(math.sqrt(a)) + 1):  
        if a % i == 0:
            return False
    return True
print(CheckPrime(23))

def print(x,y,end="\n",sep=" "):
    pass
print(3,4,sep=" ",end=" ")


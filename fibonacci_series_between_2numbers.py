import math
a=int(input("Enter lower bound: "))
b=int(input("Enter upper bound: "))
def issquare(x):
    if(x >= 0):
        sr = int(math.sqrt(x))
        return ((sr*sr) == x)
    return false
for i in range(a,b+1):
    if issquare(5*i*i + 4) or issquare(5*i*i - 4):
        print(i)
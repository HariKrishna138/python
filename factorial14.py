def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input("enter a number "))
if(n<0):
    print("NOT POSSIBLE FOR NEGATIVE NUMBERS")
else:
    print("Factorial is ",n,"is ",fact(n))
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
n=int(input("Enter a number"))
if n<=0:
    print("NOT POSSIBLE")
else:
    print("Terms are")
    for i in range(n):
        print(fib(i))
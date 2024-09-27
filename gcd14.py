def gcd(m,n):
    rem=m%n
    if rem==0:
        return n
    else:
        m=n
        n=rem  
        return gcd(m,n)
m=int(input("Enter dividend"))
n=int(input("Enter divisor"))
print(gcd(m,n))  
s={10,20,33,30,40,50}
s1={11,22,33,44,55}
s3={}
print(s|s1)#union
print(s&s1)#intersection
print(s1-s)#difference
print(s^s1)#symmetric difference
print(10 in s and 22 in s1)
print(s.add(60))
print(s.discard(10))
print(s.remove(33))
print(s1.pop())
s3=s1.copy()
print(s3)
print(s.difference(s1))
print(s3.symmetric_difference(s))
for i in s:
    print(i)
s.add(35)
print(s)
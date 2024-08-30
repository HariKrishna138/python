t=(10,20,20,30,40,55)
t1=(11,22,33,44,13)
t2=()
t3=()
print(t+t1)
print(t*4," ",t1*4)
print(t[1]*t[2])
print(t[3]-t[0])
print(10 in t)
print(12 in t1)
for i in t:
    print(i)
for j in t1:
    print(j)
for i in t:
    for j in t1:
        print("(",i,",",j,")")
#for i in range(len(t)):
# print("(",t[i],",",t1[i],")")
print(t[1:3:1])
print(t[3::1])
print(t.index(20),",",len(t1)+len(t),",",t.count(20),",",)
t2=(list(zip(t1,t)))
print(t2)
t3=set(t2)
print(t3) 

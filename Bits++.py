t=int(input())
c=0
for i in range(t):
    s=input()
    d=s.count("+")
    if d>0:
        c+=1
    else:
        c-=1
print(c)
    
    
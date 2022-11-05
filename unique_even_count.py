t=int(input())
a=list(map(int,input().split()))
d=0
c=[]
for i in a:
    if i not in c:
        c.append(i)
for j in c:
    if j%2==0:
        d+=1
print(d)
        
    
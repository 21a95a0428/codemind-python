n=int(input())
a=list(map(int,input().split()))
c=[]
for i in a:
    if i not in c:
        c.append(i)
for j in c:
    d=a.count(j)
    print(j,d,end=" ")
        

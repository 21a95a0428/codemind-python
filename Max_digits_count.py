def num_d(k):
    c=[]
    while k:
        r=k%10
        c.append(r)
        k//=10
    return len(c)
t=int(input())
a=list(map(int,input().split()))
d=[]
for i in a:
    g=num_d(i)
    d.append(g)
f=max(d)
h=d.count(f)
print(h)
    
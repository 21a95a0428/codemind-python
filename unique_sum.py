n=int(input())
a=list(map(int,input().split()))
a=list(set(a))
c=0
for i in a:
    c+=i
print(c)
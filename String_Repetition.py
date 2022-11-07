s=input()
d=s.count("a")
n=int(input())
l=len(s)
x=''
g=n%l
if g==0:
    c=n//l
    print(c*d)
else:
    for i in range(g):
        x+=s[i]
    e=x.count("a")
    h=n//l
    print((h*d)+e)
        
        
    
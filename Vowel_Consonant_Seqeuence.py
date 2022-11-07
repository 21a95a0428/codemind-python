s=input()
d="aeiou"
c=''
for i in s:
    if i in d:
        c+="V"
    else:
        c+="C"
z='h'
for i in c:
    if z[-1]!=i:
        z+=i
print(z[1:])

## WAP to print the most repeated word in a given string??

s="tus kum kumar tus panda tus kum"
s1=s.split()
d={}
for i in s1:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
mx=max(d.values())
for j in d:
    if d[j]==mx:
        print(j)


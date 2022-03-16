import json
n={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}

a=[]
b=[]
#sort=json.loads(n)
for i in n:
    a.append(i)
    b.append(n[i])
for i in range(len(b)):
    for j in range(len(b)):
        if b[i]<b[j]:
           temp=b[i] 
           b[i]=b[j]
           b[j]=temp
           temp2=a[i]
           a[i]=a[j]
           a[j]=temp2
d={} 
for c in range(len(b)):
    d[a[c]]=b[c]

print(d)              

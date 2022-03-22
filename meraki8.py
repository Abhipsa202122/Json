import json
d1=[["neelam","programer","24","2400"],["komal","trainer","24","20000"],
["anuradha","HR","25","40000"],["Abhishek","manager","29","63000"]]
a=["name","designation","age","salary"]
b=["emp1","emp2","emp3","emp4"]
e={}
for i in range(len(b)):
     dict={ }
     for j in range(len(d1)):
          dict[a[j]]=d1[i][j]      
     # e[b[i]]=dict
     e.update({b[i]:dict})
print(e)     


with open("abhi txt.json","w") as file:
     json.dump(e,file,indent=4) 

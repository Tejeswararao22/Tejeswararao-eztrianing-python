x=input("enter the name:").lower()
y=input("enter the name:").lower()
x=x.replace(" ","")
y=y.replace(" ","")
print(x)
print(y)
for i in x:
    for j in y:
        if i==j:
            x=x.replace(i,"",1)
            y=y.replace(j,"",1)
            break
count=len(x+y)
print(count)
if count>0:
        l1=["friends","lovers","affectionates","marriage","enemys","siblings"]
        while len(l1)>1:
            c=count%len(l1)
            s_index=c-1
            if s_index>=0:
                left=l1[:s_index]
                right=l1[s_index+1:]
                l1=right+left
            else:
                l1=l1[:len(l1)-1]
        print("relationship:",l1[0])
else:
     print("enter different names:")


   

'''s=input("enter")
x=s[::-1]
print(x)
if s==x:
    print("palindrome")
else:
    print("not palindrome")'''

'''s=input("enter")
count=0
for i in s:
    if i==' ':
        count+=1
print(count)'''

l=['a','e','i','o','u','A','E','I','O','U']
a=input("enter a string")
count=0
for i in a:
    if i in l:
        count=count+1
print(count)
        

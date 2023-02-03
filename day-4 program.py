#math module
import math
print("CEIL 12.5:", math.ceil(12.5))
print("FLOOR 12.5:",math.floor(12.5))
print("SQRT 345:" , math.sqrt(345))
print("FACTORAL 3:", math.factorial(3))
print("POWER 2,3",math.pow(2,3))
a,b=divmod(10,3)
print(a,b)



CEIL 12.5: 13
FLOOR 12.5: 12
SQRT 345: 18.57417562100671
FACTORAL 3: 6
POWER 2,3 8.0
3 1


s=input("enter")
x=s[::-1]
print(x)
if s==x:
    print("palindrome")
else:
    print("not palindrome")

s=input("enter")
count=0
for i in s:
    if i==' ':
        count+=1
print(count)

l=['a','e','i','o','u','A','E','I','O','U']
a=input("enter a string")
count=0
for i in a:
    if i in l:
        count=count+1
print(count)
        

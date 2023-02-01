l=[1,4,7.4,'sam']
l
[1, 4, 7.4, 'sam']
type(l)
<class 'list'>
l[3]
'sam'
l[2:4]
[7.4, 'sam']
l[0:]
[1, 4, 7.4, 'sam']
l[:-1]
[1, 4, 7.4]
l[::-1]
['sam', 7.4, 4, 1]
l=[1,4,1,1,6,4,1,2]
len(l)
8
l.count(1)
4
l.count(4)
2
l.append(400)
l
[1, 4, 1, 1, 6, 4, 1, 2, 400]
l.extend([100,200,300])
l
[1, 4, 1, 1, 6, 4, 1, 2, 400, 100, 200, 300]
l.remove(1)
l
[4, 1, 1, 6, 4, 1, 2, 400, 100, 200, 300]
l.pop(-2)
200
l
[4, 1, 1, 6, 4, 1, 2, 400, 100, 300]
l.sort()
l
[1, 1, 1, 2, 4, 4, 6, 100, 300, 400]
l.reverse()
l
[400, 300, 100, 6, 4, 4, 2, 1, 1, 1]

l=[1,3,2,4,5,6,7,8,9,4]
for i in l:
    print(i)
    
==== RESTART: C:/Users/PC-68/AppData/Local/Programs/Python/Python311/day3.py ===
1
3
2
4
5
6
7
8
9
4

l=[1.1,2.2,3.3,4.4,5.5]
x=sum(l)
print(x)
avg=x/10
print(avg)
==== RESTART: C:/Users/PC-68/AppData/Local/Programs/Python/Python311/sum.py ====
16.5
1.65

l=[1,2,3,4,5,6]
for i in l:
    if i%2==0:
        print(i)
==== RESTART: C:/Users/PC-68/AppData/Local/Programs/Python/Python311/even.py ===
2
4
6

size=int(input("size:"))
l=[]
for i in range(size):
    ele=int(input("element:"))
    l.append(ele)
print(l)
for j in l:
    if j%2==0:
        print(j)
= RESTART: C:/Users/PC-68/AppData/Local/Programs/Python/Python311/user input.py
size:6
element:1
element:2
element:3
element:3
element:5
element:6
[1, 2, 3, 3, 5, 6]
2
6
n=list(map(int,input("enter").split()))
x=1
y=0
for i in n:
    x=x*i
    y=y+i
if x<=750:
    print("product",x)
else:
    print("sum",y)

n=[elements for elements in "Great Afternoon"]
print(n)
= RESTART: C:/Users/PC-68/AppData/Local/Programs/Python/Python311/list comprehension.py
['G', 'r', 'e', 'a', 't', ' ', 'A', 'f', 't', 'e', 'r', 'n', 'o', 'o', 'n']

l=["hyd","vizag","chennai","vijayawada"]
x=[]
for i in l:
    if "v" in i:
        x.append(i)
print(x)

= RESTART: C:/Users/PC-68/AppData/Local/Programs/Python/Python311/python comprehesion.py
['vizag', 'vijayawada']

l=[2**i for i in range(2,8)]
print(l)
==== RESTART: C:/Users/PC-68/AppData/Local/Programs/Python/Python311/list.py ===
[4, 8, 16, 32, 64, 128]

s={1,2,3,4,5}
s.add(6)
s
{1, 2, 3, 4, 5, 6}
s.update([20,9])
s
{1, 2, 3, 4, 5, 6, 20, 9}
s.discard(5)
s
{1, 2, 3, 4, 6, 20, 9}
s.remove(20)
s
{1, 2, 3, 4, 6, 9}
s1={1,2,3}
s2={4,5,6,1,2}
s1|s2
{1, 2, 3, 4, 5, 6}
s1-s2
{3}
s2-s1
{4, 5, 6}
s2.issuperset(s1)
False
s1={1,2,3,4,2,1,3,4,5}
s2={1,2,3,4,6,7,8,6}
s1^s2
{5, 6, 7, 8}
##tuples
t=(4,3,4,9,6)
type(t)
<class 'tuple'>
t.count(4)
2
t.index(4)
0
#dict
d={1:"one",2:"two"}
d
{1: 'one', 2: 'two'}
type(d)
<class 'dict'>
d.items()
dict_items([(1, 'one'), (2, 'two')])
d.values()
dict_values(['techno', 'meizu'])
d.get("x")
'techno'
d.get("y")
'meizu'
l=["hii","hello"]
dict.fromkeys(l)
{'hii': None, 'hello': None}
dic.fromkeys(l,100)
dict.fromkeys(l,100)
{'hii': 100, 'hello': 100}
d={"x":"techno","y":"meizu"}
d.items()
dict_items([('x', 'techno'), ('y', 'meizu')])
d.update({"z":100})
d
{'x': 'techno', 'y': 'meizu', 'z': 100}
d.pop("z")
100
d={1:'a',2:'c'}
d.setdefault(3,d)
{1: 'a', 2: 'c', 3: {...}}
{1: 'a', 2: 'c', 3: {...}}
    

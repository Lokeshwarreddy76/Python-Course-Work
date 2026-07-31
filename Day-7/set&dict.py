Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s = {}
type(s)
<class 'dict'>
s = set()
s = {1,2,3,4,12,324,9876,12431324}
s
{1, 2, 3, 4, 324, 12, 9876, 12431324}
s = set()
a
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a
NameError: name 'a' is not defined
s
set()
s.add(1)
s.add(12.3)
s.add(2+4j)
s.add()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s.add()
TypeError: set.add() takes exactly one argument (0 given)
s
{1, 12.3, (2+4j)}
s.add(True)
s
{1, 12.3, (2+4j)}
s = {1,1,1,1,1,1}
s
{1}
l = {10,20,30}
m = {1,2,3,4}
l+m
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    l+m
TypeError: unsupported operand type(s) for +: 'set' and 'set'
l*2
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    l*2
TypeError: unsupported operand type(s) for *: 'set' and 'int'
l[0]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    l[0]
TypeError: 'set' object is not subscriptable
l[1:2]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    l[1:2]
TypeError: 'set' object is not subscriptable
a = {1,2,3,4,5}
b = {3,5,7,9}
a
{1, 2, 3, 4, 5}
b
{9, 3, 5, 7}
a|b
{1, 2, 3, 4, 5, 7, 9}
a&b
{3, 5}
a-b
{1, 2, 4}
a^b
{1, 2, 4, 7, 9}
#{1}{2}{3}{4}{5}{1,2},{2,3},{3,4},{1,4},{1,2,3,4}
{1}<=a
True
{1,2,3,4}<=a
True
a
{1, 2, 3, 4, 5}
{1,2,3,4,5}<=a
True
a
{1, 2, 3, 4, 5}
b
{9, 3, 5, 7}
a.isdisjoint(b)
False
a. disjoint({9,10})
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a. disjoint({9,10})
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
a.isdisjoint({9,10})
True
a.union(b)
{1, 2, 3, 4, 5, 7, 9}
a.intersection(b)
{3, 5}
a.issubset(b)
False
a.issuperset(b)
False
a
{1, 2, 3, 4, 5}
5 in a
True
9 not in a
True
7 in a
False
a
{1, 2, 3, 4, 5}
max(a)
5
min(a)
1
sorted(a)
[1, 2, 3, 4, 5]
sum(a)
15
a
{1, 2, 3, 4, 5}
b=a
b
{1, 2, 3, 4, 5}
a.add(12)
a
{1, 2, 3, 4, 5, 12}
b
{1, 2, 3, 4, 5, 12}
c.copy()
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    c.copy()
NameError: name 'c' is not defined
c = a.copy()
c.add(13)
c
{1, 2, 3, 4, 5, 12, 13}
a
{1, 2, 3, 4, 5, 12}
b
{1, 2, 3, 4, 5, 12}
a = {1,2,3,4,5,6,7,8}
a
{1, 2, 3, 4, 5, 6, 7, 8}
a.add(9)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9}
a.update({10,11})
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
a.pop()
1
a.pop()
2
a
{3, 4, 5, 6, 7, 8, 9, 10, 11}
a.remove(11)
a
{3, 4, 5, 6, 7, 8, 9, 10}
a.discard(11)
a.discard(13)
a
{3, 4, 5, 6, 7, 8, 9, 10}
a.discard(10)
a.discard(7)
a
{3, 4, 5, 6, 8, 9}
a.update({'str',0,4,12+j,-1,-2})
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    a.update({'str',0,4,12+j,-1,-2})
NameError: name 'j' is not defined
a.update({'str',0,4,12.3,-1,-2})
a
{0, 3, 4, 5, 6, 8, 9, 12.3, 'str', -1, -2}
a.clear()
a
set()
a = ({1,2,13,15,53,20})
a
{1, 2, 20, 53, 13, 15}
a = frozenset({1,2,13,15,53,20})
a
frozenset({1, 2, 20, 53, 13, 15})
a.add(12)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    a.add(12)
AttributeError: 'frozenset' object has no attribute 'add'
#DICTIONARIES
d={}
d=dict()
d
{}
type(d)
<class 'dict'>
d = {'k1':'v1','k2':'v2','k3':'v3',}
d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
id(d)
2915845262272
d['k4'] = 'v4'
d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
d['k5'] = 'v4'
d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4', 'k5': 'v4'}
d[]
SyntaxError: invalid syntax
d={}
d[1]
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    d[1]
KeyError: 1
d[1] = 'int'
d
{1: 'int'}
d[12.3] = 'flt'
d
{1: 'int', 12.3: 'flt'}
d[12+j] = 'complex'
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    d[12+j] = 'complex'
NameError: name 'j' is not defined
d[2+4j] = 'com'
d
{1: 'int', 12.3: 'flt', (2+4j): 'com'}
d['str'] = 'string'
d
{1: 'int', 12.3: 'flt', (2+4j): 'com', 'str': 'string'}
d[(1,2,3,4)] = 'tuple'
d
{1: 'int', 12.3: 'flt', (2+4j): 'com', 'str': 'string', (1, 2, 3, 4): 'tuple'}
d[False] = 'False'
d
{1: 'int', 12.3: 'flt', (2+4j): 'com', 'str': 'string', (1, 2, 3, 4): 'tuple', False: 'False'}
>>> d(frozenset{1,2,3}) = 'fset'
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> d = {}
>>> d[1]=1
>>> d[2]=12.3
>>> d[3]=12+4j
>>> d[4]='str'
>>> d[5]=[1,2,3,4]
>>> d[6]=(1,2,3)
>>> d[7]={1,2,3}
>>> d[8]={1:1}
>>> d
{1: 1, 2: 12.3, 3: (12+4j), 4: 'str', 5: [1, 2, 3, 4], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}}
>>> d[9]=True
>>> d
{1: 1, 2: 12.3, 3: (12+4j), 4: 'str', 5: [1, 2, 3, 4], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> 9 in d
True
>>> 10 in d
False
>>> 'str' in d
False
>>> d[5]
[1, 2, 3, 4]
>>> d[8]
{1: 1}
>>> d.get(10)
>>> d.get(1)
1
>>> d.get(10,"key is not present")
'key is not present'
>>> d.get(6,"key is not present")
(1, 2, 3)
>>> d
{1: 1, 2: 12.3, 3: (12+4j), 4: 'str', 5: [1, 2, 3, 4], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[3]=4
>>> d
{1: 1, 2: 12.3, 3: 4, 4: 'str', 5: [1, 2, 3, 4], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[5]=10
>>> d
{1: 1, 2: 12.3, 3: 4, 4: 'str', 5: 10, 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[6]=12
>>> d
{1: 1, 2: 12.3, 3: 4, 4: 'str', 5: 10, 6: 12, 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[7]=20
>>> d
{1: 1, 2: 12.3, 3: 4, 4: 'str', 5: 10, 6: 12, 7: 20, 8: {1: 1}, 9: True}

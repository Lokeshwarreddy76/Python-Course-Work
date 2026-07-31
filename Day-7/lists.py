Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> l = [1,2,3,4,5]
>>> l
[1, 2, 3, 4, 5]
>>> id(l)
2101345738752
>>> l.append(12)
>>> l
[1, 2, 3, 4, 5, 12]
>>> l.append(14)
>>> l
[1, 2, 3, 4, 5, 12, 14]
>>> l.insert[1,13]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    l.insert[1,13]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> l.insert(1,13)
>>> l
[1, 13, 2, 3, 4, 5, 12, 14]
>>> '''extend used to adding multiple elements'''
'extend used to adding multiple elements'
>>> l.extend([15,16,17])
>>> l
[1, 13, 2, 3, 4, 5, 12, 14, 15, 16, 17]
>>> l(3)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    l(3)
TypeError: 'list' object is not callable
>>> l[3]
3
>>> l
[1, 13, 2, 3, 4, 5, 12, 14, 15, 16, 17]
>>> l[12]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    l[12]
IndexError: list index out of range
>>> l[3]=18
>>> l
[1, 13, 2, 18, 4, 5, 12, 14, 15, 16, 17]
>>> id(1)
140729470915496
>>> l.pop()
17
>>> l
[1, 13, 2, 18, 4, 5, 12, 14, 15, 16]
>>> l.remove(2)
>>> l
[1, 13, 18, 4, 5, 12, 14, 15, 16]
del l[2]
l
[1, 13, 4, 5, 12, 14, 15, 16]
l.clear[]
SyntaxError: invalid syntax
l.clear()
l
[]
id(1)
140729470915496
l = [1, 13, 4, 5, 12, 14, 15, 16]
l
[1, 13, 4, 5, 12, 14, 15, 16]
max(l)
16
min(l)
1
sorted(l)
[1, 4, 5, 12, 13, 14, 15, 16]
l
[1, 13, 4, 5, 12, 14, 15, 16]
l.reverse()
l
[16, 15, 14, 12, 5, 4, 13, 1]
l.sort()
l
[1, 4, 5, 12, 13, 14, 15, 16]
l = [1,2,3]
m = [1,2,3]
l
[1, 2, 3]
n = l
l.sort(reverse=True)
l
[3, 2, 1]
sum(1)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    sum(1)
TypeError: 'int' object is not iterable
l = [1, 13, 4, 5, 12, 14, 15, 16]
l
[1, 13, 4, 5, 12, 14, 15, 16]
l.sort(reverse=True)
l
[16, 15, 14, 13, 12, 5, 4, 1]
sum(l)
80
l = [1,2,3]
m = [1,2,3]
l
[1, 2, 3]
n = l
n.append()
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    n.append()
TypeError: list.append() takes exactly one argument (0 given)
n.append()
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    n.append()
TypeError: list.append() takes exactly one argument (0 given)
n.append(4)
l
[1, 2, 3, 4]
l
[1, 2, 3, 4]
m = l.copy()
m
[1, 2, 3, 4]
m.append(10)
m
[1, 2, 3, 4, 10]
l
[1, 2, 3, 4]
all([0,'',[],set(),{},False])
False
all([1,'',[],set(),{},False])
False
any([1,'',[],set(),{},False])
True
l
[1, 2, 3, 4]
l.index(3)
2
l.index(5)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    l.index(5)
ValueError: 5 is not in list
l
[1, 2, 3, 4]
l.count(3)
1
l.count(5)
0
'nested list'
'nested list'
l = [[1,2,3,4][5,6,7,8]]
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    l = [[1,2,3,4][5,6,7,8]]
TypeError: list indices must be integers or slices, not tuple
l = [[1,2,3,4],[5,6,7,8]]
l[0]
[1, 2, 3, 4]
l[1]
[5, 6, 7, 8]
l[0][3]
4
l[1][3]
8
l[-1][-1]
8

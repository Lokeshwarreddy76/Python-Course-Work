Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
int(a)
10
float(a)
10.0
list(a)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
complex(a)
(10+0j)
bool(a)
True
dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
a=10.23
float(a)
10.23
int(a)
10
list(a)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    list(a)
TypeError: 'float' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    tuple(a)
TypeError: 'float' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    set(a)
TypeError: 'float' object is not iterable
bool(a)
True
dict(a)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    dict(a)
TypeError: 'float' object is not iterable
str(a)
'10.23'
complex(a)
(10.23+0j)
a=3+4j
complex(a)
(3+4j)
int(a)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(a)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'complex'
complex(a)
(3+4j)
str(a)
'(3+4j)'
list(a)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    list(a)
TypeError: 'complex' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    tuple(a)
TypeError: 'complex' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    dict(a)
TypeError: 'complex' object is not iterable
bool(a)
True
set(a)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    set(a)
TypeError: 'complex' object is not iterable
a={2,3,4,5,6}
set(a)
{2, 3, 4, 5, 6}
int(a)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(a)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'set'
complex(a)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    complex(a)
TypeError: complex() first argument must be a string or a number, not 'set'
tuple(a)
(2, 3, 4, 5, 6)
dict(a)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    dict(a)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
booi(a)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    booi(a)
NameError: name 'booi' is not defined. Did you mean: 'bool'?
bool(a)
True
list(a)
[2, 3, 4, 5, 6]
str(a)
'{2, 3, 4, 5, 6}'
>>> list(a)
[2, 3, 4, 5, 6]
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    dict(a)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> a=(23,45,67,89)
>>> tuple(a)
(23, 45, 67, 89)
>>> int(a)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
>>> float(a)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'tuple'
>>> complex(a)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    complex(a)
TypeError: complex() first argument must be a string or a number, not 'tuple'
>>> str(a)
'(23, 45, 67, 89)'
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    dict(a)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> list(a)
[23, 45, 67, 89]
>>> set(a)
{89, 67, 45, 23}
>>> bool(a)
True

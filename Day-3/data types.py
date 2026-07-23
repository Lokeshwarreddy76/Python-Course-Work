Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> count =10
>>> count =7
>>> count
7
>>> type(count)
<class 'int'>
>>> price=99.99
>>> price
99.99
>>> type(price)
<class 'float'>
>>> c=3=8j
SyntaxError: cannot assign to literal
>>> c=3+8j
>>> c
(3+8j)
>>> type(c)
<class 'complex'>
>>> s=loki
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s=loki
NameError: name 'loki' is not defined
>>> s='loki'
>>> s
'loki'
>>> type(s)
<class 'str'>
>>> marks=(70,80,90)
>>> type(marks)
<class 'tuple'>
>>> n={1,2,3,4,}
>>> type(n)
<class 'set'>
>>> n[12,34,56,78]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    n[12,34,56,78]
TypeError: 'set' object is not subscriptable
>>> n=[12,34,56,78]
>>> type(n)
<class 'list'>

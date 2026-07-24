Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=20
b=10
a+b
30
a-b
10
a*b
200
a|b
30
a/b
2.0
9/2
4.5
a//b
2
9//2
4
9%2
1
2**3
8
4**2
16
print('comparison operators')
comparison operators
a=20
b=20
a>b
False
a<b
False
a>=b
True
a<=b
True
a==b
True
a=10
a=20
a=b
a!=b
False
c=10
c=c+10
c
20
print('comparison operators')
comparison operators
a=10
b=20
a!=b
True
c=10
c=c+10
c
20
c=c+20
c
40
c=C+30
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    c=C+30
NameError: name 'C' is not defined. Did you mean: 'c'?
c=c+30
c
70
c+=10
c
80
c**=2
c
6400
c%=3
c
1
KeyboardInterrupt
c/=10
c
0.1
c/=2
c
0.05
print('relational operators')
relational operators
a=10
a > 5 and a < 15
True
a > 5 and a > 10
False
n % 2 and n % 3==0
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    n % 2 and n % 3==0
NameError: name 'n' is not defined
n%2==0 and n%3==0
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    n%2==0 and n%3==0
NameError: name 'n' is not defined
n=10
n%2==0
True
n%3==0
False
n%2==0 and n%3==0
False
n%8==0  or n%3==0
False
n%2==0 or n%3==0
True
#str list tuple set dict
s='codegnan'
'e' in s
True
'n' in s
True
'f' not in s
True
'o' not in s
False
l=[1,2,3,4]
4 in l
True
3 in l
True
5 not in l
True
1  not in l
False
t=(1,2,3,4,5)
'1'  in t
False
t=[1,2,3,4,5]
'1' in t
False
t=(1,2,3,4,5)
1 in t
True
5 in t
True
6 not in t
True
7 in t
False
s={1,2,3,4,5,6}
6in s
True
4 in s
True
7 in s
False
7 not in s
True
d={'name':'lokesh','batch':63,'course':'pfs')
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
d={'name':'lokesh','batch':63,'course':'pfs}
   
SyntaxError: unterminated string literal (detected at line 1)
d={'name':'lokesh','batch':63,'course':'pfs'}
   
'name' in d
   
True
'lokesh' in d
   
False
'batch' in d
   
True
63 in d
   
False
'python' in d
   
False
age not in d
   
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    age not in d
NameError: name 'age' is not defined
'age' not in d
   
True
'''identity operators'''
   
'identity operators'
l=[1,2,3,4,]
   
l=[1,23,4]
   
m=[1,2,3,4]
   
id(l)
   
1922150178560
id(m)
   
1922149835264
l is m
   
False
n = 1
   
idn)
SyntaxError: unmatched ')'
id(n)
140722659824552
l is n
False
l is not m
True
l is not n
True
a+=10
a
20
id(a)
140722659825160
s={1,2,3,4}
id(s)
1922149797888
s.add(5)
s
{1, 2, 3, 4, 5}
id(s)
1922149797888
print('bitwise operators')
bitwise operators
9&10
8
9|10
11
9^10
3
8<<2
32
8>>2
2
8<<2
32
~8
-9
~12
-13
~45
-46
a=10
b=10.3
c='codegnan'
print(a,b,c)
10 10.3 codegnan
print('a value is a',a )
a value is a 10
print('a value is' a',a,'| b value is', b','| c value is ',c)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print('a value is' a',a,'| b value is', b','| c value is ',c)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print('a value is' a',a,'| b value is', b','| c value is ',c)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("a value is' a',a,'| b value is', b','| c value is ',c)
      
SyntaxError: unterminated string literal (detected at line 1)
print('a value is', a',a,'| b value is', b','| c value is ',c)
...       
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("a value is",a,'| b value is', b','| c value is ',c)
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print("a value is",a,'| b value is', b','| c value is',c)
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print("a value is",a,"| b value is",b,'| c value is ',c)
...       
a value is 10 | b value is 10.3 | c value is  codegnan
>>> print(a,b,c)
...       
10 10.3 codegnan
>>> print(a,b,c,sep='')
...       
1010.3codegnan
>>> print(a,b,c,sep='t',end='@')
...       
10t10.3tcodegnan@
>>> print(a,b,c,sep='t',end='\n\n')
...       
10t10.3tcodegnan

>>> print(f'a=(a) b=(b) c=(c)')
...       
a=(a) b=(b) c=(c)
>>> print(f" a value is{a} b value is{b} c value is{c}")
...       
 a value is10 b value is10.3 c value iscodegnan
>>> print('a=%d b=%f c=%s'%(a,b,c))
...       
a=10 b=10.300000 c=codegnan
>>> print('a=%d b=%f c=%s'%(c,a,b))
...       
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    print('a=%d b=%f c=%s'%(c,a,b))
TypeError: %d format: a real number is required, not str

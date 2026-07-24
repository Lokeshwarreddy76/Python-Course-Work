Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#int float str list tuple dict
x=input()
lokesh
x
'lokesh'
name=input()
lokesh
name
'lokesh'
name = input("Enter your name:")
Enter your name:lokesh
name
'lokesh'
age = input("Enter your age:")
Enter your age:21
age
'21'
age = int(input("Enter your age:")
age = int(input("Enter your age:"))
          
SyntaxError: '(' was never closed
age = int(input("Enter your age:"))
          
Enter your age:21
age
          
21
names = input("Enter your name:")
          
Enter your name:lokesh
name
          
'lokesh'
names = input("Enter your names:")
          
Enter your names:lokesh avinash bharath
names
          
'lokesh avinash bharath'
names.split()
          
['lokesh', 'avinash', 'bharath']
names = input("Enter your names:").split()
          
Enter your names:lokesh bharath avinash
names
          
['lokesh', 'bharath', 'avinash']
names = input("Enter your names:").split()
          
Enter your names:1 2 3 4 5 6 
names
          
['1', '2', '3', '4', '5', '6']
map(int,names)
          
<map object at 0x000001AB9BDE44F0>
list(map(int,names))
          
[1, 2, 3, 4, 5, 6]
values =list(map(int,input().split()))
          
values =list(map(int,input().split()))
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    values =list(map(int,input().split()))
ValueError: invalid literal for int() with base 10: 'values'
values =list(map(int,input().split()))
          
1 3 4 5 6 6 7 
values
          
[1, 3, 4, 5, 6, 6, 7]
values = list(map(int,input().split()))
          
1 23 4 5 5 66 55
values
          
[1, 23, 4, 5, 5, 66, 55]
names = tuple(input("Enter the names:").split()
 lokesh ganesh avinash
              
SyntaxError: '(' was never closed
names = tuple(input("Enter your names:").split()
lokesh avinash
              
SyntaxError: invalid syntax. Perhaps you forgot a comma?
a,b = [1,2]
              
a
              
1
a,b = [1,2]
              
a
              
1
a,b=[1,2]
              
a
              
1
email,password = input("Enter the email and password:").split()
              
Enter the email and password:loki@gmail.com 4567
gmail
              
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    gmail
NameError: name 'gmail' is not defined. Did you mean: 'email'?
email
              
'loki@gmail.com'
marks
              
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    marks
NameError: name 'marks' is not defined. Did you mean: 'vars'?
password
              
'4567'
a,b,c = list(map(int,input().split()))
              
a,b,c = list(map(int,input().split()))
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    a,b,c = list(map(int,input().split()))
ValueError: invalid literal for int() with base 10: 'a,b,c'
a,b,c = list(map(int,input().split()))
              
1 2 3
a
              
1
b
              
2
c
              
3
name,marks = input().split()
              
lokesh 76
>>> name
...               
'lokesh'
>>> marks
...               
'76'
>>> int(marks)
...               
76
>>> e = eval(input())
...               
1
>>> e
...               
1
>>> e = eval(input())
...               
1234.76
>>> e
...               
1234.76
>>> e = eval(input())
...               
"lokesh"
>>> e
...               
'lokesh'
>>> KeyboardInterrupt
>>> e = eval(input())
...               
e = eval(input())
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    e = eval(input())
  File "<string>", line 1
    e = eval(input())
      ^
SyntaxError: invalid syntax
>>> e = eval(input())
... [1,2,3,4,5]
...               
SyntaxError: multiple statements found while compiling a single statement
>>> e = eval(input())
...               
true
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    e = eval(input())
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'true' is not defined. Did you mean: 'True'?

Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
c = "python programming"
len(c)
18
ord('p')
112
ord('A')
65
ord('a')
97
ord('0')
48
ord('56')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    ord('56')
TypeError: ord() expected a character, but string of length 2 found
ord('1')
49
chr(48)
'0'
sorted(c)
[' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
sorted(reverse = true)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    sorted(reverse = true)
NameError: name 'true' is not defined. Did you mean: 'True'?
min(c)
' '
max(c)
'y'
c = 'String is immutable'
c
'String is immutable'
c.upper()
'STRING IS IMMUTABLE'
c.lower()
'string is immutable'
c.capitalize()
'String is immutable'
c.title()
'String Is Immutable'
c.swapcase()
'sTRING IS IMMUTABLE'
c.casefold()
'string is immutable'
# STRING ALINEMENTS METHODS
c.centre(60,'0')
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    c.centre(60,'0')
AttributeError: 'str' object has no attribute 'centre'. Did you mean: 'center'?
c.center(60,'0')
'00000000000000000000String is immutable000000000000000000000'
c.center(60,'-')
'--------------------String is immutable---------------------'
c.center(60,'*')
'********************String is immutable*********************'
c.center(60,'0')
'00000000000000000000String is immutable000000000000000000000'
'12'.zfill(3)
'012'
'12'.zfill(8)
'00000012'
'12345'.zfill(4)
'12345'
#SEAch & FIND METHODS
c.find('i')
3
c.find('m')
11
c.find('z')
-1
c.find('i')
3
c
'String is immutable'
c.index('s')
8
c.index('i')
3
c.rindex('i')
10
c.index('z')
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    c.index('z')
ValueError: substring not found
c
'String is immutable'
c.count('g')
1
c.count('m')
2
c.count('b')
1
# REPLACE & MODIFY METHODS
c.replace('i','0')
'Str0ng 0s 0mmutable'
c.replace('string','float')
'String is immutable'
c.replace('String','Flaot')
'Flaot is immutable'
c.maketrans('aeiou','12345')
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
c.translate(c.maketrans('aeiou','12345'))
'Str3ng 3s 3mm5t1bl2'
#SPLITTING & JOIN METHODS
c.split()
['String', 'is', 'immutable']
KeyboardInterrupt
'String is immutable'

'String is immutable'
'String is immutable'.split()
['String', 'is', 'immutable']
'String is immutable'.split('_')
['String is immutable']
'String is immutable'.split(',')
['String is immutable']
String is immutable'.split(' '1)
SyntaxError: unterminated string literal (detected at line 1)
s='''
python
programming
language'''
s
'\npython\nprogramming\nlanguage'
s.spltlines()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    s.spltlines()
AttributeError: 'str' object has no attribute 'spltlines'. Did you mean: 'splitlines'?
s.splitlines()
['', 'python', 'programming', 'language']
>>> ['', 'python', 'programming', 'language'].join()
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    ['', 'python', 'programming', 'language'].join()
AttributeError: 'list' object has no attribute 'join'
>>> ''.join(['','python','programming','language'])
'pythonprogramminglanguage'
>>> '-'.join(['','python','programming','language'])
'-python-programming-language'
>>> ','.join([1,2,3])
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    ','.join([1,2,3])
TypeError: sequence item 0: expected str instance, int found
>>> ','.join(['1','2','3'])
'1,2,3'
>>> 'python.py'.partition('.')
('python', '.', 'py')
>>> s='java,python,c,c++'
>>> s.partition(',')
('java', ',', 'python,c,c++')
>>> s.rpartition(',')
('java,python,c', ',', 'c++')
>>> # WHITESPACE & TRIMMING METHODS
>>> c.strip()
'String is immutable'
>>> s = 'Hello    World'
>>> s
'Hello    World'
>>> c.strip()
'String is immutable'
>>> 'Hello World'.strip()
'Hello World'
>>> c.strip()
'String is immutable'
>>> s.strip()
'Hello    World'
>>> s.lstrip()
'Hello    World'
>>> c.rstrip()
'String is immutable'
>>> s.rstrip()
'Hello    World'
>>> # ENCODING & DECODING METHODS
>>> >text = "Hello 🙂 "
SyntaxError: invalid syntax
>>> text = "Hello 🙂 "
>>> text.encode()
b'Hello \xf0\x9f\x99\x82 '
>>> b'Hello \xf0\x9f\x99\x82 '.decode()
'Hello 🙂 '

Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> c = 'string.py'
>>> c.startswith('str')
True
>>> c.startswith('python')
False
>>> c.endswith('python')
False
>>> c.endswith("py")
True
>>> c.islower()
True
>>> c.isupper()
False
>>> 'PYTHONV13'.isupper()
True
>>> c.isalpha()
False
>>> c.isalnum()
False
>>> c.istitle()
False
>>> 's123'.isalnum()
True
>>> 's.123'.isalnum()
False
>>> '       '.isspace()
True
>>> 'l         '.isspace()
False
>>> 'this is title'.isspace()
False
>>> 'This Is Title'.isspace()
False
>>> 'This Is Title'.istite()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    'This Is Title'.istite()
AttributeError: 'str' object has no attribute 'istite'. Did you mean: 'istitle'?
>>> 'This Is Title'.istitle()
True
>>> 'my@var.isidentifier()
SyntaxError: unterminated string literal (detected at line 1)
>>> 'my@var'.isidentifier()
False
>>> 'myvar'.isidentifier()
True

Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
data = {'name':'lokesh','batch':63,'course':'PFS'}
data
{'name': 'lokesh', 'batch': 63, 'course': 'PFS'}
data['name']
'lokesh'
data['batch']
63
data['course']
'PFS'
63 in data
False
data.get('age','key is not present')
'key is not present'
data.get('course','key is not present')
'PFS'
data['batch']=64
data
{'name': 'lokesh', 'batch': 64, 'course': 'PFS'}
data['skills']=['pyhon','mysql','flask']
data
{'name': 'lokesh', 'batch': 64, 'course': 'PFS', 'skills': ['pyhon', 'mysql', 'flask']}
data['age'] =21
data
{'name': 'lokesh', 'batch': 64, 'course': 'PFS', 'skills': ['pyhon', 'mysql', 'flask'], 'age': 21}
data.update({'phno':9876543210,'email':'loki@gmail.com'})
data
{'name': 'lokesh', 'batch': 64, 'course': 'PFS', 'skills': ['pyhon', 'mysql', 'flask'], 'age': 21, 'phno': 9876543210, 'email': 'loki@gmail.com'}
data
{'name': 'lokesh', 'batch': 64, 'course': 'PFS', 'skills': ['pyhon', 'mysql', 'flask'], 'age': 21, 'phno': 9876543210, 'email': 'loki@gmail.com'}
data.pop('age')
21
data
{'name': 'lokesh', 'batch': 64, 'course': 'PFS', 'skills': ['pyhon', 'mysql', 'flask'], 'phno': 9876543210, 'email': 'loki@gmail.com'}
data.pop('phno')
9876543210
data
{'name': 'lokesh', 'batch': 64, 'course': 'PFS', 'skills': ['pyhon', 'mysql', 'flask'], 'email': 'loki@gmail.com'}
del data['name']
data
{'batch': 64, 'course': 'PFS', 'skills': ['pyhon', 'mysql', 'flask'], 'email': 'loki@gmail.com'}
data.popitem()
('email', 'loki@gmail.com')
data
{'batch': 64, 'course': 'PFS', 'skills': ['pyhon', 'mysql', 'flask']}
data.popitem()
('skills', ['pyhon', 'mysql', 'flask'])
data
{'batch': 64, 'course': 'PFS'}
data.clear()
data
{}
data ={'name': 'lokesh', 'batch': 64, 'course': 'PFS', 'skills': ['pyhon', 'mysql', 'flask'], 'age': 21, 'phno': 9876543210, 'email': 'loki@gmail.com'}
data
{'name': 'lokesh', 'batch': 64, 'course': 'PFS', 'skills': ['pyhon', 'mysql', 'flask'], 'age': 21, 'phno': 9876543210, 'email': 'loki@gmail.com'}
data.keys()
dict_keys(['name', 'batch', 'course', 'skills', 'age', 'phno', 'email'])
data.values()
dict_values(['lokesh', 64, 'PFS', ['pyhon', 'mysql', 'flask'], 21, 9876543210, 'loki@gmail.com'])
data.items()
dict_items([('name', 'lokesh'), ('batch', 64), ('course', 'PFS'), ('skills', ['pyhon', 'mysql', 'flask']), ('age', 21), ('phno', 9876543210), ('email', 'loki@gmail.com')])
sorted(data)
['age', 'batch', 'course', 'email', 'name', 'phno', 'skills']
sorted(data,reverse=True)
['skills', 'phno', 'name', 'email', 'course', 'batch', 'age']
>>> max(data)
'skills'
>>> min(data)
'age'
>>> data
{'name': 'lokesh', 'batch': 64, 'course': 'PFS', 'skills': ['pyhon', 'mysql', 'flask'], 'age': 21, 'phno': 9876543210, 'email': 'loki@gmail.com'}
>>> data.get('age')
21
>>> data.setdefault('age',0)
21
>>> data['age']
21
>>> data
{'name': 'lokesh', 'batch': 64, 'course': 'PFS', 'skills': ['pyhon', 'mysql', 'flask'], 'age': 21, 'phno': 9876543210, 'email': 'loki@gmail.com'}
>>> data.setdefault('name','')
'lokesh'
>>> data
{'name': 'lokesh', 'batch': 64, 'course': 'PFS', 'skills': ['pyhon', 'mysql', 'flask'], 'age': 21, 'phno': 9876543210, 'email': 'loki@gmail.com'}
>>> len(data)
7
>>> all(data)
True
>>> data
{'name': 'lokesh', 'batch': 64, 'course': 'PFS', 'skills': ['pyhon', 'mysql', 'flask'], 'age': 21, 'phno': 9876543210, 'email': 'loki@gmail.com'}
>>> a
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a={1:1,2:2]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
>>> a={1:1,2:2}
>>> a
{1: 1, 2: 2}
>>> b=a
>>> b[3]=3
>>> b
{1: 1, 2: 2, 3: 3}
>>> c = a.copy()
>>> c[4]=4
>>> c
{1: 1, 2: 2, 3: 3, 4: 4}
>>> a
{1: 1, 2: 2, 3: 3}
>>> d = dict.fromkeys(['a','b'],0)
>>> d
{'a': 0, 'b': 0}

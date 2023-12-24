>>> print'hello'
  File "<stdin>", line 1
    print'hello'
    ^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

>>> print('hello')
hello
>>>



>>> print(age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'age' is not defined
>>>

>>> age = 10
>>> print(age)
10
>>>


>>> numbers = [1, 2, 3, 4, 5]
>>> numbers[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range


IndexError: list index out of range
>>> numbers[4]
5
>>>




>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'

>>> import math
>>>



>>> import math
>>> math.PI
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?

>>> import math
>>> math.pi
3.141592653589793
>>>




>>> users = {'name':'Asab', 'age':250, 'country':'Finland'}
>>> users['county']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'county'
>>>

>>> users['country']
'Finland'
>>>




>>> 20 + '20'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>>

>>> 20 + '20'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 20 + int('20')
40
>>>



>>> from math import power
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'power' from 'math' (unknown location)
>>>

>>> from math import power
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'power' from 'math' (unknown location)
>>> from math import pow
>>> pow(5,2)
25.0
>>>



>>> int('29b')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '29b'

  


Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>>




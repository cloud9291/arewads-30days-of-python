#Excercise Level  1 2
# 1. check the python version you are using
import platform
print("Python version:")
print(platform.python_version())

''' 2. Open the python interactive shell and do the following operatons. 
the operands are 3 and 4'''
print(3 + 4)             # addition(+)
print(4 - 3)             # subtraction(-)
print(3 * 4)             # multiplication(*)
print(4 / 3)             # division(/)
print(3 ** 4)            # exponential(**)
print(4 % 3)             # modulus(%)
print(4 // 3)            # Floor division operator(//)

# 3. Write strings on the python interactive shell. the strings are the following:
name = "Masud"
family_name = "Akogun"
country = "Nigeria"

print(name)
print(family_name)
print(country)
print("I am enjoying 30 days of python")

# 4. Check the data types of the following data:
print(type(10))          # Int
print(type(9.8))         #double
print(type(3.14))        # Float
print(type(4 - 4j))      # Complex number
print(type(['Asabeneh', 'Python', 'Finland']))  # list
print(type('Masud')) # string
print(type('Akagun')) # string
print(type('Nigeria')) # string



#Exercise level 3
''' 1. Write an example for different Python data types such as 
Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary'''

# Integer
integer = 42
print('integer:', integer)

# Float
float = 3.14
print('float', float)

# Complex
complex = 2 + 3j
print('Complex:',complex)

# String
string = "Hello, World!"
print('String:', string)

# Boolean
boolean_var = True
print('Boolean:', boolean_var)

# List
list_num = [1, 2, 3, 4, 5]
print('List:',list_num)

# Tuple
tuple_var = (10, 20, 30, 40, 50)
print('Tuple:',  tuple_var)

# Set
set_var = {1, 2, 3, 4, 5}
print("Set:", set_var)

# Dictionary
dictionary = {'name': 'John', 
              'age': 25, 
              'city': 'New York'}
print('Dictionary:', dictionary)


# 2. Find an Euclidian distance between (2, 3) and (10, 8

import math

# Coordinates  points
p1 = (2, 3)
p2 = (10, 8)
# Euclidean distance calculation
distance = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
print('The Euclidean distance is:', distance)

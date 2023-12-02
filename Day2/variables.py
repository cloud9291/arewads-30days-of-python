#Exercise Level 1
#Day 2: 30 Days of python programming

#Declare a first name variable and assign a value to it
first_name = 'Masud'
#Declare a last name variable and assign a value to it
last_name = 'Abdulyaqeen'
#Declare a full name variable and assign a value to it
full_name = 'Masud Abdulyaqeen'
#Declare a country variable and assign a value to it
country   = 'Nigeria'
#Declare a city variable and assign a value to it
city      = 'Jos'
#Declare an age variable and assign a value to it
age       = 26
#Declare a year variable and assign a value to it
year      = 1996
#Declare a variable is_married and assign a value to it
is_married = 'Single'
#Declare a variable is_true and assign a value to it
is_true    =  True
#Declare a variable is_light_on and assign a value to it
is_light_on = "yes"

print('First name:', first_name)
print('Last name:', last_name)
print('Full name:', full_name)
print('Country', country)
print('City:', city)
print('Year:', year)
print('Married:', is_married)
print('True:', is_true)
print('is light on:', is_light_on)

#Declare multiple variable on one line
first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on = 'masud', 'Abdulyaqeen', 'Masud Abdulyaqeen', 'Nigeria', 'Jos', 26, 1996, 'single', True, 'yes'

print(first_name, last_name, country, city, age, year, is_married, is_true, is_light_on )


#Exercises: Level 2
# 1. Check the data type of all your variables using type() built-in function
# Printing out types
print(type(last_name))     # str
print(type(first_name))     # str
print(type(full_name))      # str
print(type(country))        #str
print(type(city))           #str
print(type(age))            #int
print(type(year))           #int
print(type(is_married))     #str
print(type(is_true))        #boolean
print(type(is_light_on))    #str

# 2. Using the len() built-in function, find the length of your first name

print('First name:', first_name)
print('First name length:', len(first_name))

# 3. Compare the length of your first name and your last name
#first_name = 'Masud'
#last_name = 'Abdulyaqeen'

length_first_name_is_greater = len(first_name) > len(last_name)
length_first_name_is_smaller = len(first_name) < len(last_name)
print(length_first_name_is_greater)
print(length_first_name_is_smaller)

# 4. Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
#Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
#Subtract num_two from num_one and assign the value to a variable diff
diff = num_two - num_one
#Multiply num_two and num_one and assign the value to a variable produc
product  = num_two * num_one
#Divide num_one by num_two and assign the value to a variable division
division = num_one /num_two
#Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
#Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
#Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two

print("Total:", total)
print("Difference:", diff)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)
print("Exponentiation:", exp)
print("Floor Division:", floor_division)

# 5.The radius of a circle is 30 meters
# i. Calculate the area of a circle and assign the value to a variable name of area_of_circle
import math

radius = 30
area_of_circle = math.pi*(radius **2)
print('the area of a circle:', area_of_circle)

#Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2*math.pi * radius
print('the circumference of a circle:', circum_of_circle)
#Take radius as user input and calculate the area.
radius = float(input( "Enter radius  "))
area_of_circle = math.pi*(radius **2)
print('the area of a circle:', area_of_circle)

''' 6. Use the built-in input function to get first name, last name, 
country and age from a user and store the value to their corresponding variable names'''
first_name = input("Enter your first name  ")
last_name = input("Enter your last name  ")
country = input("Enter your country  ")
age = input("Enter your age  ")

print('First Name:', first_name)
print('Last Name:', last_name)
print('Country:', country)
print('Age:', age)


# 7. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')

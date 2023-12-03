
# 1. Declare your age as integer variable
age = 25
# 2. Declare your height as a float variable
height = 4.5
# 3.Declare a variable that store a complex number
comp_lex = 4 +1j

print('the integer variable age is:', age) 
print('the float variable height is:', height)
print('the complex number is:', comp_lex)

''' 4. Write a script that prompts the user to enter base and 
 height of the triangle and calculate an area of this triangle 
(area = 0.5 x b x h).'''
base = float(input("Enter base"))
height = float(input("Enter height"))
area_of_triangle = (0.5 * base * height)
print("the area of triangle is:", area_of_triangle)

''' 5. Write a script that prompts the user to enter side a, 
side b, and side c of the triangle. Calculate the perimeter of 
the triangle (perimeter = a + b + c)'''

side_a = input('Enter side a of a triangle  ')
side_b = input('Enter side b of a triangle  ')
side_c = input("Enter side c of a triangle  ")
perimeter = (side_a + side_b + side_c)
print('The perimeter of the triangle is:', perimeter)

''' 6. Get length and width of a rectangle using prompt. Calculate 
its area (area = length x width) and perimeter (perimeter = 2 x (length + width))'''

length = float(input('Enter the length of a rectangle  '))
width = float(input('Enter the width of a rectangle  '))
area_of_rectangle = length * width
perimeter_of_rectangle = (2*(length + width))
print('the area of a rectangle is:', area_of_rectangle)
print('the perimeter of a rectangle is:', perimeter_of_rectangle)

''' 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) 
and circumference (c = 2 x pi x r) where pi = 3.14.'''

radius = float(input('Enter the radius of a circle'))
pi = 3.14
area = (pi * radius * radius)
circumference = (2 * pi * radius)
print('the area is:', area)
print('the circumference is:', circumference)

# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope_1 =2
y_intercept = -2
x_intercept = y_intercept  / slope_1

print('slope:', slope_1)
print('x-intercept:', x_intercept)
print('y-intercept:', y_intercept)


''' 9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance 
between point (2, 2) and point (6,10) '''
from math import sqrt
x1 = 2
y1 = 2
x2 = 6
y2 = 10
m = ((y2 - y1)/ (x2 -x1))
distance = sqrt((x1 - y1)**2 + (x2 -y2)**2)
print('the slope is:', m)
print('the euclidean distance is:', distance)


# 10. Compare the slopes in tasks 8 and 9.
print(m == slope_1)

''' 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use 
different x values and figure out at what x value y is going to be 0.'''

# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python'))
print(len('dragon'))
print(len('python') > len('dragon'))

# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

# 14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print("Use in operator to check if jargon is in the sentence", 'jargon' in 'I hope this course is not full of jargon')

# 15. There is no 'on' in both dragon and python
print('there is no on in both dragon and python', 'on' not in 'dragon' and 'python')

# 16. Find the length of the text python and convert the value to float and convert it to string
text = 'python'
print(len('text'))
print(float(len(text)))
print(str(text))


# 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = int(input('enter number  '))
even = (number % 2 == 0) 
print('the number is even', even) 

# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print((7 // 3) == 2.7)

# 19. Check if type of '10' is equal to type of 10
print (type('10') == type(10))

# 20.Check if int('9.8') is equal to 10
print(int(float('9.8') == 10))

# 21. Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = float(input('Enter hours  '))
rate_per_hour = float(input('Enter the rate per hour  '))
person = ( hours * rate_per_hour)
print('your payment is:', person)

''' 22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person
 can live. Assume a person can live hundred years'''

# Constants
days_in_year = 365
hours_in_day = 24
minutes_in_hour = 60
seconds_in_minute = 60

# Prompt the user to enter the number of years
years_lived = float(input("Enter the number of years you have lived: "))
# Calculate the number of seconds a person can live
seconds_lived = years_lived * days_in_year * hours_in_day * minutes_in_hour * seconds_in_minute
# print the number of seconds a person can lived is
print("The number of seconds you can live is:", seconds_lived)



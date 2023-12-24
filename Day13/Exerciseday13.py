#Exercises: Day 13
#1. Filter only negative and zero in the list using list comprehension

negative_numbers = [i for i in range(-4, 6) if i <=0]
print(negative_numbers)  
 
#2. Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flattened_list = [ i for row in list_of_lists for i in row] 
print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]


#3. Using list comprehension create the following list of tuples:

result = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]

# Printing the result
for item in result:
    print(item)


#4. Flatten the following list to a new list:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries_list = [country for row in countries for country in row]
print(countries_list)

#5. Change the following list to a list of dictionaries:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries_list_dic = [{'country': country[0], 'capital': country[1]} for row in countries for country in row]
print(countries_list_dic)


#6. Change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
fullname = [name[0]+ ' ' + name[1] for row in names for name in row]
print(fullname)


#7. Write a lambda function which can solve a slope or y-intercept of linear functions

linear_function = lambda x, m_b: m_b[0] * x + m_b[1]

# Slope = 2, y-intercept = 3
slope_intercept = (2, 3)

# Calculate y for x = 5 using the lambda function
result = linear_function(5, slope_intercept)

print(result)





#30days of python Day4 Excercises 

'''1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' 
to a single string, 'Thirty Days Of Python'.'''
string_1= 'Thirty'
string_2= 'Days'
string_3= 'Of'
string_4= 'Python'
space = ' '
concatenation= (string_1+space+ string_2+space+ string_3+space + string_4)
print('the concatenation into single string:', concatenation)

#2.Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
string_1= 'Coding'
string_2= 'For'
string_3= 'All'
space = ' '
concatenation= (string_1+space+ string_2+space+ string_3)
print('the concatenation into single string:',concatenation)

#3. Declare a variable named company and assign it to an initial value "Coding For All"
company = "Coding For All"

# 4.Print the variable company using print().
print(company)

#5. Print the length of the company string using len() method and print().
print("the length of company is:" ,len(company))

#6.Change all the characters to uppercase letters using upper() method.
print(company.upper())

#7. Change all the characters to lowercase letters using lower() method.
print(company.lower())

#8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
string_value = 'Coding For All'
print(string_value.capitalize()) # 'Coding For All'
print(string_value.title()) #return a tile case
print(string_value.swapcase())

#9. Cut(slice) out the first word of Coding For All string.
word = 'Coding For All string'
first_word = word[0:6] # starts at zero index and up to 6 but 
print(first_word) #Coding

'''10. Check if Coding For All string contains a word Coding using 
the method index, find or other methods.'''

string_to_check = "Coding For All"
word_to_find = "Coding"

# Using index
index = string_to_check.find(word_to_find)
index_message = (index != -1) #
print(index_message)

# Using find
index = string_to_check.find(word_to_find)
index_message = (index != -1) #
print(index_message)

#11. Replace the word coding in the string 'Coding For All' to Python.
word_replace = 'Coding For All'
print(word_replace.replace('Coding', 'Programming')) # 'Programming For All'

#12. Change Python for Everyone to Python for All using the replace method or other methods.
word_replace = 'Python for Everyone'
print(word_replace.replace('Python for Everyone', 'Python for All')) # 'Programming For All'

#13. Split the string 'Coding For All' using space as the separator (split()).
split_string = 'Coding, For, All'
print(split_string.split(', ')) # ['Coding', 'For', 'All']

#14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
split_string2 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(split_string2.split())

#15. What is the character at index 0 in the string Coding For All.
character = 'Coding For All'
character_at_index_0 = character[0]
print('character at index 0 is:', character_at_index_0[0])

#16. What is the last index of the string Coding For All.
character = 'Coding For All'
last_letter = character[-1]
print(last_letter) # 

#17. What character is at index 10 in "Coding For All" string..
character = 'Coding For All'
character_at_index_10 = character[10]
print('character at index 10 is:', character_at_index_10)

#18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
name = "Python For Everyone"
acronym = ''.join(word[0] for word in name.split())
print(acronym)

#19. Create an acronym or an abbreviation for the name 'Coding For All'.

name = "Coding For All"
acronym = ''.join(word[0] for word in name.split())
print(acronym)

#20. Use index to determine the position of the first occurrence of C in Coding For All.
first_occurence = 'Coding For All'
print(first_occurence.find('C'))  # 0

#21.Use index to determine the position of the first occurrence of F in Coding For All. 
first_occurence = 'Coding For All'
print(first_occurence.find('F')) #7

#22. Use rfind to determine the position of the last occurrence of l in Coding For All People 
first_occurence = 'Coding For All People'
print(first_occurence.rfind('F')) #7

'''23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 
'You cannot end a sentence with because because because is a conjunction'''
first_occurence = '''You cannot end a sentence with because 
because because is a conjunction'''
print('the fast occurence and position of the word because is ', first_occurence.find('because'))#31

'''24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence 
with because because because is a conjunction'''
last_occurence = '''You cannot end a sentence with because 
because because is a conjunction'''
print('the last occurence and position of the word because is', first_occurence.rindex('because'))#48

#25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
slice_word = 'You cannot end a sentence with because because because is a conjunction'
slice_phrase = slice_word[31:55] #'because because because'
print(slice_phrase)

#26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
first_occurence = '''You cannot end a sentence with because 
because because is a conjunction'''
print('the fast occurence and position of the word because is ', first_occurence.find('because'))

'''27. Slice out the phrase 'because because because' in the following sentence: 
'You cannot end a sentence with because because because is a conjunction'''
slice_word = 'You cannot end a sentence with because because because is a conjunction'
slice_phrase = slice_word[31:55] #'because because because'
print(slice_phrase)

#28. Does ''Coding For All' start with a substring Coding?
start_substring = 'Coding For All'
print(start_substring.startswith('Coding')) # True

#29. Does 'Coding For All' end with a substring coding?
end_substring = 'Coding For All'
print(end_substring.endswith('coding')) # False

#30 '  Coding For All      '  , remove the left and right trailing spaces in the given string.
challenge = '  Coding For All      '
print(challenge.strip()) # 'Coding For All'

'''31.Which one of the following variables return True when we use the method isidentifier():
30DaysOfPython
thirty_days_of_python'''

identifier = '30DaysOfPython'
print(identifier.isidentifier()) # False, because it starts with a number
identifier = 'thirty_days_of_python'
print(identifier.isidentifier()) # True

'''32.The following list contains the names of some of python libraries: 
['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.'''

python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = '# '.join(python_libraries)
print(result) # 'Django# Flask# Bottle #Falcon'

#33.  Use the new line escape sequence to separate the following sentences.
'''I am enjoying this challenge.
   I just wonder what is next.'''
print('I am enjoying this challenge.\n I just wonder what is next.')

#34.  Use a tab escape sequence to write the following lines.
'''Name      Age     Country   City
Asabeneh  250     Finland   Helsinki'''
print('Name    \tAge\tCountry\tCity') # adding tab space or 4 spaces 
print('Asabeneh\t250\tFinland\tHelsinki')

#35. Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string)

# 36. Make the following using string formatting methods:
a = 8
b = 6

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))
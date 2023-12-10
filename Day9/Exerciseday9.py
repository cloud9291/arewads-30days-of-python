#Exercises9: Level 1

#1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

user = int(input('Enter your age:\t'))
if user >= 18:
    print('You are old enough to drive')
else:
    years_to_wait = 18 - user 
    print('please wait for the missing amount of years',  years_to_wait)




#3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

a = int(input('enter the first number\t'))
b = int(input('enter the second number\t'))
if a  > b:
    print('a is greater than b')
elif  a < b:
    print('a is smaller than b')
else:
    print('a is equal to b')


### Exercises9: Level 2
#1. Write a code which gives grade to students according to theirs scores:

scores = int(input('enter score ' ' '))
if scores >= 80:
    grade = 'A'
elif scores >=70:
    grade = 'B'
elif scores >=60:
    grade = 'C'
elif scores >=50:
    grade = 'D'
else:
    grade = 'F'

print('your grade is:', grade)

'''2. Check if the season is Autumn, Winter, Spring or Summer. 
If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer'''

season = str(input('Enter season: '))

if season in ['September', 'October', 'November']:
    print('The season is Autumn.')
elif season in ['December', 'January', 'February']:
    print('The season is Winter.')
elif season in ['March', 'April', 'May']:
    print('The season is Spring.')
elif season in ['June', 'July', 'August']:
    print('The season is Summer.')
else:
    print('Invalid input or not a recognized season.')


#3. The following list contains some fruits:If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

fruits = ['banana', 'orange', 'mango', 'lemon']

new_fruit = input("Enter a fruit to check or add to the list: ")

# Check if the fruit is already in the list
if new_fruit.lower() in [f.lower() for f in fruits]:
    print("That fruit already exists in the list.")
else:
    fruits.append(new_fruit.lower())
    print(f"The fruit '{new_fruit}' has been added to the list. Updated list: {fruits}")



#Exercise9: Level 3
#4. Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
} } 

 #Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    dictionary = person['skills']

    if dictionary:
        middle_index = len(dictionary) // 2

        print('middle list:', dictionary[middle_index])

    else:
        print('no skills key')


 # Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person:
    has_skill = person['skills']
    if 'Python' in has_skill:
        print('the person has python skill')
    else:
        print('the person dosent has the skill python')
else:
    print('the dictionary dosent has skills')
      


  
 # If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!

skills_input = input("Enter the person's skills ")
skills = [skill.strip() for skill in skills_input.split(',')]

if 'JavaScript' in skills and 'React' in skills:
    print('He is a front end developer')
elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
    print("He is a backend developer")
elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
    print("He is a fullstack developer")
else:
    print("Unknown title")


 # If the person is married and if he lives in Finland, print the information in the following format:
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Check if the person is married and lives in Finland
if person.get('is_married') and person.get('country') == 'Finland':
    print(f"{person['first_name']} lives in highland and is married.")

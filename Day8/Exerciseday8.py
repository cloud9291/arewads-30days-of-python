
# challenge excercise day 8
#1. Create an empty dictionary called dog
dog = {}

#2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'pupy'
dog['color'] = 'brown'
dog['breed'] = 'none'
dog['legs'] = '4'
dog['age'] = 100
print(dog)

#3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionar

student={
'first_name': 'Masud',
'last_name': 'Abdulyaqeen',
'gender':     'Male',
'age':        '26',
'marital_status': 'Single',
'skills':     ['Data Analytic Engineer', 'HTML', 'Python', 'Docker'],
'country':    'Nigeria',
'city':       'Kano',
'address':    'gwarzo road'
}
print(student)

#4. Get the length of the student dictionary
print('the lenght of the dic is:', len(student))

#5. Get the value of skills and check the data type, it should be a list
print(student.get('skills'))
print(type(student.get('skills')))

#6. Modify the skills values by adding one or two skills
student['skills'].extend(['java', 'kotlin'])
print(student)

#7. Get the dictionary keys as a list
keys = student.keys()
print('the dictionary keys value are:', keys)

#8. Get the dictionary values as a list
values = student.values()
print('the dictionary values are:', values)

#9. Change the dictionary to a list of tuples using items() method

print('the dictionary list is:', student.items())

#10. Delete one of the items in the dictionary
student.pop('address')
print(student)

#11. Delete one of the dictionarie
del student['first_name']
print(student)

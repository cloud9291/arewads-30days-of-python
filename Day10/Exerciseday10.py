#Exercise 1
#1 Iterate 0 to 10 using for loop, do the same using while loop.
#using for loop
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers: 
    print(number) #prints from 0 to 10

#using while loop
numbers = 0
while numbers <= 10:
    print(numbers)
    numbers = numbers +1   #prints from 0 to 10


#2. Iterate 10 to 0 using for loop, do the same using while loop.
# Using a for loop
for i in range(10, -1, -1):
    print(i)


# Using a while loop
count = 10
while count >= 0:
    print(count)
    count -= 1

#3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
for hash in range(1, 8,):
        print('#' * hash)

#4. Use nested loops to create the following:

for n in range(8):
    for j in range(8):
        if j % 2 == 0:
            print('#', end=' ')
        else:
            print(' ', end=' ')
    print()  # Move to the next line 


#5. Print the following pattern:
for i in range(11):
    result = i * i
    print(f"{i} x {i} = {result}")

#6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
lists = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in lists:
    print(i)

#7. Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(0, 101, 2):
  print(i)

#8. Use for loop to iterate from 0 to 100 and print only odd number
for i in range(1, 101, 2):
  print(i)

#Exercises: Level 2
#1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum = 0 

for i in range(101):  
    sum += i

print("The sum of all numbers from 0 to 100 is:", sum)

#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

sum_even = 0
sum_odd = 0

for number in range(101):
    if number % 2 == 0:
        sum_even += number
    else:
        sum_odd += number

print(f"The sum of all even numbers from 0 to 100 is: {sum_even}")
print(f"The sum of all odd numbers from 0 to 100 is: {sum_odd}")

#Exercises: Level 3
#Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
countries_with_land = [country for country in countries if 'land' in country.lower()]
print("Countries containing 'land':", countries_with_land)


#2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.3
fruit_list = ['banana', 'orange', 'mango', 'lemon']

# Using a loop to reverse the order of the list
reversed_fruit_list = []

for fruit in reversed(fruit_list):
    reversed_fruit_list.append(fruit)

print("Original fruit list:", fruit_list)
print("Reversed fruit list:", reversed_fruit_list)


#3. 

# 30days of python day5 exercise
#1. Declare an empty list
empty_list = []
print(empty_list)

#2. Declare a list with more than 5 items
list_items = ['masud', 'abdul', 'nigeria', 'kano', 25]
print(list_items)

#3. Find the length of your list
list_items = ['masud', 'abdul', 'nigeria', 'kano', 25]
print(len(list_items ))

#4. Get the first item, the middle item and the last item of the list
list_items = ['masud', 'abdul', 'nigeria', 'kano', 25]
first_item = list_items[0] # we are accessing the first item using its index
print(first_item)      # masud
middle_item = list_items[2]
print(middle_item)     # nigeria
last_item = list_items[4]
print(last_item) # 25


#5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_type = ['Masud', 25, 70.5, 'single', 'no1 rijiyar zaki', ]
print(mixed_data_type)

#6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#7. # Print the list
print(it_companies)

#8. Print the number of companies in the list
print(len(it_companies))

#9. Print the first, middle and last company
first_company_name = it_companies[0]
print(first_company_name)
middle_company_name = it_companies[4]
print(middle_company_name)
last_company_name = it_companies[-1]
print(last_company_name)

#10. Print the list after modifying one of the companies
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies[0]= 'Instagram'
print(it_companies)

#11. Add an IT company to it_companies
it_companies.append('It Company')
print(it_companies)

#12. Insert an IT company in the middle of the companies list
it_companies.insert(3, 'It Company ' )
print(it_companies)

#13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1]= it_companies[1].upper()
print(it_companies) #GOOGLE

#14. Join the it_companies with a string '#;  '
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
joined_company = '# '.join(it_companies)
print(joined_company) # 'Facebook # Google# Microsoft# Apple# IBM# Oracle# Amazon'

#15. Check if a certain company exists in the it_companies list.
print('Apple' in it_companies)

#16. Sort the list using sort() method
sort_list = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
sort_list.sort()
print(sort_list)

#17. Reverse the list in descending order using reverse() method
reverse_list = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
reverse_list.sort(reverse=True)
print(reverse_list)

#18. Slice out the first 3 companies from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
slice_1 = it_companies[0:3]
print(slice_1)

#19.Slice out the last 3 companies from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
slice_2 = it_companies[-3:]
print('the last 3 company from the list is :', slice_2)

#20. Slice out the middle IT company or companies from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
slice = it_companies[2:5]
print('the middle company from the list is:',slice)

#21. Remove the first IT company from the list
remove_it_company = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
remove_it_company.remove('Facebook')
print(remove_it_company)#Facebook

#22. Remove the middle IT company or companies from the list
remove_it_company = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
del remove_it_company[2:5]
print(remove_it_company)#

#23. Remove the last IT company from the list
remove_it_company = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
remove_it_company.pop()
print(remove_it_company)#the las company Amazon as been removed

#24. Remove all IT companies from the list
clear_list = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
clear_list.clear()
print(clear_list)#empty list[]

#25. Destroy the IT companies list
del it_companies[:]
print(it_companies)

#26. Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
join_list = front_end + back_end
print(join_list)

'''27.After joining the lists in question 26. Copy the joined list 
and assign it to a variable full_stack. Then insert Python and SQL after Redux.'''
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
join_list = front_end + back_end
full_stack = join_list
append_2 = ['Python', 'SQL']
full_stack.extend(append_2)
print(full_stack)

#Exercise level 2
#1. The following is a list of 10 students ages:ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#Sort the list and find the min and max age
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
minimum_age = min(ages)
maximum_age = max(ages)
print(ages)
print(minimum_age)
print(maximum_age)

#Add the min age and the max age again to the list
ages.append(minimum_age)
ages.append(maximum_age)
print(ages)

#Find the median age (one middle item or two middle items divided by two
n = len(ages)
middle_age = n // 2

if n % 2 == 0:
    median_age = (ages[middle_age - 1] + ages[middle_age]) / 2
else:
    median_age = ages[middle_age]

print("Median Age:", median_age)

# Find the average age
average_age = sum(ages) / len(ages)
print("Average Age:", average_age)


# Find the range of ages
age_range = maximum_age - minimum_age
print("Age Range:", age_range)


# Compare the value of (min - average) and (max - average), use abs() method
min_difference = abs(minimum_age - average_age)
max_difference = abs(maximum_age - average_age)
print("Difference (min - average):", min_difference)
print('Difference (max - average):', max_difference)

#1. Find the middle country(ies) in the countries list
countries =[
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
  'Zimbabwe']
middle_countries = countries[len(countries) // 2 - 1 : len(countries) // 2 + 1]
print(middle_countries)

#2. Divide the countries list into two equal lists
if len(countries) % 2 == 0:
    first_half = countries[:len(countries) // 2]
    second_half = countries[len(countries) // 2:]
else:
    first_half = countries[:len(countries) // 2 + 1]
    second_half = countries[len(countries) // 2 + 1:]
    print('the first half is:', first_half)
    print('the second half is:', second_half)

#3.Unpack the first three countries and the rest as scandic countries
country1, country2, country3, *scandic_countries = countries
print('The first country',country1)
print('the second country',country2)
print('the third country',country3)
print('the scandic countries',scandic_countries)
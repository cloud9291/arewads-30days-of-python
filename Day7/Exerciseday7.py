


#Exercises: Level 1

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24] 

#1. Find the length of the set it_companies
print('the total number of the It companies is:', len(it_companies))

#2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print('the twitter company as been added:', it_companies)

#3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['Telegram', 'TikTok', 'Multilinks'])
print(it_companies)

#4. Remove one of the companies from the set it_companies
it_companies.remove('IBM')
print(it_companies)
#5. What is the difference between remove and discard
print(''' the diff between remove and discard is that, the remove 
word raise errors if the item to be removed is not in the set while the 
discard checks if the item is present it remove it and if not nothing 
happen and no errors ''')



#Exercises: Level 2

#1.Join A and B
join_AB = A.union(B)
print('the combination of A and B is:', join_AB)

#2. Find A intersection B
inter_sect = A.intersection(B)
print('the intersection of A and B is:', inter_sect)

#3. Is A subset of B
sub_set = A.issubset(B)
print(sub_set)#True

#4. Are A and B disjoint sets
dis_joint = A.isdisjoint(B)
print(dis_joint)#False

#5. Join A with B and B with A
first_joint = A.union(B) | B.union(A)
print(first_joint)

#6. What is the symmetric difference between A and B
sym_diff = A.symmetric_difference(B)
print('the symmetric_difference bet A and B is:', sym_diff)

#7. Delete the sets completely
del A, B


#Exercises: Level 3
#1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?

ages = set(age)
print('the ', ages)
length_ages_is_greater = len(ages) > len(age)
length_ages_is_smaller = len(ages) < len(age)
print(length_ages_is_greater)
print(length_ages_is_smaller)

#3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people'
word = sentence.split()
unique_word = set(word)
num_of_unique_word = len(unique_word)
print(num_of_unique_word)#10


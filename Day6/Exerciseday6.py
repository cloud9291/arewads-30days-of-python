
#Exercise 1
#1. Create an empty tuple

empty_tuple = () #empty tuple
print(empty_tuple)

#2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

tuple_sisters = ('Maryam', 'Nasmat', 'Hawwa', 'Hamdalah')
tuple_brothers= ('Ashir', 'A.mumin')
print('the names of my sister her:\t' ,tuple_sisters)
print('the names of my brothers are:\t', tuple_brothers)

#3. Join brothers and sisters tuples and assign it to siblings
siblings = tuple_sisters + tuple_brothers
print('my brother and sisters are:\t', siblings)

#4. How many siblings do you have?
print('the number of my siblings is:\t', len(siblings)) #6

#5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members

siblings_list = list(siblings)
siblings_list.extend(['Abdulyaqeen', 'Nihmah'])
family_members = tuple(siblings_list)
print('my family member her:\t', family_members)


# Exercises: Level 2
#1. Unpack siblings and parents from family_members
father, mother, *siblings = family_members
father = family_members[-2]
mother = family_members[-1]
print('The parents are:', father, 'and', mother)
print('The siblings are:', siblings)

#2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('oranges', 'banana', 'apple')
vegetables = ('lettuce', 'okra', 'tomatoes')
animal_product = ('meat', 'egg', 'honey')
food_stuff_tp = fruits + vegetables + animal_product
print('fruits, vegetables and animal product are:\t', food_stuff_tp)

#3.Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print('the list of food stuff tp are:\t', food_stuff_lt)

#4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
slice_middle = food_stuff_tp[4:5]
print('the middle items from the food_stuff_tp\t', slice_middle)

#5. Slice out the first three items and the last three items from food_staff_lt list
slice_three = food_stuff_lt[:2] + food_stuff_lt[-4:]
print('the first three and last three items are:\t', slice_three)

#6. Delete the food_staff_tp tuple completely
del food_stuff_tp

'''7. Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden').
#Check if 'Estonia' is a nordic country'''
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)#True

#Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)#False



# Create an empty tuple
empty_tuple = ()


# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Myrna', 'Gaby')
brothers = ('Victor', 'Emiliano')


# Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print(siblings)


# How many siblings do you have?
print(len(siblings))


# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings = list(siblings)
siblings.append('Tony')
siblings.append('Myrna')
family_members = siblings
# print(family_members)


# Unpack siblings and parents from family_members
new_siblings = family_members[:4]
parents = family_members[-2:]
print(new_siblings)
print(parents)


# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Jitomate', 'Mango')
vegetables = ('Jicama', 'Cebolla')
animal_products = ('Tocino', 'ChiCHarrón')


# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_tp = fruits + vegetables + animal_products


# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
food_stuff_tp_list = list(food_stuff_tp)
food_stuff_tp_list_2 = food_stuff_tp_list.copy()
print(len(food_stuff_tp_list))
food_stuff_tp_list = food_stuff_tp_list[:2] + food_stuff_tp_list[-2:]
print(food_stuff_tp_list)


# Slice out the first three items and the last three items from food_staff_lt list
food_stuff_tp_list_2 = food_stuff_tp_list_2[3:]
food_stuff_tp_list_2 = food_stuff_tp_list_2[3:]
print(food_stuff_tp_list_2)


# Delete the food_staff_tp tuple completely
del food_stuff_tp
print(food_stuff_tp)


# Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')


# Check if 'Estonia' is a nordic country
print('Estonia' in nordic_countries)


# Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)

# Exercises: Level 2
# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'kiwi')
vegetables = ('pickle', 'watermelon')
animal_products = ('meat', 'cheese')
food_stuff_tp = fruits + vegetables + animal_products


# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)


# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_items = len(food_stuff_lt) // 2
del food_stuff_lt[middle_items]
del food_stuff_lt[middle_items - 1]
print(food_stuff_lt)


# Slice out the first three items and the last three items from food_stuff_lt list
first_half = food_stuff_lt[:3]
second_half = food_stuff_lt[-3:]
print(first_half)
print(second_half)
food_stuff_tp = tuple(food_stuff_lt)


# # Delete the food_stuff_tp tuple completely
del food_stuff_tp
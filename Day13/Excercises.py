# 💻 Exercises: Day 13
# Filter only negative and zero in the list using list comprehension
import string
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [number for number in numbers if number <= 0]
print(negative_and_zero)



# Flatten the following list of lists of lists to a one dimensional list :
# output
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

one_dimensional_list = [digit for row in list_of_lists for digit in row]
print(one_dimensional_list)


# Using list comprehension create the following list of tuples:
# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]


# result = [tuple([n] + [n**exp for exp in range(7)]) for n in range(11)]
# print(result)



# Flatten the following list to a new list:
# output:
    # [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

output = [
    [name.upper(), name[:3].upper(), capital.upper()]
    for sublist in countries
    for name, capital in sublist
]

print(output)


# Change the following list to a list of dictionaries:
# output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]

output2 = [
    {'country' : name, 'city' : capital} 
    for sublist in countries 
    for name, capital in sublist
]

print(output2)




# Change the following list of lists to a list of concatenated strings:
# output
    # ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

names_list = [
    name + ' ' + l_name
    for sublist in names
    for name, l_name in sublist
]


print(names_list)
# Exercises: Level 1
import math
from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Use map to create a new list by changing each country to uppercase in the countries list
map_countries = list(map(lambda x: x.upper(), countries))
print(map_countries)


# Use map to create a new list by changing each number to its square in the numbers list
map_numbers = list(map(lambda x: math.pow(x,2), numbers ))
print(map_numbers)


# Use map to change each name to uppercase in the names list
def names_upper(name):
    return name.upper()
    
map_names = list(map(names_upper, names))
print(map_names)


# Use filter to filter out countries containing 'land'.
def countries_land(country):
    if 'land' in country:
        return True
    return False

filter_countries_land = list(filter(countries_land, countries))
print(filter_countries_land)


# Use filter to filter out countries having exactly six characters.
def countries_6(country):
    if len(country) == 6:
        return True
    return False

filter_countries_6 = list(filter(countries_6, countries))
print(filter_countries_6)


# Use filter to filter out countries containing six letters and more in the country list.
def countries_6_more(country):
    if len(country) >= 6:
        return True
    return False

filter_countries_6_more = list(filter(countries_6_more, countries))
print(filter_countries_6_more)


# Use filter to filter out countries starting with an 'E'
def countries_E(country):
    if country[0] == 'E':
        return True
    return False

filter_countries_E = list(filter(countries_E, countries))
print(filter_countries_E)


# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
resultado = reduce(lambda x,y: x + y,
                   filter(lambda x: x % 2 == 0,
                          map(lambda x: x**2, numbers )))

print(resultado)



# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))

list1 = ['hola', 1, 'dos']
print(get_string_lists(list1))


# Use reduce to sum all the numbers in the numbers list.
sum_all_numbers = reduce(lambda x,y: x + y, numbers)
print(sum_all_numbers)


# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
sentence = reduce(lambda x, y: x + ', '+ y, countries[:-1])
sentence = f', and {countries[-1]} are North European Countries.'
print(sentence)


# Exercises: Level 2
# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. 
# Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

import random

def list_of_hexa_colors(number):
    characters = '0123456789abcdef'
    return ['#' + ''.join(random.choices(characters, k=6)) for _ in range(number)]

print(list_of_hexa_colors(3))


# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors():
    characters = '0123456789abcdef'
    return ['#' + ''.join(random.choices(characters, k=6)) for _ in range(random.randint(1,4))]

print(list_of_rgb_colors())




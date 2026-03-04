# Exercises: Level 1
# Write a function which generates a six digit/character random_user_id.
#   print(random_user_id()) 
#   '1ee33d'

import random
import string


def random_user_id():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=6))

print(random_user_id()) 

# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
    # print(user_id_gen_by_user()) # user input: 5 5
    # #output:
    # #kcsy2
    # #SMFYb
    # #bWmeq
    # #ZXOYh
    # #2Rgxf
    
    # print(user_id_gen_by_user()) # 16 5
    # #1GCSgPLMaBAVQZ26
    # #YD7eFwNQKNs7qXaT
    # #ycArC5yrRupyG00S
    # #UbGxOFI7UXSWAyKN
    # #dIV0SSUTgAdKwStr


    
def user_id_gen_by_user():
    number_of_characters = input('Number of characters: ')
    number_of_IDs = input('Number of IDs: ')

    if not number_of_characters.isdigit() or not number_of_IDs.isdigit():
        return 'Los datos deben ser números enteros positivos.'

    number_of_characters = int(number_of_characters)
    number_of_IDs = int(number_of_IDs)
    characters = string.ascii_letters + string.digits

    for i in range(number_of_IDs):
       return ''.join(random.choices(characters, k=number_of_characters))

print(user_id_gen_by_user())


# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
# print(rgb_color_gen())
# # rgb(125,244,255) - the output should be in this form

def rgb_color_gen():
    f_value = random.randint(0,255)
    s_value = random.randint(0,255)
    t_value = random.randint(0,255)
    return 'rgb({},{},{})'.format(f_value, s_value, t_value)

print(rgb_color_gen())
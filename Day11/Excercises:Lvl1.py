# Exercises: Level 1
# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
import math
def add_two_numbers(num1, num2):
    res = num1 + num2
    return res

print(add_two_numbers(1,2))


# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def circle_area(pi, r):
    res = pi * math.pow(r, 2)
    return res

print(circle_area(math.pi, 3))



# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. 
# If not do give a reasonable feedback.
def add_all_nums(*nums):
    res = 0
    for i in nums:
        if not isinstance(i, (int)):
            return('No son todos numeros')
        else:
            res += i
    return res
        
print(add_all_nums(1,2,2, 'hola'))


# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(C):
    F = C * 9/5 + 32
    return F

print(convert_celsius_to_fahrenheit(20))


# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
spring = ['march', 'april', 'may']
summer = ['june', 'july', 'august']
autumn = ['september', 'october', 'november']
winter = ['december', 'january', 'february']

def check_season(month):
    month = month.lower()
    if month in spring:
        return('Spring')
    elif month in summer:
        return("Summer")
    elif month in autumn:
        return("Autumn")
    elif month in winter:
        return("Winter")
    else:        
        return('No es un mes valido')

print(check_season('March'))


# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    if not isinstance(lst, list):
        return('No es una lista')
    else:
        for i in lst:
            print(i)

print_list([1, 2, 3, 4, 5])



# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]
# print(reverse_list(["A", "B", "C"])) 
# # ["C", "B", "A"]
def reverse_list(lst2):
    if not isinstance(lst2, list):
        return ("No es una lista")
    else:
        return(lst2[::-1])

print(reverse_list([1,2,3]))



# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lst3):
    lst3_capitalize = []
    if not isinstance(lst3, list):
       return ("No es una lista")
    else:
        for i in lst3:
            i = i.capitalize()
            lst3_capitalize.append(i)
        return(lst3_capitalize)

print(capitalize_list_items(['hola', 'mundo']))



# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
# food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
# numbers = [2, 3, 7, 9];
# print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]
def add_item(lst4, item):
    if not isinstance(lst4, list):
       return ("No es una lista")
    else:
        lst4.append(item)
        return(lst4)

print(add_item(['myrna', 'Maldonado'], 'badillo'))



# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
# food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
# print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# numbers = [2, 3, 7, 9]
# print(remove_item(numbers, 3))  # [2, 7, 9]
def remove_item(lst5, rmv_item):
    if not isinstance(lst5, list):
       return ("No es una lista")
    elif rmv_item not in lst5:
        return("Item no encontrado")
    else:
        lst5.remove(rmv_item)
        return lst5

print(remove_item(['mango', 'mora'], 'morat'))



# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
# print(sum_of_numbers(5))  # 15
# print(sum_of_numbers(10)) # 55
# print(sum_of_numbers(100)) # 5050
def sum_of_numbers(number):
    res = 0
    if not isinstance(number, int):
       return ("No es un numero")
    else:
        for i in range(number + 1):
            res += i
        return(res)

print(sum_of_numbers(100))



# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(number):
    sum_odds = 0
    if not isinstance(number, int):
       return ("No es un numero")
    else:
        for i in range(number):
            if i % 2 != 0:
                sum_odds += i
        return("Sum odds: {}".format(sum_odds))

print(sum_of_odds(6))


# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(number):
    sum_even = 0
    if not isinstance(number, int):
       return ("No es un numero")
    else:
        for i in range(number):
            if i % 2 == 0:
                sum_even += i
        return("Sum even: {}".format(sum_even))

print(sum_of_even(6))
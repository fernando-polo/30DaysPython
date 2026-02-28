# Exercises: Level 1
# Iterate 0 to 10 using for loop, do the same using while loop.
def for_zero_to_ten():
    for i in range(10):
        print(i)

def while_zero_to_ten():
    i = 0
    while i < 10:
        i += 1
        print(i)

for_zero_to_ten()
while_zero_to_ten()

# Iterate 10 to 0 using for loop, do the same using while loop.
def for_ten_to_zero():
    for i in range(10,0,-1):
        print(i)

def while_ten_to_zero():
    i = 11
    while i > 0:
        i -= 1
        print(i)

for_ten_to_zero()
while_ten_to_zero()



# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
#   #
#   ##
#   ###
#   ####
#   #####
#   ######
#   #######

def simple_triangle():
    for i in range(8):
        print(i * '*')

simple_triangle()




# Use nested loops to create the following:
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #

def simple_square():
    for row in range(9):
        for column in range(9):
            print('#', end=' ')
        print()


simple_square()


# Print the following pattern:
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100

def tablas():
    for number in range(11):
        res = number * number
        print("{} x {} = {}".format(number, number, res))

tablas()



# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

lst = ['Python', 'Numpy','Pandas','Django', 'Flask'] 
def print_lst():
    for i in lst:
        print(i)

print_lst()



# Use for loop to iterate from 0 to 100 and print only even numbers
def even_numbers():
    for i in range(100):
        if i % 2 == 0:
            print(i)
even_numbers()


# Use for loop to iterate from 0 to 100 and print only odd numbers
def odd_numbers():
    for i in range(100):
        if i % 2 != 0:
            print(i)
odd_numbers()
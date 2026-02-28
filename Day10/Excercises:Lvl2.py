# Exercises: Level 2
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.
def sum_all_numbers():
    sum_numbers = 0
    for i in range(101):
        sum_numbers += i
    print("Sum of all numbers: {}".format(sum_numbers))

sum_all_numbers()



# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# The sum of all evens is 2550. And the sum of all odds is 2500.
def sum():
    sum_evens = 0
    sum_odds = 0
    for i in range(101):
        if i % 2 == 0:
            sum_evens += i
        else:
            sum_odds += i
    print('Even total: {}'.format(sum_evens))
    print('Odds total: {}'.format(sum_odds))

sum()


# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
    # The sum of all numbers is 5050.  
sum = 0
for i in range(101):
    sum = i + sum
    i += 1
print(sum)
    

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
    # The sum of all evens is 2550. And the sum of all odds is 2500.
sum_evens = 0
sum_odds = 0

for i in range(101):
    if i % 2 == 0:
        sum_evens = sum_evens + i
    else:
        sum_odds = sum_odds + i
print(f'The sum of all evens is {sum_evens}. And the sum of all odds is {sum_odds}.')
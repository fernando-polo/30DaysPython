# Exercises: Level 1
# Get user input using input(“Enter your age: ”). 
# If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. 
# Output:
    # Enter your age: 30
    # You are old enough to learn to drive.
    # Output:
    # Enter your age: 15
    # You need 3 more years to learn to drive.

user_age = int(input("Enter your age: "))
if user_age >= 18:
    print("You´re old enough to drive")
else:
    user_years_left = 18 - user_age
    print("You're too young to drive. You have {} years left to be able to".format(user_years_left))



# Compare the values of my_age and your_age using if … else. Who is older (me or you)? 
# Use input(“Enter your age: ”) to get the age as input. 
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. 
# Output:
    # Enter your age: 30
    # You are 5 years older than me.

my_age = 23
your_age = int(input("Enter your age: "))

if your_age > my_age:
    diff_age = your_age - my_age
    print("You are {} years older than me.".format(diff_age))
elif your_age == my_age:
    print("We are the same age!")
else:
    diff_age = my_age - your_age
    print("Im {} years older than you lil bro.".format(diff_age))




# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, 
# else a is equal to b. 
# Output:
    # Enter number one: 4
    # Enter number two: 3
    # 4 is greater than 3
    
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
if a > b:
    print("{} is greater than {}".format(a, b))
elif a < b:
    print("{} is smaller than {}".format(a, b))
else:    
    print("{} is equal to {}".format(a, b)) 




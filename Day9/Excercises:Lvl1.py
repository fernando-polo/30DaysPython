# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years. 
age = int(input("Enter your age: "))

def allow_to_drive(age):
    if age >= 18:
        print("You are old enough to drive.")
    else:
        remaining_years = 18 - age
        print(f"You need {remaining_years} more years to drive.")

# allow_to_drive(age)


# Compare the values of my_age and your_age using if … else. 
# Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.
my_age = 22
your_age = int(input("Enter your age: "))

def comparing_ages(your_age):
    if your_age == my_age:
        print("¡We are the same age!")
    elif your_age > my_age:
        diff_years1 = your_age - my_age
        print(f"You are {diff_years1} older than me.")
    else:
        diff_years2 = my_age - your_age
        print(f"I'm {diff_years2} older than you.")     

# comparing_ages(your_age)


# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, 
# else a is equal to b. 
a = int(input("Enter the value of a variable named \'a\': "))
b = int(input("Enter the value of a variable named \'b\': "))

def comparing_variables(a, b):
    if a > b:
        return (f"{a} is greater than {b}.")
    elif b > a:
        return (f"{b} is greater than {a}.")
    else:
        return (f"{a} and {b} have the same value.")
    
result_Ex3 = comparing_variables(a, b)
print(result_Ex3)



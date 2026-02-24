# Excercises Level:1
import math
# Declare your age as integer variable
age = 23


# Declare your height as a float variable
height = 1.75


# Declare a variable that store a complex number
complex_num = 1j


# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
#     Enter base: 20
#     Enter height: 10
#     The area of the triangle is 100
t_base = int("Enter base of triangle: ")
t_height = int("Enter base of triangle: ")
area = 0.5 * t_base * t_height


# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
# Enter side a: 5
# Enter side b: 4
# Enter side c: 3
# The perimeter of the triangle is 12
a = int("Enter A: ")
b = int("Enter B: ")
c = int("Enter C: ")
t_perimeter = a + b + c


# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
r_length = int("Rectangle length: ")
r_width = int("Rectangle width: ")
r_area = r_length * r_width
r_perimeter = 2 * (r_length + r_width)


# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
r_circle = int("Radius circle: ")
area = math.pi * r_circle * r_circle
circumference = 2 * r_circle * math.pi


# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)



# Compare the slopes in tasks 8 and 9.



# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x = int("Enter x value: ")
x_value = math.pow(x,2) + 6*x + 9


# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len("python")!=len("dragon"))


# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')


# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon' in 'I hope this course is not full of jargon.')


# There is no 'on' in both dragon and python
print('on' not in 'python' and 'on' not in 'dragon')


# Find the length of the text python and convert the value to float and convert it to string
python_len = len("python")
f_python = float(python_len)
s_python = str(f_python)


# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
x = int(input("x value: "))
is_even = x % 2 == 0


# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7 // 3 == int(2.7))


# Check if type of '10' is equal to type of 10
print(type("10") == type(10))


# Check if int('9.8') is equal to 10
print(int("10") == 10)


# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
# Enter hours: 40
# Enter rate per hour: 28
# Your weekly earning is 1120
hours = int("Enter hours: ")
pay_per_hour = float("Enter pay per hour: ")
total = hours * pay_per_hour
print("Your weekly earning is: ",total)


# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
# Enter number of years you have lived: 100
# You have lived for 3153600000 seconds.
years = int("How old are you? ")
seconds_per_year = 31536000
print("You have lived: ",years*seconds_per_year, " seconds")


# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

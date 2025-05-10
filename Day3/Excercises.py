# Day 3: Excercises

# Declare your age as integer variable
age = 22
# Declare your height as a float variable
height = 1.75
# Declare a variable that store a complex number
complex_number = 3 + 4j


# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the base of the triangle: "))

area = 0.5 * base * height
print(f"The area of the triangle is: {area:.2f}")


# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = float(input("Entre side a: "))
b = float(input("Entre side b: "))
c = float(input("Entre side c: "))

perimeter = a + b + c
print(f"The perimeter of the triangle is: {perimeter:.2f}")


# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = float(input("Length: "))
width = float(input("Width: "))

rectangle_area = length * width
rectangle_perimeter = 2 * (length + width)

print(f"The area of the rectangle is {rectangle_area:.2f} and its perimeter is {rectangle_perimeter}")


# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
import math

r = float(input("Enter the radius: "))

area = math.pi * math.pow(r,2)
circumference = 2 * math.pi * r

print(f"The area of the circle is {area:.2f} and its circumference is {circumference:.2f}")


# Find the slope and Euclidean distance between point (2, 2) and point (6,10)
def calculate_slope(x1,y1,x2,y2):
    m = y2-y1/x2-x1
    d = math.sqrt( math.pow(x2-x1,2) + math.pow(y2-y1,2) )
    print(f"The slope is {m:.2f} and the Euclidean distance is {d:.2f}")

calculate_slope(2,2,6,10)


# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
def calculate_y(x):
    y = math.pow(x,2) + 6 * x + 9
    print(y)

calculate_y(-3)


# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
len_python = len("python")
len_dragon= len("dragon")

is_correct = len_python == len_dragon
print(not(is_correct))
print(len_dragon is len_python)


# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("on" in "dragon")
print("on" in "python")


# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon"
print("jargon" in sentence)


# There is no 'on' in both dragon and python
print("on" not in "dragon")
print("on" not in "python")


# Find the length of the text python and convert the value to float and convert it to string
word_len = len("python")
word_float = float(word_len)
word_str = str(word_float)
print(word_str)


# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
def is_even(x):
    if x % 2 == 0:
        print("Even")
    else:
        print("Odd")

is_even(5)


# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
value_int = int(2.7)
floor_div = 7 // 3

print(value_int == floor_div)


# Check if type of '10' is equal to type of 10
print(type('10') == type(10))


# Check if int('9.8') is equal to 10
print(int(9.8) == 10)


# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = float(input("Hours: "))
rate_per_hour = float(input("Rate per hour: "))

def per_hour(hours, rate_per_hour):
    paycheck= hours * rate_per_hour
    print(f"Your profits for today will be ${paycheck:.2f}")

per_hour(hours, rate_per_hour)


# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input("Enter how many year a person can live: "))
seconds_per_year = 31536000

def seconds(years):
    seconds_years = years * seconds_per_year
    print(f"That number of years is equivalent to this seconds: {seconds_years}")

seconds(years)


# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

for i in range(1, 6):
    print(f"{i:<6}  1  {i:<6}  {i**2:<6}  {i**3}")


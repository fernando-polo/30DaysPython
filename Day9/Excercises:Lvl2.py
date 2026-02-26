# Exercises: Level 2
# Write a code which gives grade to students according to theirs scores:
    # ```sh
    # 90-100, A
    # 80-89, B
    # 70-79, C
    # 60-69, D
    # 0-59, F
    # ```

score = int(input("Student's score: "))
if score >= 90:
    print("A")
elif score <=89 and score>=80:
    print("B")
elif score <=79 and score >= 70:
    print("C") 
elif score <=69 and score >= 60:
    print("D")
else:
    print("F")


# Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, the season is Autumn. 
# December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

Autumn = ['September', 'October', 'November']
Winter = ['December', 'January', 'February']
Spring = ['March', 'April', 'May']
Summer = ['June', 'July', 'August']

month = str(input("Enter the month: "))
month = month.capitalize()

if month in Autumn:
    print("The season is Autumn")
elif month in Winter:
    print("The season is Winter")
elif month in Spring:
    print("The season is Spring")
elif month in Summer:
    print("The season is Summer")
else:
    print("That is not a month")





# The following list contains some fruits:
    # fruits = ['banana', 'orange', 'mango', 'lemon']

# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
# If the fruit exists print('That fruit already exist in the list')


fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input("Enter the fruit of your choice: ")
fruit = fruit.lower()

if fruit in fruits:
    print(fruits)
else:
    fruits.append(fruit)
    print(fruits)

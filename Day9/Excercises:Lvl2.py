# Write a code which gives grade to students according to theirs scores:
    # 80-100, A
    # 70-89, B
    # 60-69, C
    # 50-59, D
    # 0-49, F
score = int(input("Enter your score: "))

def grades(score):
    if score >= 90 and score <=100:
        return ("Your score is an A")
    elif score >= 70 and score <=89:
        return ("Your score is an B")
    elif score >= 60 and score <=69:
        return ("Your score is an C")
    elif score >= 50 and score <=59:
        return ("Your score is an D")
    else:
        return("Your score is a F")
    
final_score = grades(score)
print(final_score)



# Check if the season is Autumn, Winter, Spring or Summer. 
    # If the user input is: September, October or November, the season is Autumn. 
    # December, January or February, the season is Winter. 
    # March, April or May, the season is Spring 
    # June, July or August, the season is Summer
Autumn = ['september', 'october', 'november']
Winter = ['december', 'january', 'february']
Spring = ['march', 'april', 'may']
Summer = ['june', 'july', 'august']

season_name = str(input("Enter the name of the month: ").lower().replace(" ",""))

def season(season_name):
    if season_name in Autumn:
        return ("The season is Autumn")
    elif season_name in Winter:
        return ("The season is Winter")
    elif season_name in Spring:
        return ("The season is Spring")
    else:
        return ("The season is Summer")

res_season_name = season(season_name)
print(res_season_name)


# The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']

# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
# If the fruit exists print('That fruit already exist in the list')

fruit = str(input("Enter the name of the fruit that you are searching for: "))

def search_for_fruit(fruit):
    if fruit in fruits:
        return (fruits)
    else:
        fruits.append(fruit)
        return (fruits)

res_search_for_fruit = search_for_fruit(fruit)
print(res_search_for_fruit)
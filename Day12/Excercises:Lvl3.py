# Exercises: Level 3
# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
import random, string


def shuffle_list(lst):
    if not lst or not isinstance(lst, list):
        return('No me pasaste una lista')
    else:
        random.shuffle(lst)
        return lst

print(shuffle_list(['hola', 1]))



# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

def seven_numbers():
    return random.sample(range(10), k=7)

print(seven_numbers())
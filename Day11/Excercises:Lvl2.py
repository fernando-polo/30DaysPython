# Exercises: Level 2
# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
#     print(evens_and_odds(100))
#     # The number of odds are 50.
#     # The number of evens are 51.
def evens_and_odds(num):
    num_odds = 0
    num_evens = 0

    if not isinstance(num, int):
        return("No es un número")
    elif num < 0:
        return("No es un número positivo")
    else:
        for i in range(num+1):
            if i % 2 != 0:
                num_odds = num_odds + 1
            else:
                num_evens = num_evens + 1
        return('Odds: {}, Evens: {}'.format(num_odds, num_evens))

print(evens_and_odds(100))



# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(num):
    res_num_fact = 1
    if not isinstance(num, int):
        return("No es un número")
    elif num < 0:
        return("Debe ser arriba de cero el número.")
    else:
        for i in range(1, num+1):
            res_num_fact *= i
        return('Num fact {}'.format(res_num_fact))

print(factorial(5))



# Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(empty):
    if not empty:
        return('no hay valor')
    else:
        return('si hay valor')
    
print(is_empty(""))


# Write a function called greet which takes a default argument, name. If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.
#     greet()
#     # "Hello, Guest!
#     greet("Alice")
#     # "Hello, Alice!"
def greet(name):

    if not name:
        return ('¡Hello, Guest!')
    elif not isinstance(name, str):
        return ('No es un nombre')
    else:
        return ('¡Hello, {}!'.format(name))

print(greet('her'))





# Exercises: Level 3
# Write a function called is_prime, which checks if a number is prime.
def is_prime(num):
    if not isinstance(num, int):
        return "{} no es un número".format(num)
    elif num <= 1:
        return {"{} no puede ser numero primo, ya que es negativo o es el número 1.".format(num)}
    else:
        for i in range(2, num):
            if num % i == 0:     
                return "{} no es primo".format(num)
        return "{} es primo".format(num)

print(is_prime(['hola']))
print(is_prime(-2))
print(is_prime(2))
print(is_prime(4))


# Write a functions which checks if all items are unique in the list.
def all_items_equal(lst):
    if not isinstance (lst, list):
        return 'No es una lista'
    elif not lst:
        return 'No existe la lista'
    elif not len(lst) >= 2:
        return 'La lista no es suficiente grande para verificar.'
    else:
        for i in range(len(lst)):
            for j in range(len(lst)):
                if i != j and lst[i] == lst[j]:
                    return 'La lista tiene elemento repetidos'
            return 'La lista NO tiene elementos únicos.'
            

            
        
print(all_items_equal(''))
print(all_items_equal('hola'))
print(all_items_equal(['hola', 'adiós']))
print(all_items_equal(['hola', 'adiós', 'hola']))

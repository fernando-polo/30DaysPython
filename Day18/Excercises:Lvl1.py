# Write a pattern which identifies if a string is a valid python variable

import re
import keyword

pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'

user_input = input("Ingresa el nombre de la variable: ")

if not re.match(pattern, user_input):
    print(f"'{user_input}' no es válido: solo letras, números y _, sin empezar con número.")
elif keyword.iskeyword(user_input):
    print(f"'{user_input}' es una palabra reservada de Python.")
else:
    print(f"'{user_input}' es un nombre de variable válido.")


# Clean the following text. After cleaning, count three most frequent words in the string.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. 
There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. 
;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

new_sentence = re.sub(r"[%@&#$;!?.,]", '', sentence)
print(new_sentence)



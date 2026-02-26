# Exercises: Level 3
# Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Fernando',
    'last_name': 'Gómez',
    'age': 250,
    'country': 'México',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
       }
    }


#Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    middle_value = len(person['skills']) // 2
    print(person['skills'][middle_value])
else:
    print("The person has no skills.")

#Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person and 'Python' in person['skills']:
    print('It has python')
else:
    print('It doesn\'t have python')
    

#If a person skills has only JavaScript and React, print('He is a front end developer'), 
# if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
if person.get('skills') and set(person['skills']) == {'JavaScript', 'React'}:
    print('FrontEnd developer')
elif person.get('skills') and set(person['skills']) == {'Node', 'Python', 'MongoDB'}:
    print('He is a backend developer')
elif person.get('skills') and set(person['skills']) == {'ReacT', 'Node', 'MongoDB'}:
    print('He is a fullstack developer')
else:
    print('unknown title')


#If the person is married and if he lives in Finland, print the information in the following format:
#     Asabeneh Yetayeh lives in Finland. He is married.
if person['is_married'] == True and person['country'] == 'México':
    print("{} {} lives in {}. He is married".format(person['first_name'], person['last_name'], person['country']))
else:
    print('I dont know what are you talking about.')

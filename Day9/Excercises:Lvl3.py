
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
                }
    }

#1 #  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
def skills_key():
    if "skills" in person:
        lst_skills = person['skills']
        middle_index = len(lst_skills) // 2
        return lst_skills[middle_index]
    else:
        return ("The key \'skills\' do not exist.")

print(skills_key())


#2 #  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.

def python_key():
    if "skills" in person:
        if "Python" in person['skills']:
            return person
        else:
            return ("It has no abilities with pyhton.")
    else:
        return ("The kew \'skills\' do not exist.")
    
print(python_key())


#3 #  * If a person skills has only JavaScript and React, print('He is a front end developer'), 
#       if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
#       if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
#       else print('unknown title') - for more accurate results more conditions can be nested!

def identificar_rol():
    skills = person.get('skills')

    skills_set = set(skills)

    if skills_set == {'JavaScript', 'React'}:
        return ('He is a front end developer')
    elif {'Node', 'Python', 'MongoDB'}.issubset(skills_set):
        return ('He is a backend developer')
    elif {'React', 'Node', 'MongoDB'}.issubset(skills_set):
        return ('He is a fullstack developer')
    else:
        return ('unknown title')

print(identificar_rol())



#4 #  * If the person is married and if he lives in Finland, print the information in the following format:
    # Asabeneh Yetayeh lives in Finland. He is married.

def details_person():
    if person.get('is_married') and person.get('country') == 'Finland':
        name = person.get('first_name')
        last_name = person.get('last_name')
        country = person.get('country')
        return (f'{name} {last_name} lives in {country}. He is married')
    else:
        return 'Information not available'

print(details_person())
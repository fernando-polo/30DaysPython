# Create an empty dictionary called dog
dog = {}


# Add name, color, breed, legs, age to the dog dictionary
dog= {'color':'blueASF',
      'breed':'blue\'s clues breed',
      'legs':'4',
      'age':'3',
      'name':'blue',
    }


# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {'first_name':'Fernando',
           'last_name':'Gómez Maldonado',
           'gender':'male',
           'age':'22',
           'marital status':'singleASF',
           'skills':['Cook so delicious', 'Play volleyball', 'Goes to the gym'],
           'country':'México',
           'city':'Querétaro',
           'address':'Shhh is top secret',
           }


# Get the length of the student dictionary
len_student = len(student)
print(len_student)


# Get the value of skills and check the data type, it should be a list
skills = student.get('skills')
print(type(skills))


# Modify the skills values by adding one or two skills
student['skills'].append('Saltar la cuerda')
print(skills)


# Get the dictionary keys as a list
list_of_keys = list(student.keys())
print(list_of_keys)


# Get the dictionary values as a list
list_of_values = list(student.values())
print(list_of_values)


# Change the dictionary to a list of tuples using items() method
list_of_tuples = student.items()
print(list_of_tuples)


# Delete one of the items in the dictionary
student.pop('first_name')
print(student)


# Delete one of the dictionaries
del dog


# Merge two python dictionaries to one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict1.update(dict2)
print(dict1)


# Print the value of key ‘history’ from the below dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(sampleDict['class']['student']['marks']['history'])


# Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

res = dict.fromkeys(employees,defaults)
print(res)



# Exercises
# Create an empty dictionary called dog
dog = {}


# Add name, color, breed, legs, age to the dog dictionary
dog = { 'name' : 'ela',
        'color' : 'white', 
        'breed' : 'husky', 
        'age' : 7}


# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name' : 'Fer',
    'last_name' : 'Gómez',
    'gender'  : 'Male',
    'age' : 25,
    'marital_status' : 'Single',
    'skills' : ['Python', 'JavaScript', 'HTML', 'CSS'],
    'country' : 'México',
    'city' : 'Querétaro',
    'address' : '123 Main St'
}


# Get the length of the student dictionary
print(len(student))


# Get the value of skills and check the data type, it should be a list
print(student.get('skills'))


# Modify the skills values by adding one or two skills
student['skills'].extend(['Ruby', 'Go'])
print(student['skills'][-2:])


# Get the dictionary keys as a list
keys = student.keys()


# Get the dictionary values as a list
values = student.values()


# Change the dictionary to a list of tuples using items() method
print(student.items())


# Delete one of the items in the dictionary
student.popitem()


# Delete one of the dictionaries
del dog
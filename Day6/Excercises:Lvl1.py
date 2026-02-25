# Exercises: Level 1
# Create an empty tuple
empty_tuple = ()


# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('Myrna', 'Gaby')
sisters = ('Fer', 'Victor')


# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters


# How many siblings do you have?
len(siblings)
print(siblings)

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings = list(siblings)
siblings.append(['Tony', 'Myrna2'])
family_members = tuple(siblings)
print(family_members)
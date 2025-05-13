# Create an empty tuple
empty_tuple = ()


# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Myrna', 'Gaby')
brothers = ('Victor', 'Emiliano')


# Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print(siblings)


# How many siblings do you have?
print(len(siblings))


# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings = list(siblings)
siblings.append('Tony')
siblings.append('Myrna')
family_members = siblings
print(family_members)


# Exercises: Level 2
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]



# Join A and B
A.update(B)


# Find A intersection B
A.intersection(B)


# Is A subset of B
A.issubset(B)


# Are A and B disjoint sets
A.isdisjoint(B)


# Join A with B and B with A
A.update(B)
B.update(A)


# What is the symmetric difference between A and B
print(A.symmetric_difference(B))


# Delete the sets completely
del A
del B
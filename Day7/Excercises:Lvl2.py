# Exercises: Level 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}


# Join A and B
A_B = A.union(B)


# Find A intersection B
print(A.intersection(B))


# Is A subset of B
print(A.issubset(B))


# Are A and B disjoint sets
print(A.isdisjoint(B))


# Join A with B and B with A
B_A = B.union(A)


# What is the symmetric difference between A and B
difference = A.symmetric_difference(B)
print(difference)


# Delete the sets completely
del A
del B

# # Exercises: Level 3
# age = [22, 19, 24, 25, 26, 24, 25, 24]


# # Convert the ages to a set and compare the length of the list and the set, which one is bigger?
# age_set = set(age)

# if len(age) > len(age_set):
#     print("Es más grande la lista")
# elif len(age) == len(age_set):
#     print("Son iguales")
# else:
#     print("Es más grande el set")

# print(len(age))
# print(len(age_set))


# Explain the difference between the following data types: string, list, tuple and set
    # String: is a datatype which is any text between two quotes
    # List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
    # Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
    # Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.


# How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people"
sentece_lst = sentence.split()
sentence_set = set(sentece_lst)
print(sentence_set)




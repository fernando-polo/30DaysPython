# Excercises3
age = [22, 19, 24, 25, 26, 24, 25, 24]


# Convert the ages to a set and compare the length of the list and the set, which one is bigger?


age_set = set(age)
print(age)
print(age_set)


#"I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence?"
    #Use the split methods and set to get the unique words

sentence = "I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence?"
sentence_lst = sentence.split(' ')
sentence_set = set(sentence_lst)
print(sentence_set)


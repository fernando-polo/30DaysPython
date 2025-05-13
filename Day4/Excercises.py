# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
var_str = ['Thirty', 'Days', 'Of', 'Python']
complete_str = ' '.join(var_str)
print(complete_str)


# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
var_str = ['Coding', 'For' , 'All']
complete_str = ' '.join(var_str)
print(complete_str)


# Declare a variable named company and assign it to an initial value "Coding For All".
# Print the variable company using print().
# Print the length of the company string using len() method and print().
# Change all the characters to uppercase letters using upper() method.
# Change all the characters to lowercase letters using lower() method.
company = "Coding For All"
print(company)
print(len(company))
# company = company.upper()
# company = company.lower()


# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
# company = company.capitalize()
# company = company.title()
# company = company.swapcase()


# Cut(slice) out the first word of Coding For All string.
# company = company[7:]
# print(company)


# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print("Coding" in company)


# Replace the word coding in the string 'Coding For All' to Python.
# Change Python for Everyone to Python for All using the replace method or other methods.
company = company.replace("Coding", "Python")
print(company)


# Split the string 'Coding For All' using space as the separator (split()) .
company = company.split(" ")
print(company)


# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(', '))


# What is the character at index 0 in the string Coding For All.
company2 = "Coding For All"
print(company2[0])


# What is the last index of the string Coding For All.
print(company2[-1])


# What character is at index 10 in "Coding For All" string.
print(company2[10])


# Create an acronym or an abbreviation for the name 'Coding For All'.
print(company2[::7])


# Use index to determine the position of the first occurrence of C in Coding For All.
print(company2.find('C'))


# Use index to determine the position of the first occurrence of F in Coding For All.
print(company2.find('F'))


# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company2.rfind('l'))


# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))
print(sentence.rindex('because'))


# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence1 = sentence[:31]
sentence2 = sentence[55:]

new_sentence = sentence1 + sentence2
print(new_sentence)


# Does ''Coding For All' start with a substring Coding?
print(company2.startswith("Coding"))


# Does 'Coding For All' end with a substring coding?
print(company2.endswith("Coding"))


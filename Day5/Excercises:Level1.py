# Exercises: Level 1
# Declare an empty list
empty_list = []


# Declare a list with more than 5 items
normal_list = [1,2,3,4,5]


# Find the length of your list
print(len(normal_list))


# Get the first item, the middle item and the last item of the list
print(normal_list[::2])


# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Fer', 23, 1.75, 'Singles', 'Areca']


# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']


# Print the list using print()
print(it_companies)


# Print the number of companies in the list
print(len(it_companies))


# Print the first, middle and last company
print(it_companies[0])
print(it_companies[-1])
middle_index = len(it_companies) // 2
print(it_companies[middle_index])


# Print the list after modifying one of the companies
it_companies[0] = 'Ubuntu'
print(it_companies)


# Add an IT company to it_companies
it_companies.append('HelloWorld!')


# Insert an IT company in the middle of the companies list
it_companies.insert(middle_index, 'NOTApple')
print(it_companies)


# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()
print(it_companies)


# Join the it_companies with a string '#;  '
# it_companies = '# '.join(it_companies)
# print(it_companies)


# Check if a certain company exists in the it_companies list.
print('Microsoft' in it_companies)


# Sort the list using sort() method
it_companies.sort()
print(it_companies)


# Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)


# Slice out the first 3 companies from the list
S01 = it_companies[0:3]
print(S01)


# Slice out the last 3 companies from the list
S02 = it_companies[-3:]
print(S02)


# Slice out the middle IT company or companies from the list
middles_index = len(it_companies) // 2
S03 = it_companies[middles_index]
print(S03)


# Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)


# Remove the middle IT company or companies from the list
middles_index2 = len(it_companies) // 2
del it_companies[middles_index2]
del it_companies[middles_index2 - 1]
print(it_companies)


# Remove the last IT company from the list
it_companies.pop()
print(it_companies)


# Remove all IT companies from the list
it_companies.clear()
print(it_companies)


# Destroy the IT companies list
# del it_companies
# print(it_companies)


# Join the following lists:
    # front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    # back_end = ['Node','Express', 'MongoDB']
# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

firstList = front_end + back_end
full_stack = firstList.copy()
print(full_stack)
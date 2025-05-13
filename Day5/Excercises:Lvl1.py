# Declare an empty list
emp_list = []


# Declare a list with more than 5 items
five_items = ["Horno", "Refri", "Licuadora", "Microondas", "Freidora"]


# Find the length of your list
print(len(five_items))


# Get the first item, the middle item and the last item of the list
print(five_items[0], five_items[2], five_items[-1])


# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Fernando", 22, 1.75, "Soltero", "Areca"]


# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]


# Print the list using print()
print(it_companies)


# Print the number of companies in the list
print(len(it_companies))


# Print the first, middle and last company
print(it_companies[0], it_companies[3], it_companies[-1])


# Print the list after modifying one of the companies
it_companies[0] = "Netfilx"
print(it_companies)


# Add an IT company to it_companies
it_companies.append("Samsung")



# Insert an IT company in the middle of the companies list
it_companies.insert(4, "ClickUp")
print(it_companies)


# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()
print(it_companies)


# Join the it_companies with a string '#;  '
it_companies2 = it_companies.copy()
it_companies2 = '#; '.join(it_companies2)
print(it_companies2)
print(it_companies)


# Check if a certain company exists in the it_companies list.
print("TCS" in it_companies)


# Sort the list using sort() method
it_companies.sort()
print(it_companies)


# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)


# Slice out the first 3 companies from the list
print(it_companies[3:])


# Slice out the last 3 companies from the list
print(it_companies[-9:-3])


# Slice out the middle IT company or companies from the list
first_part = it_companies[:4]
second_part = it_companies[5:]
utlimate_part = first_part + second_part
print(utlimate_part)


# Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)


# Remove the middle IT company or companies from the list
del it_companies[3:5]
print(it_companies)


# Remove the last IT company from the list
it_companies.pop(-1)
print(it_companies)


# Remove all IT companies from the list
it_companies.clear()
print(it_companies)



# Destroy the IT companies list
del it_companies



# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack1 = front_end + back_end
print(full_stack1)


# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux
full_stack = full_stack1.copy()
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)

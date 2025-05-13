# Exercises: Level 1
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]



# Find the length of the set it_companies
print(len(it_companies))


# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)



# Insert multiple IT companies at once to the set it_companies
it_companies.update(["Samsung", "Huawei"])
print(it_companies)


# Remove one of the companies from the set it_companies
it_companies.remove("Huawei")
print(it_companies)



# The difference between remove and discard is:
# - remove() will raise a KeyError if the element is not found in the set.
# - discard() will not raise an error if the element is not found; it does nothing.



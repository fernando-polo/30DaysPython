# Write a function which count number of lines and number of words in a text. All the files are in the data the folder:

# Read obama_speech.txt file and count number of lines and words
with open('obama_speech.txt') as f:
    content = f.readlines()

num_lines = len(content)
num_words = sum(len(line.split()) for line in content)

print(f"Número de líneas: {num_lines}")
print(f"Número de palabras: {num_words}")


# Read michelle_obama_speech.txt file and count number of lines and words
with open('michelle_obama_speech.txt') as f:
    content = f.readlines()

num_lines = len(content)
num_words = sum(len(line.split()) for line in content)

print(f"Número de líneas: {num_lines}")
print(f"Número de palabras: {num_words}")


# Read donald_speech.txt file and count number of lines and words
with open('donald_speech.txt') as f:
    content = f.readlines()

num_lines = len(content)
num_words = sum(len(line.split()) for line in content)

print(f"Número de líneas: {num_lines}")
print(f"Número de palabras: {num_words}")


# Read melina_trump_speech.txt file and count number of lines and words
with open('melina_trump_speech.txt') as f:
    content = f.readlines()

num_lines = len(content)
num_words = sum(len(line.split()) for line in content)

print(f"Número de líneas: {num_lines}")
print(f"Número de palabras: {num_words}")





# Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages

import json
from collections import Counter

def most_spoken_languages(filename, k):
    with open(filename) as f:
        countries = json.load(f)
    
    languages = []
    for country in countries:
        languages.extend(country.get('languages', []))
    
    return [(count, lang) for lang, count in Counter(languages).most_common(k)]

print(most_spoken_languages('./countries_data.json', 10))
print(most_spoken_languages('./countries_data.json', 3))


# Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

import json

def most_populated_countries(filename, k):
    with open(filename) as f:
        countries = json.load(f)
    
    country_list = []
    for country in countries:
        country_list.append((country['population'], country['name']))
    
    country_list.sort(reverse=True)  
    
    return country_list[:k]  
print(most_populated_countries('./countries_data.json', 10))

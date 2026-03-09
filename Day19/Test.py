import json


with open('archivo_prueba.txt') as file:
    print(file.read(2))


person = {
    "name": "Fer",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}


with open('./json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)
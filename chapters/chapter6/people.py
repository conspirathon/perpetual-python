# 6-7. People:
person_0 = {
    "first_name": "katie",
    "last_name": "kutie",
    "age": 36,
    "city": "new york city",
}

person_1 = {
    "first_name": "mylo",
    "last_name": "foodie",
    "age": 7,
    "city": "brooklyn",
}

person_2 = {
    "first_name": "nigel",        
    "last_name": "schmoolington",
    "age": 7,
    "city": "cardiff",
}

people = [
    person_0,
    person_1,
    person_2,
]

labels = {
    "first_name": "First Name",
    "last_name": "Last Name",
    "age": "Age",
    "city": "City",
}

for person in people:
    for key, label in labels.items():
        value = person.get(key, "N/A")
        if isinstance(value, str):
            print(f"{label}: {value.title()}")
        else:
            print(f"{label}: {value}")
    print()
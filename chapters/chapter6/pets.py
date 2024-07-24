# 6-8. Pets:
pets = [
    {
        "name": "nigel",
        "species": "cat",
        "human": "ryan",
    },
    {
        "name": "mylo",
        "species": "rabbit",
        "human": "ryan",
    },
    {
        "name": "patti",
        "species": "cat",
        "human": "katie",
    },
    {
        "name": "moe",
        "species": "rabbit",
        "human": "katie",
    },
    {
        "name": "mario",
        "species": "rabbit",
        "human": "katie",
    },
]

labels = {
    "name": "Name",
    "species": "Species",
    "human": "Human",
}

for pet in pets:
    for key, label in labels.items():
        value = pet.get(key, "N/A")
        if isinstance(value, str):
            print(f"{label}: {value.title()}")
        else:
            print(f"{label}: {value}")
    print()
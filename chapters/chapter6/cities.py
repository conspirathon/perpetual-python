# 6-11. Cities:
cities = {
    "new york city": {
        "country": "u.s.a.",
        "population": 7_931_147,
        "fact": "largest city in the u.s.",
    },
    "los angels": {
        "country": "u.s.a.",
        "population": 3_795_936,
        "fact": "largest city on the westcoast",
    },
    "chicago": {
        "country": "u.s.a.",
        "population": 2_695_598,
        "fact": "largest city in midwest",
    },
}

for city, info in cities.items():
    print(f"City: {city.title()}")
    for key, value in info.items():
        if isinstance(value, str):
            print(f" {key.title()}: {value.title()}")
        else:
            print(f" {key.title()}: {value:,}")
    print()
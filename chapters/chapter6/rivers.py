# 6-5. Rivers:
dict_rivers = {}
dict_rivers["the amazon"] = ["brazil", "peru", "columbia"]
dict_rivers["the ganges"] = ["india", "bangladesh"]
dict_rivers["the danube"] = [
    "germany",
    "austria",
    "romania",
    "hungary",
    "serbia",
    "bulgaria",
    "ukraine",
    "slovakia",
    "croatia",
]

# Use a loop to print a sentence...
for river, countries in dict_rivers.items():
    countries_str = ", ".join([country.title() for country in countries])
    print(f"\n{river.title()} river runs through {countries_str}.")

"""I wanted to play with values as another type(?) in dictionary's, so I choose
rivers with multiple countries. After I wrote my code, I thought: 'and would
be great before the last country'. Right now, I know just enough about slicing
lists. So I turned to gpt-4 for a little guidence. For total transparency the
code below is not mine."""

# for river, countries in dict_rivers.items():
#     countries_list = [country.title() for country in countries]
#     if len(countries_list) > 1:
#         # Adding "and" before the last country
#         countries_str = ", ".join(countries_list[:-1]) + ", and " + countries_list[-1]
#     else:
#         # Only one country, no need to add "and"
#         countries_str = countries_list[0]
#     print(f"\n{river.title()} river runs through {countries_str}")

# # Use a loop to print the name of each river...
# for key in dict_rivers:
#     print(key.title())

# # Use a loop to print the name of each country...
# for river, countries in dict_rivers.items():
#     countries_str = ", ".join([country.title() for country in countries])
#     print(countries_str)
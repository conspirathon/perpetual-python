# 6-3. Glossary:
dict_glossary = {}

dict_glossary["variables"] = "Containers for storing data values."
dict_glossary["strings"] = "Sequences of characters enclosed in quotes."
dict_glossary["lists"] = "Ordered collections of items, defined by '[]'."
dict_glossary["loops"] = "Structures that repeat a block of code multiple times."
dict_glossary["functions"] = "Blocks of code designed to preform a specific task."

for key, value in dict_glossary.items():
    print(f"\n{key.title()}:\n\t{value}")
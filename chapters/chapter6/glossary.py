# 6-3. Glossary:
dict_glossary = {}

dict_glossary["variables"] = "Containers for storing data values."
dict_glossary["strings"] = "Sequences of characters enclosed in quotes."
dict_glossary["lists"] = "Ordered collections of items, defined by '[]'."
dict_glossary["loops"] = "Structures that repeat a block of code multiple times."
dict_glossary["functions"] = "Blocks of code designed to preform a specific task."

# 6-4. Glossary 2:
dict_glossary["int"] = "Integer number."
dict_glossary["boolean"] = "True or False value."
dict_glossary["set"] = "Unordered collection of unique items."
dict_glossary["dict"] = "Key-value pairs collection."
dict_glossary["tuple"] = "Immutable ordered sequence."

for key, value in dict_glossary.items():
    print(f"\n{key.title()}:\n\t{value}")
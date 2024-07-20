# A Dictionary of Similar Objects

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

# language = favorite_languages["sarah"].title()
# print(f"Sarah's favorite language is {language}.")

# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")

# Default dictionary looping behavior:
# for name in favorite_languages:
#     print(name)

# Looping Through All the Keys in a Dictionary

# for name in favorite_languages.keys():
#     print(name.title())

# friends = ["phil", "sarah"]
# for name in favorite_languages.keys():
#     print(f"Hi {name.title()}.")

#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")

# if "erin" not in favorite_languages.keys():
#     print("\nErin, please take our poll!")

# Looping Through a Dictionary's Keys in a Particular Order

# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")

# Looping Through All Values in a Dictionary

print("The following languages have been mentioned:")
# for language in favorite_languages.values():
#     print(language.title())

"""In a "poll" w/ a large number of respondents, it would be very repetitive.
To see each language w/o repetition, we can use a set."""
# A set is a collection in which each item must be unique:
for language in set(favorite_languages.values()):
    print(language.title())

"""When you wrap set() around a collection of values that contains
duplicate items, Python identifies the unique items in the
collection and builds a set from those items. Here we use set() to pull
out the unique languages in favorite_languages.values().
    The result is a nonrepetitive list of languages that have been
mentioned by people taking the poll:

    As you continue learning about Python, you'll often find a built-
in feature of the language that helps you do exactly what you want
with your data.
*NOTE*
You can build a set directly using braces and separating the
elements with commas:
>>> language = {"python", "rust", "python", "c"}
>>> languages
{"rust", "python", "c"}"""
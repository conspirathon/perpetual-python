# 6-6. Polling:
favorite_languages_dict = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

polling_lst = [
    "katie",
    "mario",
    "sarah",
    "mylo",
    "miriam",
    "jen",
    "phil",
]

friends = ["phil", "sarah"]

for name in sorted(favorite_languages_dict.keys()):
    print(f"\n{name.title()}, thank you for taking the poll.")
    if name in friends:
        language = favorite_languages_dict[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
for name in polling_lst:
    if name not in favorite_languages_dict.keys():
        print(f"""\n{name}, please take our poll!
        We'd love to know your favorite language.""")
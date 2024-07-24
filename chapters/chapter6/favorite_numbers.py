# 6-2. Favorite Numbers:
# favorite_numbers = {}

# favorite_numbers["katie"] = 23
# favorite_numbers["mylo"] = 7
# favorite_numbers["mario"] = 33
# favorite_numbers["moe"] = 42
# favorite_numbers["nigel"] = 9

# print(f"\nKatie's favorite number is {favorite_numbers["katie"]}.")
# print(f"\nMylo's favorite number is {favorite_numbers["mylo"]}.")
# print(f"\nMario's favorite number is {favorite_numbers["mario"]}.")
# print(f"\nMoe's favorite number is {favorite_numbers["moe"]}.")
# print(f"\nNigel's favorite number is {favorite_numbers["nigel"]}.")

# for key, value in favorite_numbers.items():
#     print(f"\n{key.title()}'s favorite number is {value}.")

# 6-10. Favorite Numbers (modified):
favorite_numbers = {
    "katie": (23, 8, 12),
    "mylo": (7, 42, 9),
    "mario": (33, 1, 17),
    "moe": (42, 19, 3),
    "nigel": (9, 6, 3),
}
for name, numbers in favorite_numbers.items():
    # print(f"{name.title()}'s favorite numbers are:")
    # for number in numbers:
    #     print(f"{number}")
    # print()
    numbers_str = ", ".join(str(number) for number in numbers)
    print(f"{name.title()}'s favorite numbers are: {numbers_str}\n")
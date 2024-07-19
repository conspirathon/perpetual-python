# 5-8. Hello Admin:
# user_names = [
#     "mylo the clever",
#     "sir schmoo",
#     "patty mayonnaise",
#     "pearl the acrobat",
#     "admin",
# ]

# for name in user_names:
#     if name == "admin":
#         print("\nHello Admin, would you like to see a status report?")
#     else:
#         print(f"\nHello {name.title()}, please enter your password")

# 5-9. No Users:
# user_names = []

# if user_names:
#     for name in user_names:
#         if name == "admin":
#             print("\nHello Admin, would you like to see a status report?")
#         else:
#             print(f"\nHello {name.title()}, please enter your password.")
# else:
#     print("We need to find some users!")

# 5-10. Checking Usernames:
# current_users = [
#     "mylo the clever",
#     "SIR schmoo",
#     "patty mayonnaise",
#     "PEARL the acrobat",
#     "moe the pony",
# ]

# new_users = [
#     "mj the anxious",
#     "muffin",
#     "super mario",
#     "miriam the destroyer",
#     "sir schmoo",
# ]

# current_users_lower = [user.lower() for user in current_users]

# for user in new_users:
#     if user.lower() in current_users_lower:
#         print(f"\nUsername '{user}' taken, please enter another name.")
#     else:
#         print(f"\nUsername '{user}' is available.")

# 5-11. Ordinal Numbers:
ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,]

for num in ordinal_numbers:
    if num == 1:
        print(f"\n{num}st")
    elif num == 2:
        print(f"\n{num}nd")
    elif num == 3:
        print(f"\n{num}rd")
    else:
        print(f"\n{num}th")
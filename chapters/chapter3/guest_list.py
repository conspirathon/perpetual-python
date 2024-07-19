lst_invites = ["john carmack", "richard stallman", "guido van rossum"]
print("Invitations sent")
print(f"Please except this dinner invitation {lst_invites[0].title()}")
print(f"Please except this dinner invitation {lst_invites[1].title()}")
print(f"Please except this dinner invitation {lst_invites[2].title()}")
print(f"{lst_invites[0]} can't make the dinner party")
lst_invites[0] = "dennis ritchie"
# new invitations
print("Second set of invitations")
print(f"Please except this dinner invitation {lst_invites[0].title()}")
print(f"Please except this dinner invitation {lst_invites[1].title()}")
print(f"Please except this dinner invitation {lst_invites[2].title()}")
print("We recieved a larger table for our party, get ready for more guests.")
lst_invites.insert(0, "yukihiro matsumoto")
lst_invites.insert(2, "bjarne stroustrup")
lst_invites.append("linus torvol")
# new invitations
print("Third set of invitations")
print(f"Please except this dinner invitation {lst_invites[0].title()}")
print(f"Please except this dinner invitation {lst_invites[1].title()}")
print(f"Please except this dinner invitation {lst_invites[2].title()}")
print(f"Please except this dinner invitation {lst_invites[3].title()}")
print(f"Please except this dinner invitation {lst_invites[4].title()}")
print(f"Please except this dinner invitation {lst_invites[5].title()}")
print("Turns out the dinner table was smaller, not larger and I'm only available to invite two guests.")
uninvite1 = lst_invites.pop()
print(f"Sorry you couldn't attend {uninvite1.title()}")
uninvite2 = lst_invites.pop()
print(f"Sorry you couldn't attend {uninvite2.title()}")
uninvite3 = lst_invites.pop()
print(f"Sorry you couldn't attend {uninvite3.title()}")
uninvite4 = lst_invites.pop()
print(f"Sorry you couldn't attend {uninvite4.title()}")
# new invitations
print(f"Please except this dinner invitation {lst_invites[0].title()}")
print(f"Please except this dinner invitation {lst_invites[1].title()}")
del lst_invites[1]
del lst_invites[0]
print(lst_invites)



# old code
# lst_invites = ["john carmack", "richard stallman", "guido van rossum"]

# def invitation(lst_invites):
#     lst_invites[0] = "nikola telsa" #john carmack canceled
#     # got a larger table to invite more guests
#     lst_invites.append("linus torvol")
#     lst_invites.append("yukihiro matsumoto")
#     lst_invites.append("dennis ritchie")
#     for each in lst_invites:
#         message = f"Please except this dinner request {each.title()} and join me on the 15th August, 2024"
#         print(message)

# invitation(lst_invites)

# refactored
# lst_invites = ["john carmack", "richard stallman", "guido van rossum"]

# def invitation(lst_invites):
#     # john carmack cancled and adding new guests
#     lst_invites[0] = "bjarne stroustrup"
#     new_invites = ["linus torvol", "yukihiro matsumoto", "dennis ritchie"]
#     lst_invites.extend(new_invites)

#     messages = [
#         f"Please except this dinner request {each.title()}"
#         for each in lst_invites
#     ]

#     for message in messages:
#         print(message)

# invitation(lst_invites)
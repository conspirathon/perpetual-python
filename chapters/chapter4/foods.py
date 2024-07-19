my_foods = ["pizza", "falafel", "carrot cake"]
# friends_foods = my_foods[:]
# my_foods.append("cannoli")
# friends_foods.append("ice cream")

# print("My favorite foods are:")
# # print(my_foods)
# for food in my_foods:
#     print(food)
# print("\nMy friend's favorite foods are:")
# # print(friends_foods)
# for food in friends_foods:
#     print(food)


# my_foods = ["pizza", "falafel", "carrot cake"]
# my_foods.append("burritos")
# my_foods.append("tortas")
# my_foods[2] = "quesadillas"
# my_foods.insert(0, "french fries")
# my_foods.append("sushi")
# my_foods.append("baked salmon")
# my_foods.append("tamago kake gohan")
# print("Full list:")
# print(my_foods)
# print("\nThe first three items in the list are:")
# print(my_foods[:3])
# print("\nThree items from the middle of the list are:")
# print(my_foods[3:6])
# print("\nThe last three items in the list are:")
# print(my_foods[6:])
my_foods[2] = "french fries"
friend_foods = my_foods[:]
new_foods = ["burrito", "torta", "quesadilla", "sushi", "baked salmon", "tamago kake gohan"]
fnew_foods = ["pancake", "waffles", "bacon and eggs",]
my_foods.extend(new_foods)
friend_foods.extend(fnew_foods)
print("\nMy favorite foods are:")
for food in my_foods:
    print(food)
print("\nMy friends favorite foods are:")
for food in friend_foods:
    print(food)

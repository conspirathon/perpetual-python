# 4-1 Pizzas: Think of at least three kinds of your favorite pizza.
# Store these pizza names in a list, and then use a for loop to print the name of each pizza.
lst_favorite_pizzas = [
    "cheese",
    "pepperoni",
    "thin crust"
]

friend_pizzas = lst_favorite_pizzas[:]
# print(friend_pizzas)
lst_favorite_pizzas.append("sausage")
friend_pizzas.append("hawaiian")
print("\nMy favorite pizzas are:")
for pizza in lst_favorite_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

# for pizza in lst_favorite_pizzas:
#     print(f"I like {pizza.title()} pizza")
# print(f"\n{lst_favorite_pizzas[0].title()} is my all time favorite!")
# print(f"{lst_favorite_pizzas[1].title()} is really good too, though.")
# print(f"But, I also love {lst_favorite_pizzas[2].title()}.")
# print("\nI just really love pizza!!")

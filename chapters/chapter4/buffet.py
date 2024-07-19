# 4-13. Buffet:
"""A buffet-style restaurant offers only five basic foods. Think of five simple
foods, and store them in a tuple.
- Use a *for* loop to print each food the restaurant offers.
- Try to modify one of the items, and make sure that Python rejects the change.
- The restaurant changes its menu, replacing two of the items with different
foods. Add a line that rewrites the tuple, and then use a *for* loop to print
each of the items on the revised menu. 
"""

# declare tuple
tp_foods = (

    "chicken & waffles",
    "steak & potatoes",
    "lasagna",
    "salad bar",
    "dessert bar",

    )
# items in tuple for loop
for food in tp_foods:
    print(food)
# try to modify/ call an python error
# tp_foods[2] = "pizza"
# print(tp_foods)
# rewrite tuple
print("\nnew menu:")
tp_foods = (

    "chicken & waffles",
    "steak & baked potato",
    "pepperoni pizza",
    "salad bar",
    "dessert bar",

    )

for food in tp_foods:
    print(food)

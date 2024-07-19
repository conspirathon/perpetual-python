# 3-10. Every Function: Think of things you could store in list. For example, you could make a list of mountain, rivers, countries, cites, languages, or anything else you you'd like.
# Write a program that creates a list containing these items and then use each function introduced in this chapter at least once.

lst_of_random_places = [
    "tokyo",
    "egypt",
    "black sea",
    "amazon rain forest",
    "machu picchu",
    "amsterdam",
]

print("\nOriginal list:")
print(lst_of_random_places)
print("\nLength of list:")
print(len(lst_of_random_places))
print("\nSorted list:")
print(sorted(lst_of_random_places))
print("\nSorted reverse-alph list:")
print(sorted(lst_of_random_places, reverse=True))
print("\nSorted reverse list:")
lst_of_random_places.reverse()
print(lst_of_random_places)
print("\nSort list:")
lst_of_random_places.sort()
print(lst_of_random_places)
print("\nSort list reverse-alph:")
lst_of_random_places.sort(reverse=True)
print(lst_of_random_places)
print("\nRemove item from list:")
removed_item = lst_of_random_places.pop()
print(removed_item)
print("\nNew list:")
print(lst_of_random_places)
print("\nCausing an index error as per 3-11:")
print(lst_of_random_places[5])



# # 3-8. Seeing the World: Think of at least five places in the world you'd like to visit.
# lst_locations = ["japan", "egypt", "finland", "holland", "peru"]
# print("\nOriginal list:")
# print(lst_locations)
# # sorted
# print("\nSorted list:")
# print(sorted(lst_locations))
# print("\nCheck if original exist:")
# print(lst_locations)
# # sorted reverse-alphbetical
# print("\nSorted reverse-alphbetical list:")
# print(sorted(lst_locations, reverse=True))
# print("\nCheck for original:")
# print(lst_locations)
# # reverse list
# print("\nReverse list:")
# lst_locations.reverse()
# print(lst_locations)
# lst_locations.reverse()
# print(lst_locations)
# # sort list
# print("\nSort list:")
# lst_locations.sort()
# print(lst_locations)
# # sort list reverse-alphbetical
# print("\nSort list reverse-alphbetical:")
# lst_locations.sort(reverse=True)
# print(lst_locations)
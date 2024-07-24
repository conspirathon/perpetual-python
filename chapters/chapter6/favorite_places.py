# 6-9. Favorite Places:
favorite_places = {}
favorite_places["katie"] = [
    "democrate point",
    "catnip & carrots",
    "maryann's house",
]
favorite_places["nigel"] = [
    "napping on a keyboard",
    "bed, sleeping (on a human of course)",
    "sleeping on the bottom step",
]
favorite_places["patti"] = [
    "anywhere with food",
    "sunbathing; anywhere",
    "food",
]

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")
    print()
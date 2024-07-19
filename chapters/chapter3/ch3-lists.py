# Code snippets from python crash course

def main():
    names = ["nigel", "mylo", "mario"]
    transportation = ["single roller skate", "half of a skateboard", "used tire", "broken jump rope"]
    food = ["timmothy hay", "bananas", "critical care"]
    message = f"My friend {names[1].title()} is so cool! He gets around town using a {transportation[0].title()} while eating {food[0].title()}?!"
    result = message

    print(result)

    too_expensive = "broken jump rope"
    transportation.remove(too_expensive)
    print(transportation)
    print(f"\nA {too_expensive.title()} is too expensive for me.")
    last_owned = transportation.pop(2)
    last_owned2 = food.pop(2)
    print(f"The last thing I owned was a {last_owned.title()} and some {last_owned2.title()}. \n\t--{names[2]} 1971")





if __name__ == "__main__":
    main()
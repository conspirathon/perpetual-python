# 5-3. Alien Colors #1:
alien_colors = "red"

if "green" in alien_colors:
    print("Player earned 5 points!")

if "red" in alien_colors:
    print("Player earned 5 points!")

alien_colors = "yellow"

if "green" in alien_colors:
    print("Player earned 5 points!")

if "red" in alien_colors:
    print("Player earned 5 points!")

# 5-4. Alien Colors #2:
alien_colors = "green"  

if "green" in alien_colors:
    print("Player earned 5 points for shooting the alien.")
else:
    print("Player earned 10 points.")

alien_colors = "red"

if "green" in alien_colors:
    print("Player earned 5 points for shooting the alien.")
else:
    print("Player earned 10 points.")

# 5-5. Alien Colors #3:
alien_colors = "green"
alien_colors = "yellow"
alien_colors = "red"

if "green" in alien_colors:
    print("Player earned 5 points.")
elif "yellow" in alien_colors:
    print("Player earned 10 points.")
else:
    print("Player earned 15 points.")

# 5-6. Stages of Life:
age = 66
age = 42
age = 19
age = 11
age = 3
age = 0


if age < 2:
    print("Person is a baby.")
elif age >= 2 and age < 4:
    print("Person is toddler.")
elif age >= 4 and age < 13:
    print("Person is a kid.")
elif age >= 13 and age < 20:
    print("Person is a teenager.")
elif age >= 20 and age < 65:
    print("Person is an adult.")
else:
    print("Person is an elder")

# 5-7. Favorite Fruits:
favorite_fruits = [
    "banana",
    "watermelon",
    "apple",
]

# if "banana" in favorite_fruits:
#     print(f"You really like {favorite_fruits[0].title()}s")
# if "watermelon" in favorite_fruits:
#     print(f"You really like {favorite_fruits[1].title()}")
# if "apple" in favorite_fruits:
#     print(f"You really like {favorite_fruits[2].title()}s")
# if "avocado" in favorite_fruits:
#     print("You really like Avocados!")
# if "mango" in favorite_fruits:
#     print("You really like Mangos.")

for fruit in favorite_fruits:
    if fruit in favorite_fruits:
        print(f"You really love {fruit}")
    else:
        print("Guess you don't like that fruit.")
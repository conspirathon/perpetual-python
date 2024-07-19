import random

def main():
    print("Please choose an option to run:")
    print("1. Generate random sentence")
    print("2. Generate random numbers")
    print("3. Create greeting")
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        names = ["mylo", "nigel", "mario", "patti", "moe", "mj", "muffin"]
        transportation = ["single roller skate", "uni-cycle", "used tire", "broken jump rope", "toy rocket"]
        food = ["timmothy hay", "critical care", "meow mix"]
        result = random_sentence(names, transportation, food)
        print(result)
    elif choice == "2":
        random_numbers = generate_random_numbers(5, 1, 10)
        print(f"Random numbers: {random_numbers}")
    elif choice == "3":
        name = input("Enter a name for the greeting: ")
        greeting = create_greeting(name)
        print(greeting)
    else:
        print("Invaild choice. Please enter 1, 2, or 3.")

def random_sentence(names, transportation, food):
    name = random.choice(names)
    transport = random.choice(transportation)
    f = random.choice(food)

    return f"My friend {name.title()} is so cool! They get around town using a {transport.title()}, while eating {f.title()}."

def generate_random_numbers(count, start, end):
    return [random.randint(start, end) for _ in range(count)]

def create_greeting(name):
    return f"Hello, {name}! Welcome to the program."

if __name__ == "__main__":
    main()
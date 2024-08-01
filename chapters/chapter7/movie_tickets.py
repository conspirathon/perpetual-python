# 7-5. Movie Tickets:
print("######################")
print("Welcome to SSH Theater")
print("######################")
prompt = "\nTell me your age, and I'll tell you the ticket price. "
prompt += "\n(Enter 'quit' to exit.) "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    try:
        age = int(age)
        if age < 0:
            print("Please enter a valued age or 'quit' to exit.")
            continue
    except ValueError:
        print("Please enter a valid age or 'quit' to exit.")
        continue
    if age <= 3:
        price = 0
    elif age > 3 and age <= 12:
        price = 10
    else:
        price = 15
    
    print("==========================================================")
    print(f"\tYou are {age} years old, your ticket price is ${price}.")
    print("==========================================================")
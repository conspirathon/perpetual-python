# 7-4. Pizza Toppings:
print("##########################")
print("Welcome to Terminal Pizza!")
print("##########################")
prompt = "\nPlease enter the toppings you'd like on your pizza:"
prompt += "\n(Enter 'quit' when you're done choosing.) "
while True:
    toppings = input(prompt)
    if toppings == 'quit':
        break
    else:
        print(f"{toppings.title()} added. Anything else?")
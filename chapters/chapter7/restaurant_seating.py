# 7-2. Restaurant Seating:

people = input("How many people are in your party? ")
people = int(people)

if people > 8:
    print(f"\nFor parties of {people}, there will be a wait time of 30 min.")
else:
    print(f"\nYour table is ready.")
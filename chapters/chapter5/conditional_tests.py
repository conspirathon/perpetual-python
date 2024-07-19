# 5-2. More Conditional Tests:
"""
Have at least one *True* and one *False* result for each of the following:
- Tests for equality and inequality with strings
- Tests using the *lower()* method
- Numerical tests involving equality and inequality, great than and less than,
greater than or equal to, and less than or equal to
- Tests using the *and* keyword and the *or* keyword
- Test whether an item is in a list
_ Test whether an item is not in a list
"""
# Start Test Case 1:
string0 = "hello"
string1 = "goodbye"
print(f"string0: '{string0.title()}', string1: '{string1.title()}'")
if string0 == string1:
    print("The strings are equal.")
else:
    print("The strings are not equal")

# Start Test Case 2:
string2 = "i love pizza!"
string3 = "I LOVE PIZZA!"
print(f"\nstring2: '{string2}', string3: '{string3}'")
if string2 != string3.lower():
    print("The strings are not equal.")
else:
    print("The strings are equal.")

# Start Test Case 3:
num0 = 33
num1 = 3
num2 = 45
num3 = 17
print(f"\nnum0: {num0}, num1: {num1}")
if num1 != num0:
    print("The numbers are not equal.")
else:
    print("The numbers are equal.")

# Start Test Case 4:
print(f"\nnum0: {num0}, num1: {num1}")
if num0 <= num1:
    print(f"{num0} is less or equal to {num1}")
else:
    print(f"{num0} is not less or equal to {num1}")

# Start Test Case 5:
print(f"\nnum0: {num0}, num1: {num1}")
if num0 >= num1:
    print(f"{num0} is greater or equal to {num1}")
else:
    print(f"{num0} is not greater or equal to {num1}")

# Start Test Case 6:
print(f"\nnum0: {num0}, num1: {num1} num2: {num2}, num3: {num3}")
if num0 > num1 and num0 > num3 or num0 < num2:
    print(f"{num0} is greater than {num1} and {num3} or less than {num2}")
else:
    print(f"{num0} is not greater than {num1} and {num3} or less than {num2}")

# Start Test Case 7:
katies_favs = [
    "moe",
    "mario",
    "mj",
    "mylo"
]

result = "mylo" in katies_favs
print(result)

# Start Case 8
result2 = "muffin" in katies_favs
print(result2)

# Start Case 9:
rabbit = "muffin"
if rabbit not in katies_favs:
    print(f"{rabbit}, is free to piss where she pleases. If she wants.")

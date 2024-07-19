# Conditional Tests:
"""
Write a series of conditional tests. Print a statement describing each test and
your prediction of the results of each test. Your code should look something
like this:
```python
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
```
- Look closely at your results, and make sure you understand why each line
evaluates to *True* or *False*.
- Create at least 10 tests. Have at least 5 tests evalute to *True* and another
5 tests evaluate to *False*.
"""
# start of code:
print("Test case 1:")
beer = "IPA"
print("Is beer == 'IPA'? I predict True.")
print(beer == "IPA")

(print("\nTest case 2:"))
print("Is beer == 'ipa'? I predict False.")
print(beer == "ipa")

print("\nTest case 3:")
pizza_toppings = ["xtr-cheese", "half-pepperoni", "half-sausage"]
print("Is topping == 'half-pepperoni'? I predict True.")
print("half-pepperoni" in pizza_toppings)

print("\nTest case 4:")
print("Is topping == 'onions'? I predict False.")
print("onions" in pizza_toppings)

print("\nTest case 5:")
at_shop = ["honda", "toyota", "subaru"]
car = "mazda"
print("Is 'car' == 'at_shop'? I predict False.")
if car not in at_shop:
    print(f"{car.title()}, is not in the repair shop.")
else:
    print(f"{car.title()}, is in the repair shop.")

print("\nTest case 6:")
at_shop.append(car)
print("Is 'car' == 'at_shop'? I predict True.")
if car not in at_shop:
    print(f"{car.title()}, is not in the repair shop.")
else:
    print(f"{car.title()}, is in the repair shop.")

print("\nTest case 7:")
car = at_shop[2]
print("Is 'car' == 'at_shop'? I predict True.")
if car not in at_shop:
    print(f"{car.title()}, is not in the repair shop.")
else:
    print(f"{car.title()}, is in the repair shop.")

print("\nTest case 8:")
age = 21
age2 = 19
drinking_age = 21
print("Is age == 21? I predict True.")
print(age == 21)

print("\nTest case 9:")
print("Is 'age' == 'age2'? I predict False.")
print(age == age2)

print("\nTest case 10:")
print("Is 'age2' == 'drinking_age'? I predict False.")
print(age2 >= drinking_age)

# numbers = range(1, 21)
# for num in numbers:
#     print(num)

# numbers = []
# for num in range(1, 1_000_000):
#     numbers.append(num)
# print(f"Minimum number:\n{min(numbers)}")
# print(f"Maximum number:\n{max(numbers)}")
# print(f"Sum of numbers:\n{sum(numbers)}")

# numbers = []
# for num in range(1, 20, 2):
#     numbers.append(num)
# print(numbers)

# threes = []
# for three in range(3, 30, 3):
#     threes.append(three)
# print(threes)

cubes = []
for cube in range(1, 10):
    cubes.append(cube**3)
print(cubes)
# list comprehension
cubes = [cube**3 for cube in range(1, 10)]
print(cubes)
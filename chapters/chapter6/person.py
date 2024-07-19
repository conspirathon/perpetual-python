# 6-1. Person:
person = {
    "first_name": "katie",
    "last_name": "scarr",
    "age": 36,
    "city": "new york city"
}

print("First Name:", person["first_name"].title())
print("Last Name:", person["last_name"].title())
print("Age:", person["age"])
print("City:", person["city"].title())

# # Define labels for each key.
# labels = {
#     "first_name": "First Name",
#     "last_name": "Last Name",
#     "age": "Age",
#     "city": "City",
# }

# for key, label in labels.items():
#     value = person[key]
#     if isinstance(value, str):
#         print(f"{label}: {value.title()}")
#     else:
#         print(f"{label}: {value}")
# Creating a list using list comprehension
squared_list = [x**2 for x in range(5)]
print(squared_list)

# Check the type
print(type(squared_list))
# Iterate over items and print them
for number in squared_list:
    print(number)

squared_list = (x**2 for x in range(5))
print(squared_list)

# Check the type
print(type(squared_list))
# Iterate over items and print them
for number in squared_list:
    print(number)

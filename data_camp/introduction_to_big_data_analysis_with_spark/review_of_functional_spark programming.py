"""

"""
from pyspark import SparkContext

sc = SparkContext
my_list2 = []

# lambda functions
double = lambda x: x * 2
print(double(3))


def cube(x):
    return x ** 3


# no return statement for lambda
# can put lambda function anywhere
g = lambda x: x ** 3

print(g(10))
print(cube(10))

# map() function takes a function and a list and returns a new list which
# contains items returned by that function for each item
items = [1, 2, 3, 4]
items_list = list(map(lambda x: x + 2, items))
print(items_list)

# the filter function takes a function and a list and returns a new list for
# which the function evaluates as true
odd_numbers = list(filter(lambda x: (x % 2 != 0), items))
print(odd_numbers)

# example: use of lambda() with map()
# Print my_list in the console
print("Input list is", map)

# Square all numbers in my_list
squared_list_lambda = list(map(lambda x: x ** 2, my_list))

# Print the result of the map function
print("The squared numbers are", squared_list_lambda)

# example: use of lambda() with filter()
# Print my_list2 in the console
print("Input list is:", my_list2)

# Filter numbers divisible by 10
filtered_list = list(filter(lambda x: (x % 10 == 0), my_list2))

# Print the numbers divisible by 10
print("Numbers divisible by 10 are:", filtered_list)

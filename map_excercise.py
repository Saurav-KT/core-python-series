"""map() function returns a map object(which is an iterator) of the results after applying the given function to each
item of a given iterable (list, tuple etc.)
Python map() Function
Syntax: map(fun, iter)
Parameters: fun: It is a function to which map passes each element of given iterable.
iter: It is iterable which is to be mapped.

NOTE: You can pass one or more iterable to the map() function.
"""


# Python program to demonstrate working of map.

def addition(n):
    return n ** 2


# We square all numbers using map()
numbers = (1, 2, 3, 4)
# result = map(addition, numbers)
# print(list(result))
# output = [1, 4, 27, 256]

# We can also use lambda expressions with map to achieve above result.
# result = map(lambda x: x ** 2, numbers)
# print(list(result))


# Add two lists using map and lambda
numbers1 = [1, 2, 3, 6]
numbers2 = [4, 5, 6, 7, 45]

result = map(lambda x, y: x + y, numbers1, numbers2)
# print(list(result))

# List of strings
l = ['sat', 'bat', 'cat', 'mat']
# map() can listify the list of strings individually
test = list(map(list, l))
print(test)


# using if statement with map():
# Define a function that doubles even numbers and leaves odd numbers as is
def double_even(num):
    if num % 2 == 0:
        return num * 2
    else:
        return num


# Create a list of numbers to apply the function to
numbers = [1, 2, 3, 4, 5]
# Use map to apply the function to each element in the list
result = list(map(double_even, numbers))
print(result)


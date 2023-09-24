"""Tuple is a collection of objects separated by commas
A tuple is immutable unlike lists which are mutable
python uses the parentheses () to create empty tuple use commas(,) to define a tuple
delete operation cannot be performed on tuple unlike array, dict"""

# extract values into a variable called tuple unpacking
# param1, param2, param3, *param4 = ("hello", "tuples", "world", "do", "solid", "practice")
# print(param4)

x = ("hello", "tuples", "world")
y = ("do", "solid", "practice")
z = (*x, *y)
print(z)

# Empty Tuple
my_tuple = ()

# Tuple with mixed datatype
my_tuple = (1, 2, 3, 4, "hello", 4.6)

item = ("hello", "tuples", "world", "do", "solid", "practice")
# Tuple slicing

# print(item[3:])


# nested tuple
my_tuple = ("laptop", "keyboard", ("my", "dream", "xyz"), [3, 6, 4], {"emp_name": "Rajesh"})
# del my_tuple[1]
# del my_tuple

tuple_obj = [('IT', "App development", "800$", "Remarks: requirement to be discussed "),
             ("IT", "Data Center", "1000$", "Remarks: new facility"),
             ("IT", "Work space", "4000$", "Remarks: under discussion ")]

for index, val in enumerate(tuple_obj):
    dept, func, value,k = val
    print(dept, func, value,k)
# for i, (x, y, z, *a) in enumerate(tuple_obj):
#     print(i, x, y, z, a)

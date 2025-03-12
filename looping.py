# 1. enter loop
# 2. test expression -->If False--> exit the loop
# 3. If True --> body of loop
dept = ["IT", "Marketing", "Accounts", "User collaboration", "supply chain", "IT", "IT"]
segment = ["Hardware", "software", "payroll", "customer feedback", "warehouse", "transport"]

# Continue statement with For loop
# for i in dept:
#     if "User collaboration" in i:
#         continue
#     print(i)

# Continue with While loop
# listcount = len(dept)-1
# while listcount >= 0:
#     if "supply chain" in dept[listcount]:
#         listcount -= 1
#         continue
#     print(dept[listcount])
#     listcount -= 1

# Continue with While loop
# listcount = len(dept)
# i = 0
# while i < listcount:
#     if "supply chain" in dept[i]:
#         i += 1
#         continue
#     if "User collaboration" in dept[i]:
#         i += 1
#         continue
#     print(dept[i])
#     i += 1


# For loop
# for x in dept:
#     print(x)

# Range method for looping
# for i in range(len(dept)):
#     print("index",i, "value", dept[i])

# for key,value in enumerate(dept, start=100):
#     print(key,value)


# Zip method for loop
# for obj1,obj2 in zip(dept,segment):
#     print(obj1, obj2)

intlist = [64, 39, 72, 47, 100, 380, 58, 2907, 45, 64, 47]

# with duplicate
# for i in sorted(dept):
#     print(i)

# without duplicate
# for i in sorted(set(dept)):
#     print(i)

# Print the value in reverse order
# for i in reversed(dept):
#     print(i)

# iter_obj = iter(dept)
# while True:
#     try:
#         element= next(iter_obj)
#         print(element)
#     except StopIteration:
#         break

# List Comprehension
# Syntax: [expression for element in iterable if condition]
# syntax contains three parts: an expression, one or more for loop, and optionnally one or more if condition
# The list comprehension must be in the square bracket []
# The result of list comprehension will be stored in the new list.

# x = [i for i in dept if "supply chain" not in i]
# print(x)

# Problem statement: find even numbers from 0 to 20
# even_number = []
# for x in range(21):
#     if x % 2 == 1:
#         even_number.append(x)
# print(even_number)

# new_list = [x for x in range(50) if x%2==0 if x%5==0]
# print(new_list)

# new_list = [str(x) + "=even" if x%2 ==0 else str(x)+"=odd" for x in range(10)]
# print(new_list)

matrix=[[1,2,3],[4,5,6],[7,8,10]]
flatlist=[num for row in matrix for num in row]
print(flatlist)

a = [11, 24, 44, "fine", [0, 4, "clear", 5, 6, "range2", ]]
y= [x for x in a[4] if x == "clear"]
z=[x for ind, x in enumerate(a[4]) if ind==2]
print(z)

a = []
a = [1, 6.90, "Hello World","List comprehension","Be pythonic",430]

# Nested list
b = [1, 6.90, "Hello World",[4,"hello python", 5.78,"hello python","hello python"]]

c = [1,700, 6.90, 190]

# b[2] = 490
# b.append(450)
# b.extend([3,70,"hello list"])
# print(b+c)

# Python list method
# Insert(),append(),extend(),remove(),pop(),clear(),count(),sort(),reverse(),copy()
# b.append(500)
# b.extend([670,590,700])
# b[3].append("list nested array example")

# b.insert(1,"insert method")
# b[3].remove("hello python")
# c=b[3].count(4)
c.sort(reverse=True)
new_list = b.copy()
new_list.append(40000)
# b[3].clear()
del b[2]
# print(new_list)
print(b)

# List comprehension examples
# Expression: [expression for member in iterable]
# Expression: [expression for member in iterable(if conditional)]



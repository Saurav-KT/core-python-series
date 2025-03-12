import array as arr
'''i - integer,I - integer,l- signed long, L- unsigned long, f- float , d- float, b- int,B- int  '''

'''Array are mutable, their element can be changed '''
a = arr.array('i',[1,4,7,59,62,50, 490,300])
# a[1]= 180
# a[2:5] = arr.array('i', [270,4,78])

# add one iten to the array using the append() method
# a.append(30)
# a.append(1000)
# add multiple iten to the array using the extend() method
a.extend([30,1000])
# print("Last element", a[-1])
# print("first element", a[0])

# Slicing
# print(a[2:5])
# print(a[:-3])
# print(a[5:])
# print(a[:])

# combine two array using + operator
# a = arr.array('i',[1,4,7,59,62,50, 490,300])
# b = arr.array('i',[1,34,7,49,62,50, 450,200])
# c = a+b
# print(c)

# Remove python array element
# we can delete one or more items from an array using python's del statement
# del a[10]
# del a
a.remove(1000)
print(a)
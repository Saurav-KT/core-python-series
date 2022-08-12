# Tuple is a collection of objects seperated by commas
# A tuple is immutable unlike lists which are mutable
# python uses the parentheses () to create empty tuple
# use commas(,) to define a tuple
# delete operation cannot be performed on tuple unlike array, dict

# tuple unpacking
# abc,x,y,*z = ("hello", "tuples","world","do","solid","practice")

# x=("hello", "tuples","world")
# y=("do","solid","practice")
#
# z= (*x,*y)
# print(z)

#Empty Tuple
my_tuple =()

#Tuple with mixed datatype
my_tuple= (1,2,3,4, "hello", 4.6)

item = ("hello", "tuples","world","do","solid","practice")
#Tuple slicing

print(item[3:])



#nested tuple
my_tuple =("laptop", "keyboard",("my","dream","xyz"),[3,6,4],{"emp_name":"Rajesh"})
# print(my_tuple)
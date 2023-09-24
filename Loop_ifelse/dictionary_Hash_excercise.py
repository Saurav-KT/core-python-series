# Dictionary Example
# Dictionary variable declaration
my_dict = {}
my_dict = [{"emp_first_name": "Anuj Kr", "last_name": "shetty", "dept": "telecom", "role": "customer service",
            "dateofjoining": "03/02/2022",
            "salaryband": "52LPA"},
           {"emp_first_name": "Amit", "last_name": "sharma", "dept": "Finance", "role": "SDE3 service",
            "dateofjoining": "03/07/2022",
            "salaryband": "40LPA"},
           {"emp_first_name": "Kruthika", "last_name": "A.", "dept": "Operation", "role": "customer service",
            "dateofjoining": "03/05/2021",
            "salaryband": "18LPA"},
           {"emp_first_name": "Akhila", "last_name": "Khandala", "dept": "IT-Software",
            "role": "Principal Engineer service",
            "dateofjoining": "06/09/2021", "salaryband": "45LPA"}
           ]


# for dic in my_dict:
#     for key, value in dic.items():
#         if "role" in dic:
#             dic[key] = "research engineer"
# print(my_dict)

# extract value from dictionary
# cats = {'Tom': {'color': 'white', 'weight': 8}, 'Klakier': {'color': 'black', 'weight': 10}}
# cat_attr = {}
# for k,v in cats.items():
# print(cats[k]['color'],cats[k]['weight'])

# extract value from dictionary dynamic keys
# for cat in cats:
#     for attr in cats[cat]:
#         print(cats[cat][attr])


# To check key exist in dictionary
def check(key, params):
    if params in key:
        return True
    else:
        return False


# my_dict = list(map(lambda x: x["role"] == "ABC" if x["emp_name"] == "Anuj Kr" else x["emp_name"], my_dict))
# for dic in my_dict:
#     for key in dic:
#         if check(key, "dept"):
#             dic[key] = "Operation"

# IsKeyExist
# if "role" in key:
#     dic["salaryband"] = "28LPA"
# if "emp_first_name" in key:
#     dic["salaryband"] = "28LPA"

# print(my_dict)

# Lambda expression syntax
#   lambda argument: expression

"""Lambda rules
--------------------------
Can have only one expression
can have multiple argument
Lambda function gets evaluated and returned no explicit return statement required
"""
# To Get specific key value from list of dictionary
# map expression
# map(sequence,callback)

empName = list(map(lambda x: '{}'.format(x["dept"]), my_dict))
print(empName)
#
dict_list = list(filter(lambda x: x["dept"] == "telecom" and int(x["salaryband"][:-3]) > 20, my_dict))
print(dict_list)

# obj = [x["role"] for x in my_dict if x["emp_name"] == "Anuj Kr"]
# print(obj)
# for d in my_dict:
#     d.update((k, "value3") for k, v in d.items() if k == "Kruthika A.")

# for d in my_dict:
#     d.update(("role", "value3") for k, v in d.items() if "emp_name" == "Kruthika A.")

# print(my_dict)


# Dictionary Comprehension
# Syntax: {key: value for (key, value) in dict.items() if condition}
Grocery_item = {"Onion": 40, "Egg": 10, "Carrot": 50, "Rice": 70, "Apple": 240, "Sugar": 270, "Pulse": 370}
new_dict = {}
# for key,value in Grocery_item.items():
#     if "Onion" in key:
#         new_dict[key]= value *70
#     else:
#         new_dict[key] = value
# print(new_dict)


new_dict = {item: (price * 170 if "Onion" in item else price) for (item, price) in Grocery_item.items()}
# print(new_dict)

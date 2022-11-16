# Example of Treating the functions as objects
"Implementation details: We have assigned the function welcome to a variable. This will not call the function instead it takes the function object referenced by a welcome and creates a second name pointing to it, welcome_method."


def welcome(params):
    return params


# print(welcome("world of object"))
# welcome_method = welcome
# print(welcome_method("welcome to the world of python"))


# Passing the function as an argument
def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


# def greet(func):
#     # storing the function in a variable
#     greeting = func("""Hi, I am created by a function passed as an argument.""")
#     print(greeting)
#
#
# greet(shout)
# greet(whisper)

# Returning functions from another function
# we have created a function inside of another function and then have returned the function created inside
def create_adder(x: int) -> int:
    def adder(y: int) -> int:
        return x + y
    return adder


add_val = create_adder(100)
x1 = add_val(10)
print(x1)

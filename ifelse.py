try:
    num = int(input("Enter a number:"))
    if num > 0:
        print("greater than zero", num)
    elif num == 0:
        print("zero value", num)
    elif num < 0:
        print("negative value", num)
    else:
        print("something else", num)
except Exception as ex:
    print(ex)
# finally:
#     print("Please enter numeric value")

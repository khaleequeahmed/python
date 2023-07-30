try:
    a = int(input("Enter a Number: "))
    c = 1/a
    print(c)
except ZeroDivisionError as e:
    print("Make Sure you are not dividing with 0")
    # print(e)
except ValueError as e:
    print("Please Enter a valid value")
    # print(e)
print("Thanks for running this code")
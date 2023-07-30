# # 1. if-elif-else ladder in python
# a = 3
# if(a>10):
#     print("The Value of a is greater than 10")
# elif(a>7):
#     print("The Value of a is greater than 7")
# elif(a<8):
#     print("The Value of a is lesser than 8")
# else:
#     print("The Value of a is not greater or lesser than given values")
# print("Done")

#2. Multipules if Statements
a = 10
#independent
if(a>10):
    print("The Value of a is greater than 10")
if(a>7):
    print("The Value of a is greater than 7")
if(a<8):
    print("The Value of a is lesser than 8")
#ladder
if(a>12):
    print("The Value of a is Greater than 12")
elif(a>2):
    print("The Value of a is greater than 2")
else:
    print("The Value of a is not greater or lesser than given values")
print("Done")
#Table
num=int(input("Enter the Number\n"))
for i in range(1, 11):
    print(str(num) + "x" + str(i) + "=" + str(i*num))

# method 2

num1=int(input("Enter the Number\n"))
for i1 in range(1, 11):
    print(f"{num1}x{i1}={i1*num1}")
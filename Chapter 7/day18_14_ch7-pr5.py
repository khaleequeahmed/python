# num= int(input("Enter the Number\n"))
# sum=0
# for i in range (1, 10):
#     sum = sum *i
# print(f"the sum of {num} is {sum}")



#ChatGPT answer

n = int(input("Enter a positive integer: "))
sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print("The sum of the first", n, "natural numbers is", sum)

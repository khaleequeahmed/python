# Reversed Table
num=int(input("Enter the Number\n"))
for i in range (10,0,-1):
    print(str(num) + "x" + str(i) + "=" + str(i*num))

# # method 2

# num1=int(input("Enter the Number\n"))
# for i1 in range(1, 11):
#     print(f"{num1}+{i1}={i1*num1}")



# ChatGPT reponse

n = int(input("Enter a positive integer: "))

for i in range(10, 0, -1):
    print(n, "x", i, "=", n*i)

'''In this program, the user is prompted to enter a 
positive integer `n`. We then use a for loop with
the `range` function to iterate over the values from 10 down to 1,
with a step size of -1 to traverse in reverse order.
During each iteration of the loop, we print out the current value of n,
the multiplication symbol "x", the current value of `i`,
and the product of `n` and `i`. This produces 
the multiplication table of n in reverse order, from 10 down to 1.'''

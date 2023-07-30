# n! = 1 * 2 * 3 * 4...n
# n! = [1 * 2 * 3 * 4...n-1] *n
# n! = n* (n-1)!


# n=5
# product=1
# for i in range(n):
#     product=product * (i+1)
# print(product)

# in function
def factorial_iter(n):
    product=1     #--> main jitna product value barhao ga to utna hi baar value ko multipy karta jaye ga
    for i in range(n):
        product = product * (i+1)
    return product
# print(factorial_iter(4))
# f=(factorial_iter(5))
# print(f)  #--. we can also assign in variable

def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_recursive(n-1)
print(factorial_recursive(4))
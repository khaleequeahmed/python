num=int(input("Enter the Number: "))
prime=True
for i in range(2, num):
    if (num%i == 0):
        prime=False
        break
if prime:
    print("this number is prime")
else:
    print("this number is not prime")


#ChatGPT repsone on what is prime numbers

'''Prime numbers are positive integers greater than 1 that have no positive integer divisors other
than 1 and themselves. In other words, a prime number is a positive integer
that is divisible only by 1 and itself.Some examples of prime numbers include:
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
67, 71, 73, 79, 83, 89, 97, 101, and so on.
Prime numbers are important in number theory and have various 
applications in computer science and cryptography.'''
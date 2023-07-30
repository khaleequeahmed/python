n = 3
for i in range (3):
    print("* " * (0*i+1), end="")
    print("* " * (i*0+1), end="")
    print(" * " * (0*i+1), end="")
    print(" " * (n-i-1))
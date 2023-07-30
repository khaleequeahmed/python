try:
    i = int(input("enter a number: "))
    c = 2/i
    print(c)
except Exception as e:
    print(e)
    exit()
finally:
    print("we're done") 

print("Thanks for using the code")
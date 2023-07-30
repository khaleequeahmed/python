try:
    i = int(input("enter a number: "))
    c = 2/i
    print(c)
except Exception as e:
    print(e)

except ZeroDivisionError as a:
    print("Make sure you are not dividing with 0")    
else:
    print("Code ran successfully") 
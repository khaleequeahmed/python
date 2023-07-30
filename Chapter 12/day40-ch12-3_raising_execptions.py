def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("Please enter a valid value")
    

a = increment (6) 
print(a)

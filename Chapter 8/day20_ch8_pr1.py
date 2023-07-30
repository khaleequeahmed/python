def maximun (num1, num2, num3):
    if (num1>num2):
        if (num1>num3):
            return num1
        else:
            return num3
    if (num2>num3):
        return num2 
    else:
        return num3       

m=maximun(10,11,9)
print("The Value of the maximum is: " + (str(m)))
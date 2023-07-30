class Employee:
    company="Google"
    salary = 1000

Khaleeque=Employee()
Ateeque=Employee()

# Creating instance attribute salary for both the objects
Ateeque.salary=100

# print(Khaleeque.salary)
print(f"Khaleeque's Salary : {Khaleeque.salary}\nAteeque's Salary : {Ateeque.salary}")


# Below line throws an error as address is not present in instance/class 
# print(Khaleeque.adress)
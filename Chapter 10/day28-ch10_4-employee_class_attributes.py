class Employee:
    company="Google"

Khaleeque=Employee()
Ateeque=Employee()
print(Khaleeque.company)
print(Ateeque.company)
Employee.company='Youtube'
print(Khaleeque.company)
print(Ateeque.company)
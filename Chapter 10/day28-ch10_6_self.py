class Employee:
    company="Google"
    def getsalary(self):
        print(f"Salary for this Employee working in {self.company} is {self.salary}")

Khaleeque=Employee()
Khaleeque.salary=100000
Khaleeque.getsalary() # Employee.getsalary(Khaleeque)

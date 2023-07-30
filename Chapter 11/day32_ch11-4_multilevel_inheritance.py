class Person:
    country="Pakistan"
    
    def work(self):
        print("Iam a Person and iam Working")


class Employee(Person):
    company = "Honda"

    def work(self):
        print("iam a Employee and iam also Working")

    def getsalary(self):
        print(f"Salary is {self.salary} ")

class Programmer(Employee):
    company = "Fiverr"

    def work(self):
        print("Iam a Programmer and iam also Working")    

    def getsalary(self):
        print("Salary is not available")

p=Person()
print(p.country)
# print(p.company) -> Throws an error
p.work()

e=Employee()
Employee.salary=100
e.getsalary()
print(e.country)
e.work()

pr=Programmer()
pr.getsalary()
print(pr.country)
print(pr.company)
pr.work()
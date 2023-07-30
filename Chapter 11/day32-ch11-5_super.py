class Person:
    country="Pakistan" 

    def __init__(self):
        print("\nInitializing Person\n")

    def work(self):
        print("Iam a Person and iam Working")


class Employee(Person):
    company = "Honda"

    def __init__(self):
        super().__init__()
        print("Initializing Employee\n")

    def work(self):
        super().work()
        print("iam a Employee and iam also Working")

    def getsalary(self):
        print(f"Your salary is {self.salary}")


class Programmer(Employee):
    company = "Fiverr"

    def __init__(self):
        # super().__init__()
        print("Initializing Programmer\n")

    def work(self):
        # super().getsalary()
        # super().work()
        print("Iam a Programmer and iam also Working")    

    def getsalary(self):
        print("Salary is not available")

# p=Person()
# p.work()

# e=Employee()
# e.salary=10
# e.getsalary()

pr=Programmer()
pr.work()
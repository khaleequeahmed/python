class Employee:
    company='Microsoft'
    def getsalary(self, signature):
        print(f"The Salary of this Employee is {self.salary}\n{signature}")


    @staticmethod
    def greet():
        print("Good Morning, Sir")
        
    @staticmethod
    def time():
        print("The time is 9AM in the Morning")

Khaleeque=Employee()
Khaleeque.salary=50000
Khaleeque.getsalary("Thanks")
Khaleeque.greet() # Employee.greet(Khaleeque)
Khaleeque.time()
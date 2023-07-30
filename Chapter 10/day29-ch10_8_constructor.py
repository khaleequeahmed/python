class Employee:
    company='Google'

    def __init__(self,name,salary,subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("Employee is Created")

    def getDetails(self):
        print(f"The name of the Employee is {self.name}")
        print(f"The salary of the Employee is {self.salary}")
        print(f"The subunit of the Employee is {self.subunit}")


    def getsalary(self, signature):
        print(f"The Salary of this Employee is {self.salary}\n{signature}")


    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9AM in the Morning")

khaleeque=Employee("Khaleeque","100k","Youtube")
# khaleeque=Employee() #--> This throws an error*(missing 3 required positional arguments:)
khaleeque.getDetails()


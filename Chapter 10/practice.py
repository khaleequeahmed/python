# staticmethod
class Employee:
    company="Google"
    @staticmethod
    def greet():
        print("Hi")

    def __init__(self,name,company,hobby):
        print("Employee is created")

        self.name=name
        self.hobby=hobby
        self.company=company

    def getDetails(self):
        print(f"The name of the Employee is {self.name} ")
        print(f"The company of the Employee is {self.company} ")
        print(f"The hobby of the Employee is {self.hobby} ")



        
# Khaleeque=Employee()
Khaleeque.greet()



# constructor

Khaleeque=Employee("Khaleeque","Google","Gaming")
Khaleeque.getDetails()


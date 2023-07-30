#Single Inheritance

# Base/Parent Class
class Employee:
    company='Google'

    def showdetails(self):
        print("This is an Employee")

# Derived/Child Class
class Programmer(Employee):
    language = 'python'
    # company='Youtube'

    def getLanguage(self):
        print(f"The Language is {self.getLanguage}")

    def showdetails(self):
        print("This is an Programmer") #--> Overwrote the showdetails from parent base


e = Employee()
e.showdetails()
p = Programmer()
p.showdetails()
print(p.company)
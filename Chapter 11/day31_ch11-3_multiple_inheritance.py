class Employee:
    company="MasterCard"
    ecode=110

class Freelancer():
    company = "Fiverr"
    level=0

    def upgradelevel(self):
        self.level = self.level +1

class Programmer(Freelancer, Employee):
    name="Khaleeque"
 

p=Programmer()
p.upgradelevel()
print(p.level)
print(p.company)

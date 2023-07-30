class Employee:
    company='dell'
    salary = 1000
    bonussalary = 200

    @property
    def totalsalary(self):
        return self.salary + self.bonussalary

    @totalsalary.setter
    def totalsalary(self, val):
        self.bonussalary = val - self.salary
            

e=Employee()
print(e.totalsalary)
e.totalsalary=1100
print(e.salary)
print(e.bonussalary)
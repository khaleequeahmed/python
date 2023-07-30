class Employee:
    company="dell"
    salary = 500


    # def changesalary(self,sal):
    #     self.__class__.salary=sal

    @classmethod
    def changesalary(cls,sal):
        cls.salary=sal

    @classmethod
    def changecompany(cls,sal):
        cls.company=sal

e=Employee()
print(e.salary)
e.changesalary(100)
print(e.salary)
print(Employee.salary)
print(e.company)
e.changecompany("hp")
print(e.company)
print(Employee.company)

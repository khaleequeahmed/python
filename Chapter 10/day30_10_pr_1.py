class Programmer:
    Company="Microsoft"
    def __init__(self,name,product):
        self.name=name
        self.product=product

    def getinfo(self):
        print(f"The name of the {self.Company} Programmer is \
{self.name} and the product is {self.product}")
        
khaleeque=Programmer("Khaleeque", "Skype")
ateeque=Programmer("Ateeque", "GitHub")

khaleeque.getinfo()
ateeque.getinfo()
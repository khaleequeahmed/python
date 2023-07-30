class RailwayForm:
    formtype="Railway From"
    def printdata(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")


KhaleequesApplication=RailwayForm()
KhaleequesApplication.name=("Khaleeque")
KhaleequesApplication.train=("Sakrand Express")

KhaleequesApplication.printdata()
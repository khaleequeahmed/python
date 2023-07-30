class Train:
    def __init__(self, name, seats, fare):
        self.name=name
        self.seats=seats
        self.fare=fare
        # self.list = list [1,2,3,4,5,6,7]
    def getStatus(self):
        print('***')
        print(f"The Name of the Train is {self.name}")
        print(f"The Seats Avaible in the Train are {self.seats}")
        print('***')
    def fareinfo(self):
        print(f"The price of the seat is {self.fare}")
    
    def Bookticket(self):
        if (self.seats>0):
            print(f"Your Seat has been booked! Your seat number is {self.seats} ")
            self.seats = self.seats -1
        else:
            print("Sorry! The seat are not avaible") 

        
    # def cancelticket(self,seatNo):
    #     pass
    #     self.seatNo=seatNo
    #     print(f"Your seat is cancelled Successfully! {self.seatNo}")
    #     self.seats = self.seats +1
        


cybercity = Train("CyberCity Express: 2132", 7 ,1000)
cybercity.getStatus()
cybercity.fareinfo()
cybercity.Bookticket()
cybercity.getStatus()
cybercity.Bookticket()
cybercity.getStatus()
# cybercity.cancelticket()
# cybercity.getStatus()
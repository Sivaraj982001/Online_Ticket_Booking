import random
from datetime import date
from Database import Fetch

class Theater:
    def __init__(self, name, count, Time, date, coloumn, row,Type, MovieName, Sheatlist=""):
        self.n = name
        self.count=count
        self.d=date
        self.t=Time
        self.c="C"+str(coloumn)
        self.r=row
        self.am=100
        self.ty=Type
        self.Typ=""
        self.M=str(MovieName).upper()
        self.sl = Sheatlist

    def dateGenerator(self):
        Current_date = date.today()
        a = str(Current_date)
        return a

    def payGenerator(self):
        self.am*=self.count
        if self.ty == 1:
            self.am+=100
            self.Typ="Couples Class"
        elif(self.ty == 2):
            self.am+=50
            self.Typ="First Class"
        elif(self.ty == 3):
            self.Typ="Club"
    
    def seatCheck(self):
            if Fetch(self.c,self.r) == "'available'":
                return True
            else: 
                return False

    def Ticket(self):
        a = self.dateGenerator()
        print("------------------------------------------OnlineBooking--------------------------------------")
        print("-----------------------------------------------------------------------------------")
        print("Date = %s"%(a[0:len(a)-2]+str(self.d)))
        print("Time = %s"%(self.t))
        print("------------------------------------------------------------------------------------")
        print("\n")
        print("Name: %s"%(self.n))
        print("Ticket count: %d"%(self.count))
        print("Class: %s"%(self.Typ))
        print("SeatNo: %s"%(self.sl))
        print("Movie: %s"%(self.M))
        print("Total Amount: %d Rs"%(self.am))
        print("\n-----------------------------------------------------------------------------------")







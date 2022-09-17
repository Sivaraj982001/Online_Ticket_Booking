import random 
from datetime import date
import time
from Database import Fetch

class Travel:
    def __init__ (self,name, passengers_count, Current_location, Your_destination, Vehicle, Coloumn, Row, seatlist):
        self.n = name
        self.p = passengers_count
        self.l = Current_location
        self.d = Your_destination
        self.v = Vehicle
        self.am = 0
        self.km = 0
        self.c = "C"+str(Coloumn)
        self.r = Row
        self.t = ""
        self.sl = seatlist
        
    def VehiclepayGenerator(self):
            if self.v == 1:
                self.km = random.randint(9000,100000)
                self.am = self.km*4
                self.am*=self.p
                self.t = "Flight"
            if self.v == 2:
                self.km = random.randint(30,500)
                self.am = self.km*3
                self.am*=self.p
                self.t = "Bus"
            if self.v == 3:
                self.km = random.randint(300,5000)
                self.am = self.km*2
                self.am*=self.p
                self.t = "Train"

    def dateTimeGenerator(self):
            now = time.localtime()
            Current_time = time.strftime("%H:%M:%S", now)
            Current_date = date.today()
            return str(Current_date),str(Current_time)
        
    def seatCheck(self):
            if Fetch(self.c,self.r) == "'available'":
                return True
            else: 
                return False
        
    def Ticket(self):
        d,t = self.dateTimeGenerator()
        print("------------------------------------------OnlineBooking--------------------------------------")
        print("-----------------------------------------------------------------------------------")
        print("Date = ",d)
        print("Time = ",t)
        print("------------------------------------------------------------------------------------")
        print("Name: %s"%(self.n))
        print("Passenger count: %d"%(self.p))
        print("Current Location: %s"%(self.l))
        print("Destination: %s"%(self.d))
        print("Travel Type: %s"%(self.t))
        print("SeatNo: %s"%(self.sl))
        print("Total Kilometers: %d km"%(self.km))
        print("Total Amount: %d Rs"%(self.am))
        print("\n-----------------------------------------------------------------------------------")








        
        

            
            
            



                




    


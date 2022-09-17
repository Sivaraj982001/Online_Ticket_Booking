from Travel import Travel 
from Database import updateData, viewSeats
import random
from Theater import Theater

print("/=========================================Welcome To Online Ticket Booking========================================/")

name = input("Enter your name : ").strip().upper()

print("----------------------------------------Welcom %s--------------------------------------------------------------"%(name))

print("\n-----------------------------------------Catogory Menu----------------------------------------------------------/")
print("1. Travel Ticket")
print("2. Theater Ticket\n")

catogory = int(input("Choose your Option : "))
print("\n---------------------------------------------------------------------------------------------------------------------")

if(catogory == 1):
    print("------------------------------------------------------------Vehicle Menu----------------------------------------------------")
    print("1. Flight")
    print("2. Bus")
    print("3. Train")

    vehicleType = int(input("Choose your Vehicle : "))

    print("\n----------------------------------------------------------------------------------------------------------------------------")
    CurrentLocation = "Virudhunagar"
    print("Your Current Location is %s"%(CurrentLocation))

    Destination = input("Enter your Destination : ")

    Count = int(input("How Many Tickets You want : "))
    print("------------------------------------------------------Seats Menu------------------------------------------------------------------------")

    viewSeats()
    seatList = []
    for i in range(Count,0,-1):
        print("\nChoose your Seat : ")
        Coloumn = int(input("Enter the Coloumn Index: "))
        Row = int(input("Enter the Row Index: "))
        seat = "C"+str(Coloumn)+","+str(Row)
        seatList.append(seat)
        obj1 = Travel(name=name,passengers_count=Count,Current_location=CurrentLocation,Your_destination=Destination,Vehicle=vehicleType,Coloumn=Coloumn,Row=Row, seatlist=seatList)

        if(obj1.seatCheck()):
            obj1.VehiclepayGenerator()
            updateData(obj1.c,"'Filled'",obj1.r)

        else:
            print("Seat is not available")

    sl =""
    for i in range(0,len(seatList)):
        sl=sl+" "+seatList[i]

    obj1.sl = sl
    obj1.Ticket()

if (catogory==2):
    MovieName = input("Enter Movie Name : ")
    Date = int(input("Enter the Date (1-31): "))

    print("---------------------------------------------Time Menu-------------------------------------------")
    Time = ["7.30AM","10.30AM","2.30AM","6.30PM","10.30PM"]
    for i in range(len(Time)):
        print("%d. %s\n"%(i+1,Time[i]))

    T = int(input("Choose Your Time : "))

    print("-------------------------------------------------------------------------------------------------------")
    c = int(input("How many Tickets You want : "))
    print("\n-----------------------------------------Class Menu-----------------------------------------------")
    print("1. Couple Class")
    print("2. First class")
    print("3. Club")

    Type = int(input("Choose your Class : "))

    print("------------------------------------------------------Seats Menu------------------------------------------------------------------------")

    viewSeats()

    seatList = []
    for i in range(c,0,-1):
        print("\nChoose your Seat : ")
        Coloumn = int(input("Enter the Coloumn Index: "))
        Row = int(input("Enter the Row Index: "))
        seat = "C"+str(Coloumn)+","+str(Row)
        seatList.append(seat)
        obj2 = Theater(name=name, count=c,Time=Time[T], date=Date, coloumn=Coloumn, row=Row, Type=Type, MovieName=MovieName)

        releasedate = random.randint(1,28)
        if Date == releasedate:
            obj2.am+=200
        else:
            pass
        
        if(obj2.seatCheck()):
            obj2.payGenerator()
            updateData(obj2.c,"'Filled'",obj2.r)
            if(i>1):
                print("Choose Next Seat")
        else:
            print("Seat is not available")


    sl =""
    for i in range(0,len(seatList)):
        sl=sl+" "+seatList[i]

    obj2.sl=sl
    obj2.Ticket()
        














    




    



import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="@Siva8124",
  database="mydatabase"
)

Cursor = mydb.cursor()

TableName = "OnlineTicketTable"
Cursor.execute("DROP TABLE IF EXISTS %s"%(TableName))
Cursor.execute("""CREATE TABLE IF NOT EXISTS %s (ID int, C1 VARCHAR(50), C2 VARCHAR(50), C3 VARCHAR(50), C4 VARCHAR(50),C5 VARCHAR(50), C6 VARCHAR(50) )"""%(TableName))

Coloumns = "ID, C1, C2, C3, C4, C5, C6"

val = "available"

def upload(Coloumns,val):
    for i in range(1,7):
        Cursor.execute("INSERT INTO OnlineTicketTable (%s) VALUES (%d,'%s','%s','%s','%s','%s','%s')"%(Coloumns,i,val,val,val,val,val,val))

upload(Coloumns,val)

mydb.commit()

def viewSeats():
    Cursor.execute("SELECT * FROM OnlineTicketTable")
    for i in Cursor:
        print(i)

def Fetch(column, INDEX):
    Cursor.execute("SELECT %s FROM OnlineTicketTable WHERE ID=%d"%(column,INDEX))
    for i in Cursor:
        i = str(i)
        i = i[1:len(i)-2]
        return(i)

def updateData(coloumn, value, INDEX):
    Cursor.execute("UPDATE OnlineTicketTable SET %s=%s where ID=%d"%(coloumn,value,INDEX))
    mydb.commit()



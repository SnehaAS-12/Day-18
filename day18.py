#Create a DB with doctor and doctor ID & patients visited
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="1234",
  database="Doctors"
)
dbse = mydb.cursor()
dbse.execute("CREATE TABLE Doctors(dr_id VARCHAR(255), Patient_visited VARCHAR(255))")
dbse = mydb.cursor()
sql = "INSERT INTO Doctors(dr_id , Patient_visited) VALUES (%s,%s)"
val = [  ('D1','15'), ('D3','6'), ('D5','2'),('D4','1'),('D13','9'),('D2','6'),('D8','3'),('D6','0'),('D23','15'),('D42','9'),('D33','0'),('D41','0'), ('D53','19'),('D77','7'),('D28','0'),('D19','4')    ]


#Get the doctors who have more than 5 patients visited
dbse.executemany(sql, val)
mydb.commit()
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Doctors where Patient_visited >5")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
  
  
#Get the doctors with no patients visit
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Doctors where Patient_visited=0")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
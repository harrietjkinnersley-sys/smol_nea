# report login


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()





def login(): 
    entry = input("enter username: ")
    if entry == SELECT * FROM "usernames:" WHERE values = entry:
      else print("ACCESS DENIED")
    
    pass = input("Enter password: ")
    if pass == SELECT * FROM "passwords" WHERE values = pass :
        else print("ACCESS DENIED")
    

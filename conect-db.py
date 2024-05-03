import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="blugin",
    password="135426@blugin",
    database="blugin_db"
    
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM categoria")

myresult = mycursor.fetchall()

for row in myresult:
    print(row)

mydb.close()
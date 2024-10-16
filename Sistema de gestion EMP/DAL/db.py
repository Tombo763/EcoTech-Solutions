import mysql.connector

cnx = mysql.connector.connect(
    user='root', 
    password='',
    host='127.0.0.1',
    database='biblioteca')
    
cursor = cnx.cursor()
cursor.execute('Select * from editorial')
    #cursor.execute("SHOW DATABASES") # Comando usado para testear la conexión, OK
for base in cursor:
    print(base)
cnx.close()
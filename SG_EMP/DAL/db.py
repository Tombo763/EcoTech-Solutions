import mysql.connector
def connector():

    global cursor
    cnx = mysql.connector.connect(
        user='root', 
        password='',
        host='127.0.0.1',
        database='ecotech solutions')
    

    cursor = cnx.cursor()
    cursor.execute()
    for base in cursor:
        print (base)
    cnx.close()
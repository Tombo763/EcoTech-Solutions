import mysql.connector


def connector():
            
        connection = mysql.connector.connect(
            user='root',
            password='',
            host='127.0.0.1',
            database='ecotech solutions'
        )
        if connection.is_connected():
                print("Conexión exitosa a la base de datos.")
                return connection
        
        
        





#cursor = cnx.cursor()
    
    
    
    
#for base in cursor:
 #       print (base)
 #   cnx.close()

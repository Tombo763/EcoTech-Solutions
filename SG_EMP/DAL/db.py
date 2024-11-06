import mysql.connector




def connector():
    
    
    cnx = mysql.connector.connect(
        user='root', 
        password='',
        host='127.0.0.1',
        database='ecotech solutions')
    
    return cnx
    


#cursor = cnx.cursor()
    
    
    
    
#for base in cursor:
 #       print (base)
 #   cnx.close()

def consulta_1():
    
    consulta1 =('''select * from empleados''')

    return consulta1




def consulta_2(usuario):
    new_user=[]
    for dato in usuario:
        new_user.append(dato)
    consulta2=(f"""inserti into usuarios (nombre,correo,username,contraseña) 
               values({[0]},{[1]},{[2]},{[3]});
               
               """) 


    return consulta2
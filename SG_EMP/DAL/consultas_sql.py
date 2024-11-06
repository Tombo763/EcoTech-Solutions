from DAL.db import connector
cursor=connector().cursor()

def consulta_1():
    
    cursor.execute('''select * from empleados;''')

    emps=cursor.fetchall
    cursor.close()
    return emps



def consulta_2(nombre,fecha_nac,fecha_contrato,
              salario,correo,phono,direccion,rut,contraseña):
    
        
    cursor.execute(f"""insert into usuarios (NOMBRE,FECHA_NAC,
                        FECHA_CONTRATO,SALARIO,CORREO,TELEFONO,DIRECCION,
                        RUT,CONTRASENA) 
               values({nombre,fecha_nac,fecha_contrato,
              salario,correo,phono,direccion,rut,contraseña});
               
               """) 
    cursor.execute(F'select *from empleados where NOMBRE={nombre},TELEFONO={phono},CORREO={correo};')
    nuevo=cursor.fetchall
    cursor.close()
    return nuevo


def consulta_3(campo,atributo,mod_id):


    cursor.execute(f'update empleados set {campo}={atributo} where ID_EMPLEADO={mod_id};')
    
    cursor.execute(f'select ID_EMPLEADO,{campo} from empleados where ID_EMPLADO={mod_id};')
    val_modificado=cursor.fetchall
    cursor.close()
    return val_modificado



def consulta_4():

    cursor.execute('select ID_EMPLEADO from empleados;')
    id_emps=list(cursor.fetchall)
    cursor.close
    return id_emps


def consulta_5(id_emp_delete):

    cursor.execute(F"DELETE from empleados where ID_EMPLEADO in {id_emp_delete}")
    cursor.close()
#Aquí se desarrolla el codigo como tal

import re
from getpass import getpass
from SG_EMP.DAL.db import connector
from SG_EMP.Clases.empleados import Empleados

valid_mail = re.compile(r"([\w\d.-_]+)@([\w]+).([\w]+)")
usuarios=[]
id_emp=0
list_usuarios=[]
list_password=[]
consulta=[1,2,3,4,5]
conexion=connector()
cursor=conexion.cursor()

def menuinicio():
    print("================================")
    print("       M E N Ú  I N I C I O     ")
    print("================================")
    print("       1.- INICIAR SECION       ")
    print("       2.- CREAR SECION         ")
    print("       3.- Salir                ")
    print("================================")


def crear_secion():
    usuario=[]
    print("================================")
    print("           SING IN              ")
    print("================================")
    
    nombre=input(" ingrese su nombre: ")
    while not len(nombre):
        print('el campo nombre es obligatorio')
        nombre=input(" ingrese su nombre: ")
    usuario.append(nombre)

    correo=input(" ingrese su correo: ")
    while not len(valid_mail.findall(correo)):
        print("la direccion de correo no es valida")
        correo = input("INGRESE CORREO: ")
    usuario.append(correo)

    nom_usuario=input("ingrese su nombre de usuario: " )
    while not len(nom_usuario):
         print('el campo nombre es obligatorio')
         nom_usuario=input("ingrese su nombre de usuario: " )
    usuario.append(nom_usuario)


    contraseña=getpass(" ingrese su contraseña: minimo de 8 caracteres ")
    while not len(contraseña) or len(contraseña)< 8:
        print('la contraseña no es valida')
    usuario.append(contraseña)
    
    connector(consulta[1])
    id_usuario=+1
    usuarios.update({id_usuario:usuario})


    print("================================")



def inicio_secion():
    print("================================")
    print("             LOGIN              ")
    print("================================")

    nombre_user=input("  NOMBRE DE USUARIO: ")
    while nombre_user not  in list_usuarios:
        print ("este usuario no existe")
        nombre_user=input("  NOMBRE DE USUARIO: ")
    
    password=getpass(" CONTRASEÑA: ")
    while password not in  list_password:
        print (" CONTRASEÑA INCORRECTA")
        password=getpass(" CONTRASEÑA: ")


    
    print("================================")




def menuprincipal():
    print("================================")
    print("   M E N Ú  P R I N C I P A L   ")
    print("================================")
    print("       1.- (C) INGRESAR         ")
    print("       2.- (R) MOSTRAR          ")
    print("       3.- (U) MODIFICAR        ")
    print("       4.- (D) ELIMINAR         ")
    print("       5.- (E) Salir            ")
    print("================================")



def menu_datos():
    print("=====================================")
    print("         SELECIONE DATOS             ")
    print("=====================================")
    print("        1.- EMPLEADOS                ")
    # print("        2.- DEPARTAMENTOS            ")
    # print("        3.- PROYECTOS                ")
    # print("        4.- INFORME                  ")    
    print("        2.- VOLVER                   ")
    print("=====================================")



def menu_num_datos():
    print("=====================================")
    print("           MOSTRAR  DATOS            ")
    print("=====================================")
    print("        1.- MOSTRAR TODOS            ")
    #print("        2.- MOSTRAR UNO              ")
    #print("        3.- MOSTRAR PARCIAL          ")
    print("        2.- VOLVER                   ")
    print("=====================================")



def mod_departamentos():
    print("================================")
    print("     MODIFICAR DEPARTAMENTO     ")
    print("================================")
    print("       1.- NOMBRE               ")
    print("       2.- VOLVER               ")
    print("================================")


def ingreso_empleados():
    empleado=[]
    print("================================")
    print("       INGRESAR EMPLEADO        ")
    print("================================")
    nombre=input('Nombre: ')
    while not len (nombre):
        print('campo necesario')
        nombre=input('Nombre: ')
    empleado.append(nombre) #[0]
    
    fecha_nac=input('Fecha Nacimiento: ')
    while not len(fecha_nac):
        print('campo necesario')
    empleado.append(fecha_nac) #[1]

    fecha_contrato=input('Fecha Contrato: ')
    while not len(fecha_contrato):
        print('campo necesario')
        fecha_contrato=input('Fecha Contrato: ')
    empleado.append(fecha_contrato) #[2]


    salario=int(input('Salario: $'))
    while not len(salario):
        print('campo necesario')
        salario=int(input('Salario: $'))
    empleado.append(salario) #[3]

    correo=input('correo: ')
    while not re.fullmatch(valid_mail,correo):
        print('correo no es valido')
        correo=input('correo: ')
    empleado.append(correo) #[4]
    
    
    
    phono=int (input('Telefono: '))
    while not len(phono) or len(phono)!=9:
        print('nunero de telefono no valido')
        phono=int (input('Telefono: '))
    empleado.append(phono) #[5]


    direccion=input('diereccion:  ')   
    while not len (direccion):
        print('campo necesario')
        direccion=input('diereccion:  ') 
    empleado.append(direccion) #[6]
    
    ch_rut=['1','2','3','4','5','6','7','8','9','0','k']
    rut=input('RUT:  ')
    while rut not in ch_rut or len(rut)!=9:
        print('el rut no es valido') 
        rut=input('RUT:  ')
    empleado.append(rut) #[7]


    contraseña=getpass('Contraseña:    ')
    while len(contraseña)<8:
        print('la contraseña es muy corta')
        contraseña=getpass('Contraseña:    ')
    empleado.append(contraseña) #[8]

    id_emp=+1
    empleado = Empleados(id_emp,empleado[0],empleado[1],empleado[2],empleado[3],
                         empleado[4],empleado[5],empleado[6],empleado[7],empleado[8])
    
    cursor.execute(F'''insert into empleados (NOMBRE,FECHA_NAC,FECHA,CONTRATO,
                   SALARIO,CORREO,TELEFONO,DIRECCION,RUT,CONTRASEÑA) 
                   values ({empleado[0]},{empleado[1]},{empleado[2]},{empleado[3]},
                   {empleado[4]},{empleado[5]},{empleado[6]},{empleado[7]},{empleado[8]})''')
    print("================================") 


def mod_empleados():
    print("================================")
    print("       MODIFICAR EMPLEADO       ")
    print("================================")
    print("       1.- NOMBRE               ")
    print("       2.- FECHA NACIMIENTO     ")
    print("       3.- FECHA CONTRATO       ")
    print("       4.- SALARIO              ")
    print("       5.- CORREO               ")
    print("       6.- TELEFONO             ")
    print("       7.- DIRECCION            ")
    print("       8.- RUT                  ")
    print("       9.- CONTRASEÑA           ")
    print("      10.- VOLVER               ")
    print("================================")    



def mod_proyecto():
    print("================================")
    print("       MODIFICAR PROYECTO       ")
    print("================================")
    print("       1.- NOMBRE               ")
    print("       2.- DESCRIPCION          ")
    print("       3.- FECHA DE INICIO      ")
    print("       4.- FECHA DE LIMITE      ")
    print("       5.- VOLVER               ")
    print("================================")

def mod_informe():
    print("===============================")
    print("       MODIFICAR INFORME       ")
    print("===============================")
    print("       1.- FECHA               ")
    print("       2.- REPORTE             ")
    print("       3.- VOLVER              ")
    print("===============================")    

def leer_tabla_emp():
    cursor.execute('select *from  empleados;')
    resultado=cursor.fetchall
    return resultado

while True:     
    op_1=['1','2','3','4','5']
    opciones_2=['1','2']
    opciones_mostrar=['1','2']



    menuprincipal()
    op_menuprincipal=int(input('engrese su eleccion: '))
    while op_menuprincipal not in op_1:
        print('esta opcio no existe')
        op_menuprincipal=int(input('engrese su eleccion: '))

    if op_menuprincipal=='1':  # ingresar
        menu_datos()
        op_menu_datos=input('elija el tipo de dato que quiere ingresar: ')
        while op_menu_datos not in opciones_2:
            print('esta opcion no existe')
            op_menu_datos=input('elija el tipo de dato que quiere ingresar: ')


        if op_menu_datos=='1':
            ingreso_empleados()
        else:
            continue


    elif op_menuprincipal=='2': # mostrar
        menu_datos()
        op_mostrar_data=input('elija el tipo de dato que quiere ver')
        while op_mostrar_data not in opciones_2:
            print('esta opcion no existe')
            op_mostrar_data=input('elija el tipo de dato que quiere ver')


        menu_num_datos()
        op_mostrar=input('¿quiere mostrar todos los campos o volver?')
        while op_mostrar not in opciones_mostrar:
            print('esta opcion no existe')
            op_mostrar=input('¿quiere mostrar todos los campos o volver?')


        if op_mostrar =='1':
            for fila in leer_tabla_emp():
                print(fila)
        else:
            continue
    
    elif op_menuprincipal=='3': # modificar
        menu_datos()
        op_mod=input('elija el tipo de dato que quiere modificar')
        while op_mod not in opciones_2:
            print('esta opcion no existe')
        mod_empleados()

    
    elif  op_menuprincipal=='4': # eliminar
        menu_datos()   




    else :
        break    
    
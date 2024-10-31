#Aquí se desarrolla el codigo como tal
import mysql.connector
import re
from getpass import getpass
from 



valid_mail = re.compile(r"([\w\d.-_]+)@([\w]+).([\w]+)")
usuarios={}
id_usuario=0


def connector(consulta):

    cnx = mysql.connector.connect(
        user='root', 
        password='',
        host='127.0.0.1',
        database='ecotech solutions')
    cursor = cnx.cursor()
    cursor.execute(consulta)
    return cursor

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

    id_usuario=+1
    usuarios.update({id_usuario:usuario})


    print("================================")



def inicio_secion():
    print("================================")
    print("             LOGIN              ")
    print("================================")
    nombre_user=input("  NOMBRE DE USUARIO: ")
    
    
    
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
    print("        1.- DEPARTAMENTOS            ")
    print("        2.- EMPLEADOS                ")
    print("        3.- PROYECTOS                ")
    print("        4.- INFORME                  ")    
    print("        5.- VOLVER                   ")
    print("=====================================")



def menu_num_datos():
    print("=====================================")
    print("           MOSTRAR  DATOS            ")
    print("=====================================")
    print("        1.- MOSTRAR TODOS            ")
    print("        2.- MOSTRAR UNO              ")
    print("        3.- MOSTRAR PARCIAL          ")
    print("        4.- VOLVER                   ")
    print("=====================================")



def mod_departamentos():
    print("================================")
    print("     MODIFICAR DEPARTAMENTO     ")
    print("================================")
    print("       1.- NOMBRE               ")
    print("       2.- VOLVER               ")
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


while True:
    opciones1=[1,2,3]
    menuinicio()
    op_inicio=input("ingrese opcion:  ")
    while op_inicio not in opciones1:
        print ('opcion no existe por favor intente de nuevo')
        op1=int(input("ingrese opcion :  "))
    if op_inicio == 1:
        pass

        
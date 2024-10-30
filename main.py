#Aquí se desarrolla el codigo como tal
import mysql.connector
import re
from getpass import getpass
valid_mail = re.compile(r"([\w\d.-_]+)@([\w]+).([\w]+)")


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
    print("       5.- VOLVER                ")
    print("================================")

def mod_informe():
    print("===============================")
    print("       MODIFICAR INFORME       ")
    print("===============================")
    print("       1.- FECHA               ")
    print("       2.- REPORTE             ")
    print("       3.- VOLVER              ")
    print("===============================")    

def connector():
    global cursor
    cnx = mysql.connector.connect(
        user='root', 
        password='',
        host='127.0.0.1',
        database='ecotech solutions')
    cursor= cnx.cursor()


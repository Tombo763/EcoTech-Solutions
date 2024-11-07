#Aquí se desarrolla el codigo como tal

import re
from getpass import getpass

from DAL.consultas_sql import consulta_1,consulta_3,consulta_4,consulta_5
from rut_chile import rut_chile
from Clases.empleados import Empleados

valid_mail = re.compile(r"([\w\d.-_]+)@([\w]+).([\w]+)")
valid_date=re.compile(r"DD/MM/AAAA")
usuarios=[]
id_emp=consulta_4()
list_usuarios=[]
list_password=[]
consulta=[1,2,3,4,5]

ch_rut=['1','2','3','4','5','6','7','8','9','0','k']

def menuinicio():
    print("================================")
    print("       M E N Ú  I N I C I O     ")
    print("================================")
    print("       1.- INICIAR SESION       ")
    print("       2.- CREAR SESION         ")
    print("       3.- Salir                ")
    print("================================")


def crear_sesion():
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
    
    print("================================")
    print("       INGRESAR EMPLEADO        ")
    print("================================")
    nombre=input('Nombre: ')
    while not len (nombre):
        print('campo necesario')
        nombre=input('Nombre: ')
    
    
    fecha_nac=input('Fecha Nacimiento: ')
    while not len(fecha_nac):
        print('campo necesario')
    

    fecha_contrato=input('Fecha Contrato: ')
    while not len(fecha_contrato):
        print('campo necesario')
        fecha_contrato=input('Fecha Contrato: ')
    


    salario=int(input('Salario: $'))
    while not len(salario):
        print('campo necesario')
        salario=int(input('Salario: $'))
    

    correo=input('correo: ')
    while not re.fullmatch(valid_mail,correo):
        print('correo no es valido')
        correo=input('correo: ')
    
    
    
    
    phono=int (input('Telefono: '))
    while not len(phono) or len(phono)!=9:
        print('nunero de telefono no valido')
        phono=int (input('Telefono: '))
    


    direccion=input('diereccion:  ')   
    while not len (direccion):
        print('campo necesario')
        direccion=input('diereccion:  ') 
    
    
    rut=input('RUT:  ')
    while rut_chile.is_valid_rut(rut) is False:
        print('el rut no es valido') 
        rut=input('RUT:  ')
    


    contraseña=getpass('Contraseña:    ')
    while len(contraseña)<8:
        print('la contraseña es muy corta')
        contraseña=getpass('Contraseña:    ')
    

    id_emp2=int(id_emp[-1])
    id_emp2=+1
    empleado=Empleados(id_emp2,nombre,fecha_nac,fecha_contrato,
              salario,correo,phono,direccion,rut,contraseña)
    
    #consulta_2(nombre,fecha_nac,fecha_contrato,
     #         salario,correo,phono,direccion,rut,contraseña)
    if Empleados.validar_datos(empleado) is False:
        print ("listo")
    


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

def menu_delt_dato():
    
    print("=====================================")
    print("           ELIMINAR DATOS            ")
    print("=====================================")
    print("        1.- ELIMINAR UNO              ")
    print("        2.- ELIMINAR PARCIAL          ")
    print("        3.- VOLVER                   ")
    print("=====================================")



while True:     
    op_1=['1','2','3','4','5']
    opciones_datos=['1','2']
    opciones_mostrar=['1','2']
    opciones_modificar=['1','2','3','4','5','6','7','8','9','10']


    menuprincipal()
    op_menuprincipal=int(input('engrese su eleccion: '))
    while op_menuprincipal not in op_1:
        print('esta opcio no existe')
        op_menuprincipal=int(input('engrese su eleccion: '))

    if op_menuprincipal=='1':  # ingresar
        menu_datos()
        op_menu_datos=input('elija el tipo de dato que quiere ingresar: ')
        while op_menu_datos not in opciones_datos:
            print('esta opcion no existe')
            op_menu_datos=input('elija el tipo de dato que quiere ingresar: ')


        if op_menu_datos=='1':
            ingreso_empleados()
        else:
            continue


    elif op_menuprincipal=='2': # mostrar
        menu_datos()
        op_mostrar_data=input('elija el tipo de dato que quiere ver')
        while op_mostrar_data not in opciones_datos:
            print('esta opcion no existe')
            op_mostrar_data=input('elija el tipo de dato que quiere ver')
        if op_mostrar_data=='2':
            continue
        


        menu_num_datos()
        op_mostrar=input('¿quiere mostrar todos los campos o volver?')
        while op_mostrar not in opciones_mostrar:
            print('esta opcion no existe')
            op_mostrar=input('¿quiere mostrar todos los campos o volver?')


        if op_mostrar =='1':
            for fila in consulta_1():
                print(fila)
        else:
            continue
    
    elif op_menuprincipal=='3': # modificar
        menu_datos()
        op_mod_data=input('elija el tipo de dato que quiere modificar')
        while op_mod_data not in opciones_datos:
            print('esta opcion no existe')
            op_mod_data=input('elija el tipo de dato que quiere modificar')
        if op_mod_data=='2':
            continue
        
        
        for fila in consulta_1():
                print(fila)
        
        id_mod_emp=input('ingresa el ID del empleado que quieres modificar')
        while id_mod_emp not in consulta_4:
            print('no hay un empleado con este ID')
            id_mod_emp=input('ingresa el ID del empleado que quieres modificar')

        mod_empleados()
        op_mod=input('elija que atributo quiere cambiar o vuelve')
        
        
        while True:

            while op_mod not in opciones_modificar:
                print ('no existe esta opcion')
                op_mod=input('elija que atributo quiere cambiar o vuelve')

            campos=['NOMBRE','FECHA_NAC','FECHA_CONTRATO','SALARIO','CORREO','TELEFONO','DIRECCION','RUT','CONTRASEÑA']
            if op_mod=='1':
                nuevo_nom=input('ingrese el nuevo nombre')
                while not len(nuevo_nom):
                    print('campo nesesario')
                    nuevo_nom=input('ingrese el nuevo nombre')
                vew_nombre=consulta_3(campos[0],nuevo_nom,id_mod_emp)
                print(vew_nombre)
                continue           
            elif op_mod=='2':
                print('siga este formato DD/MM/AAAA')
                nueva_fecha_nac=input('ingese la nueva fecha')
                while not re.fullmatch(valid_date,nueva_fecha_nac):
                    print("la fecha ingresada no sigue el formato")
                    nueva_fecha_nac=input('ingese la nueva fecha')
                vew_fecha_nac=consulta_3(campos[1],nueva_fecha_nac,id_mod_emp)
                print(vew_fecha_nac)
                continue

            elif op_mod=='3':
                print('siga este formato DD/MM/AAAA')
                fecha_contrato=input('ingese la nueva fecha')
                while not re.fullmatch(valid_date,fecha_contrato):
                    print("la fecha ingresada no sigue el formato")
                    fecha_contrato=input('ingese la nueva fecha')
                vew_fecha_contrato=consulta_3(campos[2],fecha_contrato,id_mod_emp)
                print(vew_fecha_contrato)
                continue

            elif op_mod=='4':
                    while True:
                        try:    
                            nuevo_salario=int(input('ingrese el nuevo salario'))
                            vew_salario=consulta_3(campos[3],nuevo_salario,id_mod_emp)
                            print('$',vew_salario)
                        except ValueError:
                                print('salario no valido')                       
                                continue



            elif op_mod=='5':
                nuevo_correo=input('ingrese el nuevo correo')
                while not re.fullmatch(valid_mail,nuevo_correo):
                    print('el correo no es valido')
                    nuevo_correo=input('ingrese el nuevo correo')
                vew_correo=consulta_3(campos[4],nuevo_correo,id_mod_emp)
                print(vew_correo)
                continue



            elif op_mod=='6':
                chr_fono=['0','1','2','3','4','5','6','7','8','9']
                nuevo_telefono=input('ingrese nuevo telefono')
                while nuevo_telefono not in chr_fono:
                   print('telefono no valido')
                   nuevo_telefono=input('ingrese nuevo telefono')
                vew_fono=consulta_3(campos[5],nuevo_telefono,id_mod_emp)  
                print(vew_fono)
                continue  
            
            elif op_mod=='7':
                
                nueva_direccion=input('ingrese nueva direccion')
                vew_direccion=consulta_3(campos[6],nueva_direccion,id_mod_emp)
                print(vew_direccion)            


            elif op_mod=='8':
                nuevo_rut=input('ingrese el nuevo RUT')
                while rut_chile.is_valid_rut(nuevo_rut) is False:
                    print('RUT no valido')
                    nuevo_rut=input('ingrese el nuevo RUT')
                vew_rut=consulta_3(campos[7],nuevo_rut,id_mod_emp)


            elif op_mod=='9':
                simbolos=['#','@','-']
                match=0
                print('la contraseña debe tener al menos 8 caracteres y un minimo de 1 simbolo (#,@,-)')
                nueva_contraseña=input('ingrese la nueva contraceña')
                for chr in nueva_contraseña:
                    if chr in simbolos:
                        math=+1
                while len(nueva_contraseña)<8 and match<1:
                    print('contraseña no valida')
                    print('la contraseña debe tener al menos 8 caracteres y un minimo de 1 simbolo (#,@,-)')
                    nueva_contraseña=input('ingrese la nueva contraceña')
                vew_contraseña=consulta_3(campos[8],nueva_contraseña,id_mod_emp)


            else:

                break  

    
    elif  op_menuprincipal=='4': # eliminar
        menu_datos()
        op_delt=input('elija el tipo de dato que quiere eliminar')
        while op_delt not in opciones_datos:
            print('no existe esta opcion')
            op_delt=input('elija el tipo de dato que quiere eliminar')
        if op_mod_data=='2':
            continue
        menu_delt_dato()
        ops_del=["1","2","3"]
        numero_del=input("elija una de las opciones")
        while numero_del not in ops_del:
            print('esta opcion no existe') 
            numero_del=input("elija una de las opciones")

        id_empleado=[]
        if numero_del=="1":
            for fila in consulta_1:
                print (fila)
            id_delt=input('ingrese el ID del empleado que quiere eliminar')
            while id_delt not in consulta_4:
                print ('ID noo existe')
                id_delt=input('ingrese el ID del empleado que quiere eliminar')
            id_empleado.append(id_delt)
            consulta_5(id_empleado)

        elif numero_del=="2":
            ops_num_parcial=["1","2"]
            while True:
                for fila in consulta_1:
                    print (fila)
                id_delt=input('ingrese el ID del empleado que quiere eliminar')
                while id_delt not in consulta_4:
                    print ('ID noo existe') 
                    id_delt=input('ingrese el ID del empleado que quiere eliminar')
                
                num_parcial=input("si quiere eliminar otro empleado ingrese 1 si quiere terminar ingese 2")
                while num_parcial not in ops_num_parcial:
                    print('esta opcion no existe')
                    num_parcial=input("si quiere eliminar otro empleado ingrese 1 si quiere terminar ingese 2")
                if num_parcial=='1':
                    id_empleado.append(id_delt)
                else:
                    consulta_5(id_empleado)
                    break



        else:     
            continue

    else :
        break    
    
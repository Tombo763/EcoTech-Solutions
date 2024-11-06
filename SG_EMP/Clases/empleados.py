
from Clases.roles import Roles
from Clases.tipo_empleado_emp import Tipo_empleado_emp
from getpass import getpass
#from DAL.db import connector
import re
valid_mail = re.compile(r"([\w\d.-_]+)@([\w]+).([\w]+)")

class Empleados(Roles,Tipo_empleado_emp):
    id_empleado: int
    def __init__(self,id_empleado= 0,nombre_empleado='',fecha_nacimiento='',fecha_contrato='',
               salario=0,correo='',telefono='',
               direccion='',rut='',password='',id_tipo_empleado_emp=0,id_rol=0):

        self.id_empleado=id_empleado
        self.nombre_empleado=nombre_empleado
        self.fecha_nacimmiento=fecha_nacimiento
        self.fecha_contrato=fecha_contrato
        self.salario=salario
        self.correo=correo
        self.telefono=telefono
        self.direcciom=direccion
        self.rut=rut
        self.password=password
        self.id_tipo_empleado_emp=id_tipo_empleado_emp
        self.id_rol=id_rol


    def validar_datos(self):

        if re.fullmatch(valid_mail,self.correo):
            return True
        else:
            return False
    


    def habilitar_modulos():
        
        pass


    def encriptacion(self):
        contraseña=getpass(self.password) 
        return contraseña
        pass

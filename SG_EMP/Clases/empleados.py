import modulos
import roles
import tipo_empleado_emp
from getpass import getpass
from DAL.db import connector

import re
valid_mail = re.compile(r"([\w\d.-_]+)@([\w]+).([\w]+)")

class Empleados(modulos,roles,tipo_empleado_emp):
    def _init_(self,id_empleado,nombre_empleado,fecha_nacimiento,fecha_contrato,salario,correo,telefono,
               direccion,rut,id_tipo_empleado_emp,id_rol,id_modulo,password):
        tipo_empleado_emp.Tipo_empleado_emp.__init__(id_tipo_empleado_emp)
        roles.Roles.__init__(id_rol)
        modulos.Modulos.__init__(id_modulo)
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

    def validar_datos(mail):
        re.match(valid_mail,mail) is not None
        
        pass


    def habilitar_modulos():
        
        pass


    def encriptacion(self,contraseña):
        connector()
        self.password=getpass(contraseña) 
        pass

import Modulos
import Roles
import Tipo_empleado_emp

class empleados:
    def _init_(self,id_empleado,nombre_empleado,fecha_nacimiento,fecha_contrato,salario,correo,telefono,
               direccion,rut,id_tipo_empleado_emp,id_rol,id_modulo,password):
        super(Tipo_empleado_emp)._init_(id_tipo_empleado_emp)
        super(Roles)._init_(id_rol)
        super(Modulos)._init_(id_modulo)
        self.id_empleado=id_empleado
        self.nombre_empleado=nombre_empleado
        self.fecha_nacimmiento=fecha_nacimiento
        self.fecha_contrato=fecha_contrato
        self.direcciom=direccion
        self.rut=rut
        self.password=password

    def validar_datos():
        pass


    def habilitar_modulos():
        pass


    def encriptacion():
        pass
import empleados
class Departamento(empleados):
    def __init__(self,id_departamento,nombre_departamento,id_empleado):
        empleados.Empleados.__init__(id_empleado)
        self.id_departamento=id_departamento
        self.nombre_departamento=nombre_departamento

from Clases.empleados import Empleados
class Departamento(Empleados):
    def __init__(self,id_departamento,nombre_departamento,id_empleado):
        Empleados.__init__(id_empleado)
        self.id_departamento=id_departamento
        self.nombre_departamento=nombre_departamento

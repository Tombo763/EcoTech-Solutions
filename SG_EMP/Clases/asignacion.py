from Clases.empleados import Empleados
from Clases.departamento import Departamento

class Asignacion(Empleados,Departamento):
    def __init__(self,id_asignacion=0,id_departamento=0,id_empleado=0):
        Empleados.__init__(id_empleado)
        Departamento.__init__(id_departamento)
        self.id_asignacion=id_asignacion
    
    def validar_asignacion():
        pass


    def asignacion():
        pass

    
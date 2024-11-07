from Clases.empleados import Empleados
from Clases.proyecto import Proyecto

class Proyecto_empleado(Empleados,Proyecto):
    def __init__(self,id_proyecto_empleado,id_empleado,id_proyecto):
        Empleados.__init__(id_empleado)
        Proyecto.__init__(id_proyecto)
        self.id_proyecto_empleado=id_proyecto_empleado

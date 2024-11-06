import empleados
import proyecto

class Proyecto_empleado(empleados,proyecto):
    def __init__(self,id_proyecto_empleado,id_empleado,id_proyecto):
        empleados.Empleados.__init__(id_empleado)
        proyecto.Proyecto.__init__(id_proyecto)
        self.id_proyecto_empleado=id_proyecto_empleado

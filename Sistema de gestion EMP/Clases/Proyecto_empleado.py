import empleados
import proyecto
#wena shoro
class Proyecto_empleado(empleados,proyecto):
    def _init_(self,id_proyecto_empleado,id_empleado,id_proyecto):
        empleados.Empleados.__init__(id_empleado)
        proyecto.Proyecto.__init__(id_proyecto)
        self.id_proyecto_empleado=id_proyecto_empleado
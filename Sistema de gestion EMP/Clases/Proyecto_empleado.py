import Empleados
import Proyecto

class proyecto_empleado:
    def _init_(self,id_proyecto_empleado,id_empleado,id_proyecto):
        super(Empleados)._init_(id_empleado)
        super(Proyecto)._init_(id_proyecto)
        self.id_proyecto_empleado=id_proyecto_empleado
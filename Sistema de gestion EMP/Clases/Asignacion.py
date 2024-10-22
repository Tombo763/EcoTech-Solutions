import empleados
import departamento

class Asignacion(empleados,departamento):
    def _init_(self,id_asignacion,id_departamento,id_empleado):
        empleados.Empleados.__init__(id_empleado)
        departamento.Departamento.__init__(id_departamento)
        self.id_asignacion=id_asignacion
    
    def validar_asignacion():
        pass


    def asignacion():
        pass
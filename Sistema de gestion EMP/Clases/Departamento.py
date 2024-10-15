import Empleados
class departamento:
    def _init_(self,id_departamento,nombre_departamento,id_empleado):
        super(Empleados)._init_(id_empleado)
        self.id_departamento=id_departamento
        self.nombre_departamento=nombre_departamento
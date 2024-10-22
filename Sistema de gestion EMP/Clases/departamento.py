import empleados
class Departamento(empleados):
    def _init_(self,id_departamento,nombre_departamento,id_empleado):
        super()._init_(id_empleado)
        self.id_departamento=id_departamento
        self.nombre_departamento=nombre_departamento

from Clases.tipo_empleado import Tipo_empleado

class Tipo_empleado_emp(Tipo_empleado):
    def __init__(self,id_tipo_empleado_emp=0,id_tipo_empleado=0):
        Tipo_empleado.__init__(id_tipo_empleado)
        self.id_tipo_empleado_emp=id_tipo_empleado_emp

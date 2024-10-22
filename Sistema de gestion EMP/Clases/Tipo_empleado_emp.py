import tipo_empleado

class Tipo_empleado_emp(tipo_empleado):
    def _init_(self,id_tipo_empleado_emp,id_tipo_empleado):
        super().__init__(id_tipo_empleado)
        self.id_tipo_empleado_emp=id_tipo_empleado_emp
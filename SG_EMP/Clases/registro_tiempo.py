
from Clases.proyecto_empleado import Proyecto_empleado

class Registro_tiempo(Proyecto_empleado):
    def __init__(self,id_registro_tiempo,fecha_registro,cantidad_horas,
               descripcion,id_proyecto_empleado,hora_extra,observacion):
        super().__init__(id_proyecto_empleado)
        self.id_registro_tiempo=id_registro_tiempo
        self.fecha_registro=fecha_registro
        self.cantidad_horas=cantidad_horas
        self.descripcion=descripcion
        self.hora_extra=hora_extra
        self.observacion=observacion

    def validacion_horas_extra():
        pass    

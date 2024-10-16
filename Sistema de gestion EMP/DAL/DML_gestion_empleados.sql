-- Insertamos registros en la tabla Modulos.
INSERT INTO MODULOS(NOMBRE) 
VALUES
('Gestión de Proyectos'),
('Gestión de Empleados'),
('Generación de Informes');

-----------------------------------------------------------------
INSERT INTO TIPO_EMPLEADO(NOMBRE)
VALUES 
('Administrador'),
('Gerente'),
('Desarrollador');

-----------------------------------------------------------------
INSERT INTO DEPARTAMENTOS(NOMBRE) 
VALUES 
('Recursos Humanos'),
('Tecnología'),
('Finanzas');

-----------------------------------------------------------------
INSERT INTO PROYECTOS(NOMBRE, DESCRIPCION, FECHA_INICIO, FECHA_PLAZO)
VALUES 
('EcoTech App', 'Desarrollo de la app para la gestión de residuos', '2024-01-01', '2024-12-31'),
('Sistema Interno', 'Implementación de sistema de gestión interna', '2024-05-15', '2024-10-15'),
('Automatización Financiera', 'Automatización de procesos financieros', '2024-03-01', '2024-09-01');

-----------------------------------------------------------------
INSERT INTO ROLES(NOMBRE)
VALUES 
('Administrador'),
('Gerente de Proyecto'),
('Empleado');

-----------------------------------------------------------------
INSERT INTO ROL_MODULOS(ID_ROL, ID_MODULO) 
VALUES 
(1, 1),
(1, 2),
(2, 1); 
-----------------------------------------------------------------
INSERT INTO EMPLEADOS (ID_EMPLEADO, NOMBRE, FECHA_NAC, FECHA_CONTRATO, SALARIO, CORREO, TELEFONO, DIRECCION, RUT, CONTRASENA, ID_DEPARTAMENTO, ID_TIPO_EMPLEADO) 
VALUES 
(1, 'Alessandro Olivares', '1990-05-27', '2024-01-15 00:00:00', 500000, 'alessandro_or@hotmail.com', '948758127', 'Av. Esmeralda 1252', '20254360-', 'contraseña12345', 2, 1),
(2, 'Diego Bravo', '1985-08-25', '2024-02-20 00:00:00', 540000, 'diego.bravo@inacapmail.cl', '987654321', 'Luis durand 045', '23456789-', 'password123*', 1, 2),
(3, 'Pedro Sánchez', '1995-11-15', '2024-03-10 00:00:00', 630000, 'pedro.sanchez@gmail.com', '456789123', 'Los filosofos', '34567890-', 'juanita2413', 3, 3);


------------------------------------------------------------------
INSERT INTO INFORMES(ID_EMPLEADO, FECHA, REPORTE) 
VALUES 
(1, '2024-06-15', 'Informe sobre el progreso del proyecto EcoTech App'),
(2, '2024-07-20', 'Evaluación del desempeño de los empleados'),
(3, '2024-08-10', 'Reporte del sistema financiero automatizado');

-----------------------------------------------------------------
INSERT INTO ASIGNACIONES(ID_EMPLEADO, ID_DEPARTAMENTO) 
VALUES 
(1, 2),
(2, 1),
(3, 3); 

-----------------------------------------------------------------
INSERT INTO EMPLEADO_ROL(ID_EMPLEADO, ID_ROL) 
VALUES 
(1, 1),
(2, 2), 
(3, 3); 

-----------------------------------------------------------------
INSERT INTO PROYECTO_EMPLEADO(ID_EMPLEADO, ID_PROYECTO) 
VALUES 
(1, 1),
(2, 2),
(3, 3); 

-----------------------------------------------------------------
INSERT INTO REGISTRO_TIEMPO(FECHA, CANTIDAD_HORAS, DESCRIPCION, ID_PROYECTO_EMPLEADO) 
VALUES 
('2024-07-01', 8, 'Desarrollo de funcionalidades en EcoTech App', 1),
('2024-07-05', 7, 'Planificación de sistema interno', 2),
('2024-07-10', 6, 'Pruebas de automatización financiera', 3);
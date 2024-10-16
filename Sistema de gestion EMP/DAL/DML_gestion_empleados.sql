-- Insertamos registros en la tabla Modulos.
INSERT INTO MODULOS (NOMBRE) VALUES ('Gestión de Proyectos');
INSERT INTO MODULOS (NOMBRE) VALUES ('Gestión de Empleados');
INSERT INTO MODULOS (NOMBRE) VALUES ('Generación de Informes');

-----------------------------------------------------------------
INSERT INTO TIPO_EMPLEADO(NOMBRE) VALUES ('Administrador');
INSERT INTO TIPO_EMPLEADO(NOMBRE) VALUES ('Gerente');
INSERT INTO TIPO_EMPLEADO(NOMBRE) VALUES ('Desarrollador');

-----------------------------------------------------------------
INSERT INTO DEPARTAMENTOS(NOMBRE) VALUES ('Recursos Humanos');
INSERT INTO DEPARTAMENTOS(NOMBRE) VALUES ('Tecnología');
INSERT INTO DEPARTAMENTOS(NOMBRE) VALUES ('Finanzas');

-----------------------------------------------------------------
INSERT INTO PROYECTOS(NOMBRE, DESCRIPCION, FECHA_INICIO, FECHA_PLAZO) VALUES ('EcoTech App', 'Desarrollo de la app para la gestión de residuos', '2024-01-01', '2024-12-31');
INSERT INTO PROYECTOS(NOMBRE, DESCRIPCION, FECHA_INICIO, FECHA_PLAZO) VALUES ('Sistema Interno', 'Implementación de sistema de gestión interna', '2024-05-15', '2024-10-15');
INSERT INTO PROYECTOS(NOMBRE, DESCRIPCION, FECHA_INICIO, FECHA_PLAZO) VALUES ('Automatización Financiera', 'Automatización de procesos financieros', '2024-03-01', '2024-09-01');

-----------------------------------------------------------------
INSERT INTO ROLES(NOMBRE) VALUES ('Administrador');
INSERT INTO ROLES(NOMBRE) VALUES ('Gerente de Proyecto');
INSERT INTO ROLES(NOMBRE) VALUES ('Empleado');

-----------------------------------------------------------------
INSERT INTO ROL_MODULOS(ID_ROL, ID_MODULO) VALUES (1, 1); 
INSERT INTO ROL_MODULOS(ID_ROL, ID_MODULO) VALUES (1, 2); 
INSERT INTO ROL_MODULOS(ID_ROL, ID_MODULO) VALUES (2, 1); 
-----------------------------------------------------------------
INSERT INTO EMPLEADOS (ID_EMPLEADO, NOMBRE, FECHA_NAC, FECHA_CONTRATO, SALARIO, CORREO, TELEFONO, DIRECCION, RUT, CONTRASENA, ID_DEPARTAMENTO, ID_TIPO_EMPLEADO) VALUES (1, 'Alessandro Olivares', '1990-05-27', '2024-01-15 00:00:00', 500000, 'alessandro_or@hotmail.com', '948758127', 'Av. Esmeralda 1252', '20254360-', 'contraseña12345', 2, 1),
INSERT INTO EMPLEADOS (ID_EMPLEADO, NOMBRE, FECHA_NAC, FECHA_CONTRATO, SALARIO, CORREO, TELEFONO, DIRECCION, RUT, CONTRASENA, ID_DEPARTAMENTO, ID_TIPO_EMPLEADO) VALUES (2, 'Diego Bravo', '1985-08-25', '2024-02-20 00:00:00', 540000, 'diego.bravo@inacapmail.cl', '987654321', 'Luis durand 045', '23456789-', 'password123*', 1, 2),
INSERT INTO EMPLEADOS (ID_EMPLEADO, NOMBRE, FECHA_NAC, FECHA_CONTRATO, SALARIO, CORREO, TELEFONO, DIRECCION, RUT, CONTRASENA, ID_DEPARTAMENTO, ID_TIPO_EMPLEADO) VALUES (3, 'Pedro Sánchez', '1995-11-15', '2024-03-10 00:00:00', 630000, 'pedro.sanchez@gmail.com', '456789123', 'Los filosofos', '34567890-', 'juanita2413', 3, 3);


------------------------------------------------------------------
INSERT INTO INFORMES(ID_EMPLEADO, FECHA, REPORTE) VALUES (1, '2024-06-15', 'Informe sobre el progreso del proyecto EcoTech App');
INSERT INTO INFORMES(ID_EMPLEADO, FECHA, REPORTE) VALUES (2, '2024-07-20', 'Evaluación del desempeño de los empleados');
INSERT INTO INFORMES(ID_EMPLEADO, FECHA, REPORTE) VALUES (3, '2024-08-10', 'Reporte del sistema financiero automatizado');

-----------------------------------------------------------------
INSERT INTO ASIGNACIONES(ID_EMPLEADO, ID_DEPARTAMENTO) VALUES (1, 2); 
INSERT INTO ASIGNACIONES(ID_EMPLEADO, ID_DEPARTAMENTO) VALUES (2, 1); 
INSERT INTO ASIGNACIONES(ID_EMPLEADO, ID_DEPARTAMENTO) VALUES (3, 3); 

-----------------------------------------------------------------
INSERT INTO EMPLEADO_ROL(ID_EMPLEADO, ID_ROL) VALUES (1, 1); 
INSERT INTO EMPLEADO_ROL(ID_EMPLEADO, ID_ROL) VALUES (2, 2); 
INSERT INTO EMPLEADO_ROL(ID_EMPLEADO, ID_ROL) VALUES (3, 3); 

-----------------------------------------------------------------
INSERT INTO PROYECTO_EMPLEADO(ID_EMPLEADO, ID_PROYECTO) VALUES (1, 1); 
INSERT INTO PROYECTO_EMPLEADO(ID_EMPLEADO, ID_PROYECTO) VALUES (2, 2); 
INSERT INTO PROYECTO_EMPLEADO(ID_EMPLEADO, ID_PROYECTO) VALUES (3, 3); 

-----------------------------------------------------------------
INSERT INTO REGISTRO_TIEMPO(FECHA, CANTIDAD_HORAS, DESCRIPCION, ID_PROYECTO_EMPLEADO) VALUES ('2024-07-01', 8, 'Desarrollo de funcionalidades en EcoTech App', 1);
INSERT INTO REGISTRO_TIEMPO(FECHA, CANTIDAD_HORAS, DESCRIPCION, ID_PROYECTO_EMPLEADO) VALUES('2024-07-05', 7, 'Planificación de sistema interno', 2);
INSERT INTO REGISTRO_TIEMPO(FECHA, CANTIDAD_HORAS, DESCRIPCION, ID_PROYECTO_EMPLEADO) VALUES('2024-07-10', 6, 'Pruebas de automatización financiera', 3);
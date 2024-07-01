-- Tabla para Especialidad -----------------------------------------------------------------------------
CREATE TABLE Especialidad (
    Id INT PRIMARY KEY,
    Nombre VARCHAR(100) 
);
-- Tabla para Médicos -----------------------------------------------------------------------------
CREATE TABLE Medico (
    Id INT PRIMARY KEY,
    Nombre VARCHAR(50),
    Apellido VARCHAR(50),
    Email VARCHAR(100),
    Contrasena VARCHAR(100),
    Id_Especialidad INT,
    Telefono VARCHAR(20),
    Fecha_Registro DATE,
    Id_Alta_Medico VARCHAR(20), 
    Num_Cedula VARCHAR(50),
    Calle VARCHAR(100),
    Colonia VARCHAR(100),
    Numero VARCHAR(10),
    Ciudad VARCHAR(100),
    Pais VARCHAR(100),
    Codigo_Postal VARCHAR(10),
    Honorarios DECIMAL(10, 2),
    FOREIGN KEY (Id_Especialidad) REFERENCES Especialidad(Id)
);
-- Tabla para Pacientes --------------------------------------------------------------------------
CREATE TABLE Paciente (
    Id INT PRIMARY KEY,
    Nombre VARCHAR(50),
    Apellido VARCHAR(50),
    Email VARCHAR(100),
    Contrasena VARCHAR(100),
    Telefono VARCHAR(20),
    Fecha_Nacimiento DATE,
    Sexo VARCHAR(10),
    Estatus VARCHAR(20)
);
-- Tabla para Administradores -----------------------------------------------------------------------
CREATE TABLE Administrador (
    Id INT PRIMARY KEY,
    Nombre VARCHAR(50),
    Apellido VARCHAR(50),
    Email VARCHAR(100),
    Contrasena VARCHAR(100),
    Estatus VARCHAR(20)
);
-- Tabla para Alta_Medico ----------------------------------------------------------------------------
/*
    * SIGNIFICADO DE ESTATUS ******************************************************************
    * 1 SOLICITUD ALTA
    * 2 APROBADO SIN PAGO
    * 3 ACTIVO
*/
CREATE TABLE Alta_Medico (
    Id INT PRIMARY KEY,
    Id_Medico INT,
    Estatus VARCHAR(50),
    Fecha_Alta DATE,
    Fecha_Modificacion DATE,
    FOREIGN KEY (Id_Medico) REFERENCES Medico(Id)
);

-- Tabla Suscripcion ----------------------------------------------------------------------------------
CREATE TABLE Suscripcion (
    Id INT PRIMARY KEY,
    Id_Tipo_Suscripcion INT,
    Id_Medico INT,
    Fecha_Inicio DATE,
    Fecha_Fin DATE,
    Estatus VARCHAR(20),
    FOREIGN KEY (Id_Tipo_Suscripcion) REFERENCES Tipo_Suscripcion(Id),
    FOREIGN KEY (Id_Medico) REFERENCES Medico(Id)
);
-- Tabla Tipo_Suscripcion -----------------------------------------------------------------------------
CREATE TABLE Tipo_Suscripcion (
    Id INT PRIMARY KEY,
    Nombre VARCHAR(50),
    Descripcion VARCHAR(100),
    Precio DECIMAL(10, 2),
    Duracion INT  
);
-- Tabla Pago_Suscripcion ------------------------------------------------------------------------------
CREATE TABLE Pago_Suscripcion (
    Id INT PRIMARY KEY,
    Id_Suscripcion INT,
    Monto DECIMAL(10, 2),
    Fecha_Pago DATE,
    FOREIGN KEY (Id_Suscripcion) REFERENCES Suscripcion(Id)
);
-- Tabla Dias -------------------------------------------------------------------------------------------
CREATE TABLE Dias (
    Id INT PRIMARY KEY,
    Dia VARCHAR(20) 
);
-- Tabla Horario -----------------------------------------------------------------------------------------
CREATE TABLE Horario (
    Id INT PRIMARY KEY,
    Id_Dia INT,
    Hora_Inicio TIME,
    Hora_Fin TIME,
    FOREIGN KEY (Id_Dia) REFERENCES Dias(Id)
);
-- Tabla Horario_Medico ---------------------------------------------------------------------------------
CREATE TABLE Horario_Medico (
    Id INT PRIMARY KEY,
    Id_Medico INT,
    Id_Horario INT,
    FOREIGN KEY (Id_Medico) REFERENCES Medico(Id),
    FOREIGN KEY (Id_Horario) REFERENCES Horario(Id)
);
-- Tabla Cita -------------------------------------------------------------------------------------------
/*
    * 0 Pendiente por confirmar (ninguno de los dos la ha aprobado)
    * 1 Confirmada por médico
    * 2 Confirmada por médico y paciente
    * 3 Cancelada por médico
    * 4 Cancelada por paciente
    * 5 Cita Terminada (Permitirá calificar al médico)

    #NOTA: Al usuario le aparecerá el recordatorio hasta una semana antes de su cita :D
*/
CREATE TABLE Cita (
    Id INT PRIMARY KEY,
    Id_Paciente INT,
    Id_Medico INT,
    Id_Horario INT,
    Fecha DATE,
    Descripcion TEXT,
    FOREIGN KEY (Id_Paciente) REFERENCES Paciente(Id),  
    FOREIGN KEY (Id_Medico) REFERENCES Medico(Id),
    FOREIGN KEY (Id_Horario) REFERENCES Horario(Id)
);
-- Tabla Motivos_Cita_Cancelacion --------------------------------------------------------------------------
CREATE TABLE Motivos_Cita_Cancelacion (
    Id INT PRIMARY KEY,
    Id_Cita INT,
    Motivo_Cancelacion TEXT,  
    FOREIGN KEY (Id_Cita) REFERENCES Cita(Id)
);
-- Tabla Calificacion_Medico --------------------------------------------------------------------------------
CREATE TABLE Calificacion_Medico (
    Id INT PRIMARY KEY,
    Id_Paciente INT,
    Id_Medico INT,
    Id_Cita INT,
    Puntuacion INT,
    Fecha DATE,
    Comentarios TEXT, 
    FOREIGN KEY (Id_Paciente) REFERENCES Paciente(Id),  
    FOREIGN KEY (Id_Medico) REFERENCES Medico(Id),
    FOREIGN KEY (Id_Cita) REFERENCES Cita(Id)
);
-- Tabla Pacientes_Asignados --------------------------------------------------------------------------------
CREATE TABLE Pacientes_Asignados (
    Id INT PRIMARY KEY,
    Id_Medico INT,
    Id_Paciente INT,
    Fecha DATE,
    Estatus VARCHAR(20),  
    FOREIGN KEY (Id_Medico) REFERENCES Medico(Id),
    FOREIGN KEY (Id_Paciente) REFERENCES Paciente(Id)  
);
-- Tabla Indicaciones --------------------------------------------------------------------------------
CREATE TABLE Indicaciones (
    Id INT PRIMARY KEY,
    Id_Historial_Clinico INT,
    Id_Paciente INT,
    Indicacion TEXT,
    Lapso VARCHAR(50),  
    Duracion VARCHAR(50),  
    Fecha_Inicio DATE,
    Estatus VARCHAR(10),
    FOREIGN KEY (Id_Historial_Clinico) REFERENCES Historial_Clinico(Id),
    FOREIGN KEY (Id_Paciente) REFERENCES Paciente(Id)  
);
-- Tabla Historial_Clinico --------------------------------------------------------------------------------
CREATE TABLE Historial_Clinico (
    Id INT PRIMARY KEY,
    Id_Paciente INT,
    Id_Medico INT,
    Observaciones TEXT,
    Diagnostico TEXT,
    Peso_Paciente DECIMAL(5, 2),
    Talla_Paciente DECIMAL(5, 2),
    FOREIGN KEY (Id_Paciente) REFERENCES Paciente(Id),
    FOREIGN KEY (Id_Medico) REFERENCES Medico(Id),,
);

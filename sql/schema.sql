CREATE DATABASE IF NOT EXISTS db_colegio;

USE db_colegio;

CREATE TABLE IF NOT EXISTS Asignaturas (
	asignatura_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    rama VARCHAR(255)
);
    
CREATE TABLE IF NOT EXISTS Profesores (
	profesor_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL, 
    apellido1 VARCHAR(255) NOT NULL,
    apellido2 VARCHAR(255)
);
    
CREATE TABLE IF NOT EXISTS ProfesorAsignatura (
	profesor_id INT,
    asignatura_id INT,
    FOREIGN KEY (profesor_id) REFERENCES Profesores(profesor_id),
    FOREIGN KEY (asignatura_id) REFERENCES Asignaturas(asignatura_id)
);

CREATE TABLE IF NOT EXISTS Aulas (
	aula_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_aula VARCHAR(255) NOT NULL,
    capacidad INT, 
    zona VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Alumnos (
	alumno_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    apellido1 VARCHAR(255) NOT NULL,
    apellido2 VARCHAR(255),
    fecha_incorporacion DATE,
    aula_id INT,
    FOREIGN KEY (aula_id) REFERENCES Aulas(aula_id)
);

CREATE TABLE IF NOT EXISTS Notas (
	nota_id INT AUTO_INCREMENT PRIMARY KEY,
    asignatura_id INT,
    alumno_id INT,
    nota FLOAT,
    trimestre INT,
    fecha_examen DATE,
    FOREIGN KEY (asignatura_id) REFERENCES Asignaturas(asignatura_id),
    FOREIGN KEY (alumno_id) REFERENCES Alumnos(alumno_id)
);

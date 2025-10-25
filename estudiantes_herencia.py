# -----------------------------------------
# Actividad Formativa 3: Herencia en Python
# Autor: Sarahi Téllez
# Materia: POO
# -----------------------------------------

# Clase base
class Estudiante:
    def _init_(self, nombre, matricula, carrera):
        self.nombre = nombre
        self.matricula = matricula
        self.carrera = carrera
        self.calificaciones = []

    def agregar_calificacion(self, nota):
        """Agrega una calificación al estudiante."""
        self.calificaciones.append(nota)

    def calcular_promedio(self):
        """Calcula el promedio de calificaciones."""
        if len(self.calificaciones) == 0:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)

    def mostrar_info(self):
        """Muestra la información general del estudiante."""
        print(f"Nombre: {self.nombre}")
        print(f"Matrícula: {self.matricula}")
        print(f"Carrera: {self.carrera}")
        print(f"Promedio: {self.calcular_promedio():.2f}")
        print("-" * 30)


# Clase derivada 1
class EstudianteLicenciatura(Estudiante):
    def _init_(self, nombre, matricula, carrera, semestre):
        # Llama al constructor de la clase base
        super()._init_(nombre, matricula, carrera)
        self.semestre = semestre

    def mostrar_tipo(self):
        """Muestra el tipo de estudiante."""
        print(f"Tipo de estudiante: Licenciatura - Semestre {self.semestre}")


# Clase derivada 2
class EstudiantePosgrado(Estudiante):
    def _init_(self, nombre, matricula, carrera, tema_investigacion):
        # Llama al constructor de la clase base
        super()._init_(nombre, matricula, carrera)
        self.tema_investigacion = tema_investigacion

    def mostrar_info(self):
        """Sobrescribe el método mostrar_info para agregar información extra."""
        super().mostrar_info()
        print(f"Tema de investigación: {self.tema_investigacion}")
        print("-" * 30)


# ---- Bloque principal de prueba ----
if _name_ == "_main_":
    # Estudiante de licenciatura
    est1 = EstudianteLicenciatura("Ana Pérez", "A12345", "Ingeniería en Sistemas", 5)
    est1.agregar_calificacion(90)
    est1.agregar_calificacion(85)
    est1.agregar_calificacion(100)

    # Estudiante de posgrado
    est2 = EstudiantePosgrado("Luis Gómez", "B67890", "Administración", "Estrategias de mercado")
    est2.agregar_calificacion(95)
    est2.agregar_calificacion(88)
    est2.agregar_calificacion(92)

    # Mostrar información de ambos estudiantes
    print("----- Información de Estudiantes -----\n")
    est1.mostrar_tipo()
    est1.mostrar_info()

    est2.mostrar_info()

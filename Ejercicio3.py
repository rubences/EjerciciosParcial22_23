class alumno:
    #Usamos el constructor para asignarle el nombre y la nota al alumno
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

        print(f"El alumno {self.nombre} se ha creado con exito")
    #Creamos un metodo para saber si el alumno ha aprobado o suspendido
    def calificacion(self):
        if self.nota >= 5 and self.nota <= 10:
            print(f"El alumno {self.nombre} ha aprobado. ")
        elif self.nota < 5 and self.nota >= 0:
            print(f"El alumno {self.nombre} ha suspendido. ")

#Creamos los alumnos
Dario = alumno("Dario", 5)
Javi = alumno("Javier", 7)
Mareque = alumno("Mareque", 3)
#Mostramos si han aprobado o suspendido
alumno.calificacion(Dario)
alumno.calificacion(Javi)
alumno.calificacion(Mareque)
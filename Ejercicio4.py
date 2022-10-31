class alumno:

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

        print(f"El alumno {self.nombre} se ha creado con exito")
    #Insertamos el metodo especial str para obtener una cadena con el nombre y nota del alumno
    def __str__(self):
        return F"Nombre: {self.nombre}\t Nota: {self.nota}"

    def calificacion(self):
        if self.nota >= 5 and self.nota <= 10:
            print(f"El alumno {self.nombre} ha aprobado. ")
        elif self.nota < 5 and self.nota >= 0:
            print(f"El alumno {self.nombre} ha suspendido. ")

Dario = alumno("Dario", 5)
Javi = alumno("Javier", 7)
Mareque = alumno("Mareque", 3)
print(Dario)
print(Javi)
print(Mareque)
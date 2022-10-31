class tabla_hash():

    #En primer lugar creo un constructor donde se crea la tabla hash de un determinado tamaño.
    def __init__(self, tamaño_tabla):
        self.tamaño_tabla = tamaño_tabla
        self.tabla = [None] * tamaño_tabla

    #Creamos un metodo que nos permitira imprimir esa tabla
    def imprime_tabla(self):
        for i in range (len(self.tabla)):
            print(f"{i}: {self.tabla[i]}")
    
    #Ahora calculamos la funcion hash de una cadena. Para ello asigno un valor de la tabla a cada caracter.
    #Viendo la funcion bernsteis, utilizaremos el numero magico 33
    def funcion_hash(self, caracter):
        return ord(caracter) * 33 % self.tamaño_tabla

    #Metodo para insertar elementos
    def Insert_elementos(self, valor):
        hash = self.funcion_hash(valor)
        if self.tabla[hash] is None:
            self.tabla[hash] = valor

    #Calcula el codigo hash de cada elemento de la cadena
    def encriptar(self, cadena):
        resultado = ""
        for i in cadena:
            self.Insert_elementos(i)
            resultado = resultado + chr(self.funcion_hash(i) + 33)
        return resultado

    #A partir de la cadena hasheada te devuelde la cadena original utilizando la tabla hash
    def desencriptar(self, cadena):
        resultado = ""
        for i in cadena:
            resultado = resultado + str(self.tabla[ord(i)-33])
        return resultado

alfabeto = [chr(i) for i in range(32, 125)]
#Lo primero es crear la tabla hash del tamaño y longitud del alfabeto
Hash = tabla_hash(len(alfabeto))
#Para comprobar si la tabla hash se cfeo correctamente insertaremos un elemento y luego imprimiremos la tabla
#Hash.Insertar_elementos("A")
#Hash.imprime_tabla()

#Pedrimos la cadena que se quiere encriptar
cadena = input("Introduce la cadena a encriptar: ")
print(f"Cadena sin encriptar: {cadena}")
#Encriptamos la cadena y la mostramos
cadena_encriptada = Hash.encriptar(cadena)
print(f"Cadena encriptada: {cadena_encriptada}")
#Desencriptamos y mostramos la cadena original
cadena_desencriptada = Hash.desencriptar(cadena_encriptada)
print(f"Cadena desencriptada: {cadena_desencriptada}")
numeros = [18, 50, 210, 80, 145, 333, 70, 30]

#Apartado 1
#Creo una funcion que cree una lista aparte con valores multiplos de diez y menores de 200
def imprimir(lista):
    multiplos1 = []
    for n in lista:
        if n % 10 == 0 and n < 200:
            multiplos1.append(n)
    return multiplos1

multiplos = imprimir(numeros)
print(multiplos)

#Apartado 2
#Hago lo mismo que en el apartado anterior pero salgo del bucle cuando encuentro un valor > que 300
def imprimir_2(lista):
    multiplos2 = []
    for n in lista:
        if n > 300:
            break
        if n % 10 == 0 and n < 200:
            multiplos2.append(n)
    return multiplos2

multiplos_2 = imprimir_2(numeros)
print(multiplos_2)

#Apartado 3
#Utilizo la funcion merge_sort para obtener la lista introducida ordenada de menor a mayor.
def merge_sort(coleccion: list) -> list:
    def merge(izquierda: list, derecha: list) -> list:

        def _merge():
            while izquierda and derecha:
                yield (izquierda if izquierda[0] <= derecha[0] else derecha).pop(0)
            yield from izquierda
            yield from derecha

        return list(_merge())
    if len(coleccion) <= 1:
        return coleccion
    medio = len(coleccion) // 2
    return merge(merge_sort(coleccion[:medio]), merge_sort(coleccion[medio:]))

print(merge_sort(numeros), sep=",")

#Apartado 4
#Finalmente hago una funcion indice para que me de el valor del indice en las dos situaciones propuestas
def indice(lista):
    if 145 in lista:
        print(numeros.index(145))
    else:
        print("-1")
    return indice
indice(numeros)
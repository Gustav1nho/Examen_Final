"""1. Utilizar el concepto de módulo necesariamente. Escribir un programa para
el manejo de listas el cuál cumplirá los siguientes requerimientos (3 ptos):
Reglas:
- Crear una función que le permitirá almacenar 10 números aleatorios en una
lista y finalmente los imprimirá por consola al llamar la función.
- Crear una función que le permita almacenar los números no repetidos de la
lista anterior, retornar este valor e imprimirlo por consola.
- Crear una función donde se creará una lista para ordenar de mayor a menor
la lista que se creó en el ítem anterior (número no repetidos) y otra lista
para ordenarlas de menor a mayor, retornar este valor e imprimirlos por
consola.
- Crear una función para indicar cuál es mayor número par de la lista (lista
del ítem 2), retornar este valor e imprimirlo por consola."""
import random


def AñadirNumero():
    lista = []
    for _ in range(0, 11):
        lista.append(random.randrange(0, 20))
    return lista


lista = AñadirNumero()


def Eliminar_Iguales():
    Nuevalista = list(set(lista))
    print("Nuestra nueva lista será {}".format(Nuevalista))
    return Nuevalista


Nuevalista = Eliminar_Iguales()


def ordenar():
    ascendente = sorted(Nuevalista)
    descendente = sorted(Nuevalista, reverse=True)
    print("Lista ordenada de menor a mayor será {}".format(ascendente))
    print("Lista ordenada de mayor a menor será {}".format(descendente))
    return ascendente, descendente


def mayorpar():
    pares = [num for num in Nuevalista if num % 2 == 0]
    if pares:
        par_mayor = max(pares)
        print("El mayor número par de la lista es: {}".format(par_mayor))
        return par_mayor
    else:
        print("No existen pares")
        return None

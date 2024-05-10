import math
import random

def escribir_lista(tamaño):
    with open("../Examen Final/Files/notas.txt", "a") as file:
        numeros = [random.randint(1, 100) for _ in range(tamaño)]
        file.write("Lista de números:\n")
        file.write(", ".join(map(str, numeros)) + "\n")

def calcular_raiz_cuadrada():
    with open("../Examen Final/Files/notas.txt", "a") as file:
        file.write("Raíces cuadradas de los números:\n")
        with open("../Examen Final/Files/notas.txt", "r") as f:
            lineas = f.readlines()
            numeros = lineas[1].strip().split(", ")
            raices = [math.sqrt(int(num)) for num in numeros]
            file.write(", ".join(map(str, raices)) + "\n")

escribir_lista(10)
calcular_raiz_cuadrada()

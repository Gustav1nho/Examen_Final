"""3. (2 ptos) Crear un programa usando decoradores para medir el tiempo de
ejecución.
Reglas:
- Crear la función decorador adecuadamente que sumará los elementos de la
función que pasará como parámetro de la función decoradora
- Crear una función, por ejemplo: multiplicación de 4 números (o x números)
para decorarla con la función anterior.
- Usar la propiedad de N parámetros para la función a decorar usando sus key
y values (**) y visualizar los resultados usando el decorador implementado
con un mínimo tres ejemplos."""

import time


def medir_tiempo(func):
    def decoracion(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecución de {func.__name__}: {fin - inicio} segundos")
        return resultado

    return decoracion


@medir_tiempo
def multiplicar(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado


resultado1 = multiplicar(2, 3, 4)
print("Primer resultado {}".format(resultado1))

resultado2 = multiplicar(5, 6, 7, 8)
print("segundo resultado {}".format(resultado2))

resultado3 = multiplicar(10, 20, 30, 40, 50)
print("tercer resultado {}".format(resultado3))

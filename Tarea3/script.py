import random
import math
# importar las funciones de funciones.py
from funciones import *

# importa las funciones de funciones_tarea2.py
from funciones_tarea2 import *

# Genera un vecino de la solución dada cambiando un bit aleatorio.
def generar_vecino(solucion, num_cambios=1):
    """Genera un vecino de la solución dada cambiando un bit aleatorio."""
    vecino = list(solucion)
    indices_a_cambiar = random.sample(range(len(solucion)), num_cambios)
    for indice in indices_a_cambiar:
        vecino[indice] = 1 - vecino[indice]  # Cambiar de 0 a 1 o de 1 a 0
    return vecino


# Enfriamiento lineal
 # T_k+1 = T_0 -n * k

def enfriamiento_lineal(T0, n, k):
    """Función de enfriamiento lineal.
    T0: Temperatura inicial.
    n: Número de iteraciones.
    k: Iteración actual.

    Retorna la temperatura en la iteración k.
    """
    return T0 - n * k 


def recocido_simulado(funcion, intervalo, num_bits, T0, n, kmax):
    """
    Algoritmo de recocido simulado para optimizar funciones de optimización continua.
    Parameters:
    funcion -- función a optimizar
    intervalo -- límites del intervalo
    num_bits -- número de bits usados para representar el número real
    T0 -- temperatura inicial
    n -- parámetro de enfriamiento
    kmax -- número máximo de iteraciones
    Returns:
    mejor_solucion -- mejor solución encontrada
    """
    # Genera una solución aleatoria
    solucion = [random.randint(0, 1) for _ in range(num_bits)]
    # Inicializa la mejor solución
    mejor_solucion = solucion
    # Inicializa la mejor evaluación
    mejor_evaluacion = funcion([decodificar(solucion, intervalo, num_bits)])
    # Inicializa la temperatura
    T = T0
    # Itera hasta que la temperatura llegue a 0
    for k in range(kmax):
        # Genera un vecino
        vecino = generar_vecino(solucion)
        # Decodifica el vecino
        x = decodificar(vecino, intervalo, num_bits)
        # Calcula la evaluación del vecino
        evaluacion = funcion([x])
        # Si el vecino es mejor que la mejor solución
        if evaluacion < mejor_evaluacion:
            # Actualiza la mejor solución
            mejor_solucion = vecino
            # Actualiza la mejor evaluación
            mejor_evaluacion = evaluacion
        # Si el vecino es peor que la solución actual
        else:
            # Calcula la probabilidad de aceptación
            p = math.exp((mejor_evaluacion - evaluacion) / T)
            # Si se acepta el vecino
            if random.random() < p:
                # Actualiza la solución actual
                solucion = vecino
        # Enfría la temperatura
        T = enfriamiento_lineal(T0, n, k)

    mejor_solucion = decodificar(mejor_solucion, intervalo, num_bits)
    return mejor_solucion


# ejecuta el algoritmo de recocido simulado para optimizar la funciónes 

# print(recocido_simulado(sphere, [-5.12, 5.12], 10, 100, 0.1, 1000))
# print(recocido_simulado(ackley, [-30, 30], 10, 100, 0.1, 1000))
# print(recocido_simulado(griewank, [-600, 600], 10, 100, 0.1, 1000))
# print(recocido_simulado(rastrigin, [-5.12, 5.12], 10, 100, 0.1, 1000))
# print(recocido_simulado(rosenbrock, [-2.048, 2.048], 10, 100, 0.1, 1000))


import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: Ejercicio1.py <algoritmo> <funcion> <intervalo> <num_bits> <kmax>")
        sys.exit(1)

    algoritmo = sys.argv[1]
    funcion = sys.argv[2]
    intervalo = [float(sys.argv[3]), float(sys.argv[4])]
    num_bits = int(sys.argv[5])
    kmax = int(sys.argv[6])

    if algoritmo == "busqueda_aleatoria":
        if funcion == "sphere":
            print(busqueda_aleatoria(sphere, intervalo, num_bits, kmax))
        elif funcion == "ackley":
            print(busqueda_aleatoria(ackley, intervalo, num_bits, kmax))
        elif funcion == "griewank":
            print(busqueda_aleatoria(griewank, intervalo, num_bits, kmax))
        elif funcion == "rastrigin":
            print(busqueda_aleatoria(rastrigin, intervalo, num_bits, kmax))
        elif funcion == "rosenbrock":
            print(busqueda_aleatoria(rosenbrock, intervalo, num_bits, kmax))
        else:
            print("Función no válida")
    elif algoritmo == "recocido_simulado":
        T0 = float(sys.argv[7])
        n = float(sys.argv[8])
        if funcion == "sphere":
            print(recocido_simulado(sphere, intervalo, num_bits, T0, n, kmax))
        elif funcion == "ackley":
            print(recocido_simulado(ackley, intervalo, num_bits, T0, n, kmax))
        elif funcion == "griewank":
            print(recocido_simulado(griewank, intervalo, num_bits, T0, n, kmax))
        elif funcion == "rastrigin":
            print(recocido_simulado(rastrigin, intervalo, num_bits, T0, n, kmax))
        elif funcion == "rosenbrock":
            print(recocido_simulado(rosenbrock, intervalo, num_bits, T0, n, kmax))
        else:
            print("Función no válida")
    else:
        print("Algoritmo no válido")
        sys.exit(1)



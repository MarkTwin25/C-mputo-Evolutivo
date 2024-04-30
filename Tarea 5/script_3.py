
import numpy as np
import random
import math
import matplotlib.pyplot as plt
from funciones import sphere, ackley, griewank, rastrigin, rosenbrock

from script_1 import *
from script_2 import *

# Ejercicio 3. Análisis de resultados
#Después de realizar la experimentación del ejercicio anterior, se deberá incluir en el reporte lo siguiente:
# 3.a) Gráficas de evolución de aptitud para diferentes ejecuciones.
# basta con incluir algunos ejemplos que sean interesantes ( debe incluir al menos
# 2 x ejemplar (una por cada una de las estrategias) y esto para al menos y ejemplares interesantes.)

import matplotlib.pyplot as plt

def graficar_evolucion_aptitud(funcion, intervalo, num_bits, T0, n, kmax, enfriamiento, iteraciones, semilla=None):
    # Fija la semilla del generador de números aleatorios
    if semilla is not None:
        random.seed(semilla)
    # Genera una solución aleatoria
    solucion = [random.randint(0, 1) for _ in range(num_bits)]
    # Inicializa la mejor solución
    mejor_solucion = solucion
    # Inicializa la mejor evaluación
    mejor_evaluacion = funcion([decodificar(solucion, intervalo, num_bits)])
    # Inicializa la temperatura
    T = T0
    # Inicializa la evolución de la aptitud
    evolucion_aptitud = [mejor_evaluacion]
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
            # Asegurarse de que T nunca sea cero
            T = max(enfriamiento(T0, n, k), 1e-10)
            p = math.exp((mejor_evaluacion - evaluacion) / T)
            # Si se acepta el vecino
            if random.random() < p:
                # Actualiza la solución actual
                solucion = vecino
        # Enfría la temperatura
        T = enfriamiento(T0, n, k)
        evolucion_aptitud.append(mejor_evaluacion)
    
    plt.plot(range(kmax + 1), evolucion_aptitud)
    plt.xlabel("Iteraciones")
    plt.ylabel("Aptitud")
    plt.title(funcion.__name__)
    plt.show()

#graficar_evolucion_aptitud(sphere, [-5.12, 5.12], 10, 100, 0.1, 1000, enfriamiento_exponencial, 1000, 1234)

def graficar_evolucion_aptitud_genetico(funcion, intervalo, tamano_poblacion, num_genes, prob_mutacion, num_generaciones, reemplazo, semilla=None):
    # Fija la semilla del generador de números aleatorios
    if semilla is not None:
        random.seed(semilla)
    # Inicializa la población
    poblacion = [[random.randint(0, 1) for _ in range(num_genes)] for _ in range(tamano_poblacion)]
    # Inicializa las aptitudes de la población
    aptitudes = [aptitud(individuo) for individuo in poblacion]
    # Inicializa la mejor solución
    mejor_solucion = poblacion[np.argmin(aptitudes)]
    # Inicializa la evolución de la aptitud
    evolucion_aptitud = [funcion([decodificar(mejor_solucion, intervalo, num_genes)])]
    # Itera hasta alcanzar el número de generaciones
    for _ in range(num_generaciones):
        # Genera una nueva población
        nueva_poblacion = []
        for _ in range(tamano_poblacion):
            # Selecciona dos padres
            padres = seleccion(poblacion, aptitudes, 2)
            # Cruza los padres
            hijo = cruzar(padres[0], padres[1])
            # Mutación
            hijo = mutar(hijo, prob_mutacion)
            nueva_poblacion.append(hijo)
        # Calcula las aptitudes de la nueva población
        nueva_aptitudes = [aptitud(individuo) for individuo in nueva_poblacion]
        # Reemplazo
        poblacion, aptitudes = reemplazo(poblacion, aptitudes, nueva_poblacion, nueva_aptitudes)
        # Actualiza la mejor solución
        if min(nueva_aptitudes) < aptitud(mejor_solucion):
            mejor_solucion = nueva_poblacion[np.argmin(nueva_aptitudes)]
        evolucion_aptitud.append(funcion([decodificar(mejor_solucion, intervalo, num_genes)])
)
    plt.plot(range(num_generaciones + 1), evolucion_aptitud)
    plt.xlabel("Generaciones")
    plt.ylabel("Aptitud")
    plt.title(funcion.__name__)
    plt.show()



def graficar_ejemplos_aptitud():
    funciones = [sphere, ackley, griewank]
    intervalos = [[-5.12, 5.12], [-30, 30], [-600, 600]]
    semillas = [2500, 5000, 7100]
    for funcion, intervalo, semilla in zip(funciones, intervalos, semillas):
        graficar_evolucion_aptitud(funcion, intervalo, 10, 100, 0.1, 1000, enfriamiento_exponencial, 1000, semilla)
        graficar_evolucion_aptitud_genetico(funcion, intervalo, 100, 10, 0.01, 100, generacional_elitismo, semilla)

graficar_ejemplos_aptitud()


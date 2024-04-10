# Describe e Implementa un algoritmo genético para el problema de optimización de
# gráficas.

import random
import numpy as np
import matplotlib.pyplot as plt


# 1. Representación de la solución (cromosoma)
def generar_cromosoma(tam_poblacion, tam_grafica):
    poblacion = []
    for i in range(tam_poblacion):
        cromosoma = [random.randint(0, 1) for _ in range(tam_grafica)]
        poblacion.append(cromosoma)
    return poblacion

# Tipos de metodos de seleccion de padres ()
# 2. Selección de padres metodo torneo
def seleccion_padres_torneo(aptitudes):
    padres = []
    for _ in range(2):
        idx1 = random.randint(0, len(aptitudes) - 1)
        idx2 = random.randint(0, len(aptitudes) - 1)
        if aptitudes[idx1] > aptitudes[idx2]:
            padres.append(idx1)
        else:
            padres.append(idx2)
    return padres

# 3. Cruza de cromosomas (1 punto)
def cruza(padres, poblacion):
    punto_cruza = random.randint(1, len(poblacion[0]) - 1)
    hijo1 = poblacion[padres[0]][:punto_cruza] + poblacion[padres[1]][punto_cruza:]
    hijo2 = poblacion[padres[1]][:punto_cruza] + poblacion[padres[0]][punto_cruza:]
    return hijo1, hijo2

# 4. Mutación de cromosomas
def mutacion(cromosoma, prob_mutacion):
    for i in range(len(cromosoma)):
        if random.random() < prob_mutacion:
            cromosoma[i] = 1 - cromosoma[i]
    return cromosoma


# 5. Reemplazo de la población con elitismo
def reemplazo_generacional(poblacion, aptitudes, nueva_poblacion, nueva_aptitudes):
    poblacion = poblacion + nueva_poblacion
    aptitudes = aptitudes + nueva_aptitudes
    idxs = np.argsort(aptitudes)[::-1]
    poblacion = [poblacion[i] for i in idxs[:len(poblacion)]]
    aptitudes = [aptitudes[i] for i in idxs[:len(poblacion)]]
    return poblacion, aptitudes


# Algoritmo genético
def algoritmo_genetico(tam_poblacion, tam_grafica, prob_mutacion, num_generaciones):
    poblacion = generar_cromosoma(tam_poblacion, tam_grafica)
    aptitudes = [random.random() for _ in range(tam_poblacion)]
    mejor_aptitud = max(aptitudes)
    mejor_cromosoma = poblacion[aptitudes.index(mejor_aptitud)]
    for _ in range(num_generaciones):
        nueva_poblacion = []
        nueva_aptitudes = []
        for _ in range(tam_poblacion // 2):
            padres = seleccion_padres_torneo(aptitudes)
            hijo1, hijo2 = cruza(padres, poblacion)
            hijo1 = mutacion(hijo1, prob_mutacion)
            hijo2 = mutacion(hijo2, prob_mutacion)
            nueva_poblacion.append(hijo1)
            nueva_poblacion.append(hijo2)
            nueva_aptitudes.append(random.random())
            nueva_aptitudes.append(random.random())
        poblacion, aptitudes = reemplazo_generacional(poblacion, aptitudes, nueva_poblacion, nueva_aptitudes)
        if max(aptitudes) > mejor_aptitud:
            mejor_aptitud = max(aptitudes)
            mejor_cromosoma = poblacion[aptitudes.index(mejor_aptitud)]
    return mejor_cromosoma, mejor_aptitud


# Ejemplo de uso

def ejecucion_ejemplo():
    tam_poblacion = 100
    tam_grafica = 10
    prob_mutacion = 0.01
    num_generaciones = 100
    mejor_cromosoma, mejor_aptitud = algoritmo_genetico(tam_poblacion, tam_grafica, prob_mutacion, num_generaciones)
    print("Mejor cromosoma:", mejor_cromosoma)
    print("Mejor aptitud:", mejor_aptitud)
    plt.plot(mejor_cromosoma)
    plt.show()

# Graficar evolución de la aptitud

def graficar_evolucion():
    tam_poblacion = 100
    tam_grafica = 10
    prob_mutacion = 0.01
    num_generaciones = 100
    poblacion = generar_cromosoma(tam_poblacion, tam_grafica)
    aptitudes = [random.random() for _ in range(tam_poblacion)]
    mejor_aptitud = max(aptitudes)
    mejor_cromosoma = poblacion[aptitudes.index(mejor_aptitud)]
    evolucion_aptitud = []
    for _ in range(num_generaciones):
        nueva_poblacion = []
        nueva_aptitudes = []
        for _ in range(tam_poblacion // 2):
            padres = seleccion_padres_torneo(aptitudes)
            hijo1, hijo2 = cruza(padres, poblacion)
            hijo1 = mutacion(hijo1, prob_mutacion)
            hijo2 = mutacion(hijo2, prob_mutacion)
            nueva_poblacion.append(hijo1)
            nueva_poblacion.append(hijo2)
            nueva_aptitudes.append(random.random())
            nueva_aptitudes.append(random.random())
        poblacion, aptitudes = reemplazo_generacional(poblacion, aptitudes, nueva_poblacion, nueva_aptitudes)
        if max(aptitudes) > mejor_aptitud:
            mejor_aptitud = max(aptitudes)
            mejor_cromosoma = poblacion[aptitudes.index(mejor_aptitud)]
        evolucion_aptitud.append(mejor_aptitud)
    plt.plot(evolucion_aptitud)
    plt.show()

# ejecucion_ejemplo()

import sys
if __name__ == "__main__":
    if sys.argv[1] == "genetico":
        ejecucion_ejemplo()
    elif sys.argv[1] == "grafica":
        graficar_evolucion()
    else:
        ejecucion_ejemplo()
        graficar_evolucion()

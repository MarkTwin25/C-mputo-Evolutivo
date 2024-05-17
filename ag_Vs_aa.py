# Algoritmo de recocido simulado para el problema de set covering 

# ejemplo:
# Considere un conjunto

#U = {1, 2, 3, 4, 5}
#y una familia de subconjuntos
#F = {{1, 2, 3}, {2, 4}, {3, 4}, {4, 5}}
#La solución óptima es
# F' = {{1, 2, 3}, {4, 5}}
#que cubre todos los elementos de U.

# Se desea encontrar la solución óptima utilizando un algoritmo genético


# Se importan las librerías necesarias
import random
import numpy as np

# 1. generar la población inicial
def generar_poblacion_inicial(tamano_poblacion, num_subconjuntos):
    poblacion = []
    for i in range(tamano_poblacion):
        individuo = []
        for j in range(num_subconjuntos):
            individuo.append(random.randint(0, 1))
        poblacion.append(individuo)
    return poblacion

#print(generar_poblacion_inicial(4, 3))

# 2. seleccionar los padres
def seleccionar_padres(poblacion, fitness, num_padres):
    padres = []
    for i in range(num_padres):
        idx_padre = np.argmax(fitness)
        padres.append(poblacion[idx_padre])
        fitness[idx_padre] = -1
    return padres

#poblacion = [[0, 1, 0], [1, 0, 1], [0, 0, 1], [1, 1, 0]]
#fitness = [2, 3, 1, 2]
#num_padres = 2
#print(seleccionar_padres(poblacion, fitness, num_padres))

# 3. cruzar los padres
def cruzar_padres(padres, num_hijos):
    hijos = []
    for i in range(num_hijos):
        padre1 = padres[random.randint(0, len(padres)-1)]
        padre2 = padres[random.randint(0, len(padres)-1)]
        punto_cruce = random.randint(0, len(padre1)-1)
        hijo = padre1[:punto_cruce] + padre2[punto_cruce:]
        hijos.append(hijo)
    return hijos

#padres = [[0, 1, 0], [1, 0, 1]]
#num_hijos = 2
#print(cruzar_padres(padres, num_hijos))

# 4. mutar los hijos
def mutar_hijos(hijos, prob_mutacion):
    for i in range(len(hijos)): 
        for j in range(len(hijos[i])): 
            if random.random() < prob_mutacion: 
                hijos[i][j] = 1 - hijos[i][j] 
    return hijos

#hijos = [[0, 1, 0], [1, 0, 1]]
#prob_mutacion = 0.2
#print(mutar_hijos(hijos, prob_mutacion))

# 5. evaluar la población
def evaluar_poblacion(poblacion, subconjuntos, elementos):
    fitness = [] # lista de valores de fitness
    for i in range(len(poblacion)): # para cada individuo en la población
        cobertura = set() # inicializar la cobertura
        for j in range(len(poblacion[i])): # para cada subconjunto en el individuo
            if poblacion[i][j] == 1: # si el subconjunto está seleccionado
                cobertura = cobertura.union(subconjuntos[j]) # agregar los elementos del subconjunto a la cobertura
        fitness.append(len(cobertura.intersection(elementos))) # calcular el fitness como la cantidad de elementos cubiertos
    return fitness

#poblacion = [[0, 1, 0], [1, 0, 1], [0, 0, 1], [1, 1, 0]]
#subconjuntos = [{1, 2}, {2, 4}, {3, 4}]
#elementos = {1, 2, 3, 4, 5}
#print(evaluar_poblacion(poblacion, subconjuntos, elementos))

# 6. algoritmo genético
def algoritmo_genetico(tamano_poblacion, num_subconjuntos, num_generaciones, 
                        num_padres, num_hijos, prob_mutacion, subconjuntos, elementos):
    poblacion = generar_poblacion_inicial(tamano_poblacion, num_subconjuntos)
    for i in range(num_generaciones):
        fitness = evaluar_poblacion(poblacion, subconjuntos, elementos)
        padres = seleccionar_padres(poblacion, fitness, num_padres)
        hijos = cruzar_padres(padres, num_hijos)
        hijos_mutados = mutar_hijos(hijos, prob_mutacion)
        poblacion = padres + hijos_mutados
    fitness = evaluar_poblacion(poblacion, subconjuntos, elementos)
    idx_mejor = np.argmax(fitness)
    mejor_solucion = poblacion[idx_mejor]
    return mejor_solucion

# Definir los elementos y subconjuntos
elementos = {1, 2, 3, 4, 5}
subconjuntos = [{1, 2}, {2, 4}, {3, 4}, {4, 5}]
tamano_poblacion = 10
num_subconjuntos = len(subconjuntos)
num_generaciones = 100
num_padres = 2
num_hijos = 2
prob_mutacion = 0.1

#Ejecutar el algoritmo genético
mejor_solucion = algoritmo_genetico(tamano_poblacion, num_subconjuntos, num_generaciones, num_padres, num_hijos, prob_mutacion, subconjuntos, elementos)
print(mejor_solucion)

# Ahora usar el algoritmo tabu search para encontrar la mejor solución
# Se importan las librerías necesarias

# 1. generar la población inicial
def generar_poblacion_inicial(tamano_poblacion, num_subconjuntos):
    poblacion = []
    for i in range(tamano_poblacion):
        individuo = []
        for j in range(num_subconjuntos):
            individuo.append(random.randint(0, 1))
        poblacion.append(individuo)
    return poblacion

# 2. evaluar la población
def evaluar_poblacion(poblacion, subconjuntos, elementos):
    fitness = []
    for i in range(len(poblacion)):
        cobertura = set()
        for j in range(len(poblacion[i])):
            if poblacion[i][j] == 1:
                cobertura = cobertura.union(subconjuntos[j])
        fitness.append(len(cobertura.intersection(elementos)))
    return fitness

# 3. obtener los vecinos
def obtener_vecinos(individuo):
    vecinos = []
    for i in range(len(individuo)):
        vecino = individuo.copy()
        vecino[i] = 1 - vecino[i]
        vecinos.append(vecino)
    return vecinos

# 4. algoritmo tabu search
def tabu_search(tamano_poblacion, num_subconjuntos, num_iteraciones, subconjuntos, elementos):
    poblacion = generar_poblacion_inicial(tamano_poblacion, num_subconjuntos)
    mejor_solucion = poblacion[0]
    mejor_fitness = evaluar_poblacion([mejor_solucion], subconjuntos, elementos)[0]
    tabu_list = []
    for i in range(num_iteraciones):
        fitness = evaluar_poblacion(poblacion, subconjuntos, elementos)
        idx_mejor = np.argmax(fitness)
        if fitness[idx_mejor] > mejor_fitness:
            mejor_solucion = poblacion[idx_mejor]
            mejor_fitness = fitness[idx_mejor]
        vecinos = obtener_vecinos(poblacion[idx_mejor])
        idx_mejor_vecino = -1
        mejor_fitness_vecino = -1
        for j in range(len(vecinos)):
            if vecinos[j] not in tabu_list:
                fitness_vecino = evaluar_poblacion([vecinos[j]], subconjuntos, elementos)[0]
                if fitness_vecino > mejor_fitness_vecino:
                    mejor_fitness_vecino = fitness_vecino
                    idx_mejor_vecino = j
        if idx_mejor_vecino != -1:
            poblacion[idx_mejor] = vecinos[idx_mejor_vecino]
            tabu_list.append(vecinos[idx_mejor_vecino])
            if len(tabu_list) > tamano_poblacion:
                tabu_list.pop(0)
    return mejor_solucion

# Definir los elementos y subconjuntos
elementos = {1, 2, 3, 4, 5}
subconjuntos = [{1},{2},{3},{4,5},{5}]
tamano_poblacion = 10
num_subconjuntos = len(subconjuntos)
num_iteraciones = 100

# Ejecutar el algoritmo tabu search
#mejor_solucion = tabu_search(tamano_poblacion, num_subconjuntos, num_iteraciones, subconjuntos, elementos)
#print(mejor_solucion)

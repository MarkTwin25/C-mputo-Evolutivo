# Algoritmo genético vs algoritmo de colonia de hormigas(ACO)
# en el problema del viajante de comercio 

import random
import math

# algoritmo genetico para el problema del viajante de comercio

# 1. Función para generar la población inicial
def generar_poblacion(tamano_poblacion, tamano_gen):
    poblacion = []
    for _ in range(tamano_poblacion):
        individuo = [i for i in range(tamano_gen)]
        random.shuffle(individuo)
        poblacion.append(individuo)
    return poblacion

# 2. Función de selección de individuos
def seleccion(poblacion, distancias):
    seleccionados = []
    for individuo in poblacion:
        distancia_total = sum(distancias[individuo[i - 1]][individuo[i]] for i in range(1, len(individuo)))
        distancia_total += distancias[individuo[-1]][individuo[0]]
        seleccionados.append((individuo, distancia_total))
    return seleccionados

# 3. Función de cruzamiento (crossover) OX
def cruzamiento(padre, madre):
    punto_corte1 = random.randint(0, len(padre) - 1)
    punto_corte2 = random.randint(0, len(padre) - 1)
    punto_corte1, punto_corte2 = min(punto_corte1, punto_corte2), max(punto_corte1, punto_corte2)
    hijo1 = [-1 for _ in range(len(padre))]
    hijo2 = [-1 for _ in range(len(padre))]
    for i in range(punto_corte1, punto_corte2 + 1):
        hijo1[i] = madre[i]
        hijo2[i] = padre[i]
    j1, j2 = 0, 0
    for i in range(len(padre)):
        if j1 == punto_corte1:
            j1 = punto_corte2 + 1
        if j2 == punto_corte1:
            j2 = punto_corte2 + 1
        if padre[i] not in hijo1:
            hijo1[j1] = padre[i]
            j1 += 1
        if madre[i] not in hijo2:
            hijo2[j2] = madre[i]
            j2 += 1
    return hijo1, hijo2

# 4. Función de mutación swap
def mutacion(individuo):
    i, j = random.sample(range(len(individuo)), 2)
    individuo[i], individuo[j] = individuo[j], individuo[i]
    return individuo

# 5. Reemplazo generacional con elitismo
def reemplazo(poblacion, nueva_generacion):
    poblacion.extend(nueva_generacion)
    poblacion.sort(key=lambda x: x[1])
    return poblacion[:len(nueva_generacion)]

# Algoritmo genético
def algoritmo_genetico(tamano_poblacion, tamano_gen, distancias, probabilidad_mutacion, num_generaciones):
    poblacion = generar_poblacion(tamano_poblacion, tamano_gen)
    for _ in range(num_generaciones):
        seleccionados = seleccion(poblacion, distancias)
        nueva_generacion = []
        while len(nueva_generacion) < tamano_poblacion:
            padre = random.choice(seleccionados)[0]
            madre = random.choice(seleccionados)[0]
            hijo1, hijo2 = cruzamiento(padre, madre)
            hijo1 = mutacion(hijo1)
            hijo2 = mutacion(hijo2)
            nueva_generacion.append(hijo1)
            nueva_generacion.append(hijo2)
        poblacion = reemplazo(poblacion, nueva_generacion)
    mejor_individuo = min(seleccionados, key=lambda x: x[1])
    return mejor_individuo

# Ejemplo de uso:

# Distancias entre ciudades
distancias = [
    [0, 29, 20, 21], # Distancias de la ciudad A a las demás ciudades
    [29, 0, 15, 12], # Distancias de la ciudad B a las demás ciudades
    [20, 15, 0, 25], # Distancias de la ciudad C a las demás ciudades
    [21, 12, 25, 0] # Distancias de la ciudad D a las demás ciudades
]

# Parámetros del algoritmo genético
tamano_poblacion = 100
tamano_gen = 4
probabilidad_mutacion = 0.1
num_generaciones = 100

# Ejecutar el algoritmo genético
mejor_individuo = algoritmo_genetico(tamano_poblacion, tamano_gen, distancias, probabilidad_mutacion, num_generaciones)
print(mejor_individuo)

# Algoritmo de colonia de hormigas para el problema del viajante de comercio

# 1. Función para inicializar las feromonas
def inicializar_feromonas(tamano_gen):
    return [[1 for _ in range(tamano_gen)] for _ in range(tamano_gen)]

# 2. Función para seleccionar la siguiente ciudad
def seleccionar_ciudad(ciudad_actual, ciudades_restantes, feromonas, alfa, beta):
    probabilidades = []
    for ciudad in ciudades_restantes:
        numerador = feromonas[ciudad_actual][ciudad] ** alfa * (1.0 / distancias[ciudad_actual][ciudad]) ** beta
        denominador = sum(feromonas[ciudad_actual][c] ** alfa * (1.0 / distancias[ciudad_actual][c]) ** beta for c in ciudades_restantes)
        probabilidad = numerador / denominador
        probabilidades.append((ciudad, probabilidad))
    seleccionada = max(probabilidades, key=lambda x: x[1])
    return seleccionada[0]

# 3. Función para actualizar las feromonas
def actualizar_feromonas(feromonas, mejores_hormigas, evaporacion, Q):
    for i in range(len(feromonas)):
        for j in range(len(feromonas[i])):
            feromonas[i][j] *= evaporacion
    for hormiga in mejores_hormigas:
        for i in range(len(hormiga) - 1):
            feromonas[hormiga[i]][hormiga[i + 1]] += Q

# Algoritmo de colonia de hormigas
# Algoritmo de colonia de hormigas
def colonia_hormigas(tamano_gen, distancias, feromonas, alfa, beta, evaporacion, Q, num_generaciones):
    mejores_hormigas = []
    for _ in range(num_generaciones):
        hormigas = []
        for _ in range(tamano_gen):
            ciudad_actual = random.randint(0, tamano_gen - 1)
            ciudades_restantes = set(range(tamano_gen))
            ciudades_restantes.remove(ciudad_actual)
            hormiga = [ciudad_actual]
            while ciudades_restantes:
                siguiente_ciudad = seleccionar_ciudad(ciudad_actual, ciudades_restantes, feromonas, alfa, beta)
                hormiga.append(siguiente_ciudad)
                ciudades_restantes.remove(siguiente_ciudad)
                ciudad_actual = siguiente_ciudad
            hormigas.append(hormiga)
        mejores_hormiga = min(hormigas, key=lambda x: sum(distancias[x[i - 1]][x[i]] for i in range(1, len(x))))
        mejores_hormigas.append(mejores_hormiga)
        actualizar_feromonas(feromonas, mejores_hormigas, evaporacion, Q)
    mejor_individuo = min(mejores_hormigas, key=lambda x: sum(distancias[x[i - 1]][x[i]] for i in range(1, len(x))))
    km_recorridos = sum(distancias[mejor_individuo[i - 1]][mejor_individuo[i]] for i in range(1, len(mejor_individuo)))
    km_recorridos += distancias[mejor_individuo[-1]][mejor_individuo[0]]  # Sumar la distancia desde la última ciudad hasta la ciudad de origen
    return mejor_individuo, km_recorridos

# Ejemplo de uso:

# Parámetros del algoritmo de colonia de hormigas
alfa = 1
beta = 2
evaporacion = 0.1
Q = 2
num_generaciones = 100

# Inicializar las feromonas
feromonas = inicializar_feromonas(tamano_gen)

# Ejecutar el algoritmo de colonia de hormigas
mejor_individuo = colonia_hormigas(tamano_gen, distancias, feromonas, alfa, beta, evaporacion, Q, num_generaciones)

print(mejor_individuo)



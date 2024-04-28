#Ejercicio 1. Parametrización de Algoritmos
#En esta tarea vamos a comparar diferentes algoritmos para resolver problemas de optimización
#continua. Implementa los cambios necesarios para poder realizar las siguientes comparaciones:

#1.a) Parámetros del Recocido simulado
#a) Comparar al menos dos esquemas de enfriamiento.

import numpy as np
import random
import math
import matplotlib.pyplot as plt
from funciones import sphere, ackley, griewank, rastrigin, rosenbrock

# ¿ que esquemas de enfriamiento se van a comparar?
# Enfriamiento lineal y enfriamiento exponencial

def enfriamiento_lineal(T0, n, k):
    """
    Enfriamiento lineal.
    Parameters:
    T0 -- temperatura inicial
    n -- parámetro de enfriamiento
    k -- iteración actual
    Returns:
    T -- temperatura
    """
    return T0 - n * k

def enfriamiento_exponencial(T0, n, k):
    """
    Enfriamiento exponencial.
    Parameters:
    T0 -- temperatura inicial
    n -- parámetro de enfriamiento
    k -- iteración actual
    Returns:
    T -- temperatura
    """
    return T0 * n**k

def recocido_simulado(funcion, intervalo, num_bits, T0, n, kmax, enfriamiento):
    """
    Algoritmo de recocido simulado para optimizar funciones de optimización continua.
    Parameters:
    funcion -- función a optimizar
    intervalo -- límites del intervalo
    num_bits -- número de bits usados para representar el número real
    T0 -- temperatura inicial
    n -- parámetro de enfriamiento
    kmax -- número máximo de iteraciones
    enfriamiento -- esquema de enfriamiento
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
            # Asegurarse de que T nunca sea cero
            T = max(enfriamiento(T0, n, k), 1e-10)
            
            p = math.exp((mejor_evaluacion - evaluacion) / T)
            # Si se acepta el vecino
            if random.random() < p:
                # Actualiza la solución actual
                solucion = vecino
        # Enfría la temperatura
        T = enfriamiento(T0, n, k)

    mejor_solucion = decodificar(mejor_solucion, intervalo, num_bits)
    return mejor_solucion

def generar_vecino(solucion):
    """
    Genera un vecino.
    Parameters:
    solucion -- solución actual
    Returns:
    vecino -- vecino
    """
    vecino = solucion.copy()
    i = random.randint(0, len(solucion) - 1)
    vecino[i] = 1 - vecino[i]
    return vecino

def decodificar(solucion, intervalo, num_bits):
    """
    Decodifica una solución.
    Parameters:
    solucion -- solución
    intervalo -- límites del intervalo
    num_bits -- número de bits usados para representar el número real
    Returns:
    x -- número real
    """
    x = 0
    for i in range(num_bits):
        x += solucion[i] * 2**i
    x = intervalo[0] + x * (intervalo[1] - intervalo[0]) / (2**num_bits - 1)
    return x

    # Ejecutar cada función de optimización con enfriamiento lineal y exponencial y generar tabla con resultados
def ejecutar_recocido_simulado():
    # Funciones de optimización
    funciones = [sphere, ackley, griewank, rastrigin, rosenbrock]
    # Límites de los intervalos
    intervalos = [[-5.12, 5.12], [-30, 30], [-600, 600], [-5.12, 5.12], [-2.048, 2.048]]
    # Número de bits
    num_bits = 10
    # Temperatura inicial
    T0 = 100
    # Parámetro de enfriamiento
    n = 0.1
    # Número máximo de iteraciones
    kmax = 1000

    # Esquemas de enfriamiento
    enfriamientos = [enfriamiento_lineal, enfriamiento_exponencial]
    alias_enfriamientos = {enfriamiento_lineal: "Lineal", enfriamiento_exponencial: "Exponencial"}

    # Tabla con resultados
    resultados = []
    for funcion, intervalo in zip(funciones, intervalos):
        for enfriamiento in enfriamientos:
            mejor_solucion = recocido_simulado(funcion, intervalo, num_bits, T0, n, kmax, enfriamiento)
            resultados.append([funcion.__name__, alias_enfriamientos[enfriamiento], mejor_solucion])

    # Mostrar tabla con resultados
    print("{:<20} {:<20} {:<20}".format("Función", "Enfriamiento", "Mejor solución"))
    for resultado in resultados:
        print("{:<20} {:<20} {:<20}".format(resultado[0], resultado[1], str(resultado[2])))


# Los resultados son:
#Recocido simulado
#Función              Enfriamiento         Mejor solución      
#sphere               Lineal               0.02502443792766318
#sphere               Exponencial          -0.005004887585532636
#ackley               Lineal               0.02932551319648269
#ackley               Exponencial          -0.02932551319648269
#griewank             Lineal               -25.219941348973634
#griewank             Exponencial          -12.316715542522047
#rastrigin            Lineal               -0.005004887585532636
#rastrigin            Exponencial          0.005004887585532636
#rosenbrock           Lineal               -0.9389169110459432
#rosenbrock           Exponencial          1.0229990224828933

# ¿Cuál es el mejor esquema de enfriamiento para cada función de optimización?
#Para "sphere", el esquema de enfriamiento lineal parece ser mejor.
#Para "griewank" y "rosenbrock", el esquema de enfriamiento exponencial parece ser mejor.
# Para "ackley" y "rastringin ", ambos esquemas son igualmente efectivos, pero producen soluciones con signos opuestos.


#1b Parámetros del Algoritmo genético
#   Comparar los siguientes esquemas de reemplazo:
#i) Generacional
#ii) Generacional con elitismo
#iii) Reemplazo de los peores

def generacional(poblacion, aptitudes, nueva_poblacion, nueva_aptitudes):
    """
    Reemplazo generacional.
    Parameters:
    poblacion -- población actual
    aptitudes -- aptitudes de la población actual
    nueva_poblacion -- nueva población
    nueva_aptitudes -- aptitudes de la nueva población
    Returns:
    poblacion -- población actual
    aptitudes -- aptitudes de la población actual
    """
    # Reemplaza la población actual
    poblacion = nueva_poblacion
    # Calcula las aptitudes de la población actual
    aptitudes = nueva_aptitudes
    return poblacion, aptitudes

def generacional_elitismo(poblacion, aptitudes, nueva_poblacion, nueva_aptitudes):
    """
    Reemplazo generacional con elitismo.
    Parameters:
    poblacion -- población actual
    aptitudes -- aptitudes de la población actual
    nueva_poblacion -- nueva población
    nueva_aptitudes -- aptitudes de la nueva población
    Returns:
    poblacion -- población actual
    aptitudes -- aptitudes de la población actual
    """
    # Selecciona los individuos de la población actual
    seleccionados = [poblacion[i] for i in np.argsort(aptitudes)[:len(nueva_poblacion)]]
    # Selecciona los individuos de la nueva población
    nuevos = [nueva_poblacion[i] for i in np.argsort(nueva_aptitudes)]
    # Reemplaza la población actual
    poblacion = seleccionados + nuevos
    # Calcula las aptitudes de la población actual
    aptitudes = [aptitud(individuo) for individuo in poblacion]
    return poblacion, aptitudes

def reemplazo_peores(poblacion, aptitudes, nueva_poblacion, nueva_aptitudes):
    """
    Reemplazo de los peores.
    Parameters:
    poblacion -- población actual
    aptitudes -- aptitudes de la población actual
    nueva_poblacion -- nueva población
    nueva_aptitudes -- aptitudes de la nueva población
    Returns:
    poblacion -- población actual
    aptitudes -- aptitudes de la población actual
    """
    # Reemplaza los peores individuos
    indices = np.argsort(aptitudes)[:len(nueva_poblacion)]
    for i, indice in enumerate(indices):
        poblacion[indice] = nueva_poblacion[i]
        aptitudes[indice] = nueva_aptitudes[i]
    return poblacion, aptitudes

def algoritmo_genetico(funcion, intervalo, tamano_poblacion, num_genes, prob_mutacion, num_generaciones, reemplazo):
    """
    Algoritmo genético para optimizar funciones de optimización continua.
    Parameters:
    funcion -- función a optimizar
    intervalo -- límites del intervalo
    tamano_poblacion -- tamaño de la población
    num_genes -- número de genes
    prob_mutacion -- probabilidad de mutación
    num_generaciones -- número de generaciones
    reemplazo -- esquema de reemplazo
    Returns:
    mejor_solucion -- mejor solución encontrada
    """
    # Inicializa la población
    poblacion = [[random.randint(0, 1) for _ in range(num_genes)] for _ in range(tamano_poblacion)]
    # Inicializa las aptitudes de la población
    aptitudes = [aptitud(individuo) for individuo in poblacion]
    # Inicializa la mejor solución
    mejor_solucion = poblacion[np.argmin(aptitudes)]
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
    mejor_solucion = decodificar(mejor_solucion, intervalo, num_genes)
    return mejor_solucion

def seleccion(poblacion, aptitudes, n):
    """
    Selección por torneo.
    Parameters:
    poblacion -- población
    aptitudes -- aptitudes de la población
    n -- número de individuos a seleccionar
    Returns:
    seleccionados -- individuos seleccionados
    """
    seleccionados = []
    for _ in range(n):
        indices = random.sample(range(len(poblacion)), 2)
        seleccionados.append(poblacion[indices[np.argmin([aptitudes[i] for i in indices])]])
    return seleccionados

def cruzar(padre1, padre2):
    """
    Cruza de un punto.
    Parameters:
    padre1 -- primer padre
    padre2 -- segundo padre
    Returns:
    hijo -- hijo
    """
    punto = random.randint(0, len(padre1) - 1)
    hijo = padre1[:punto] + padre2[punto:]
    return hijo

def mutar(individuo, prob_mutacion):
    """
    Mutación.
    Parameters:
    individuo -- individuo
    prob_mutacion -- probabilidad de mutación
    Returns:
    individuo -- individuo mutado
    """
    for i in range(len(individuo)):
        if random.random() < prob_mutacion:
            individuo[i] = 1 - individuo[i]
    return individuo

def aptitud(individuo):
    """
    Aptitud de un individuo.
    Parameters:
    individuo -- individuo
    Returns:
    aptitud -- aptitud del individuo
    """
    x = decodificar(individuo, [-5.12, 5.12], 10)
    return sphere([x])

def ejecutar_algoritmo_genetico():
    # Funciones de optimización
    funciones = [sphere, ackley, griewank, rastrigin, rosenbrock]
    # Límites de los intervalos
    intervalos = [[-5.12, 5.12], [-30, 30], [-600, 600], [-5.12, 5.12], [-2.048, 2.048]]
    # Tamaño de la población
    tamano_poblacion = 100
    # Número de genes
    num_genes = 10
    # Probabilidad de mutación
    prob_mutacion = 0.01
    # Número de generaciones
    num_generaciones = 100
    # Esquemas de reemplazo
    reemplazos = [generacional, generacional_elitismo, reemplazo_peores]
    alias_reemplazos = {generacional: "Generacional", generacional_elitismo: "Generacional con elitismo", reemplazo_peores: "Reemplazo de los peores"}

    # Tabla con resultados
    resultados = []
    for funcion, intervalo in zip(funciones, intervalos):
        for reemplazo in reemplazos:
            mejor_solucion = algoritmo_genetico(funcion, intervalo, tamano_poblacion, num_genes, prob_mutacion, num_generaciones, reemplazo)
            resultados.append([funcion.__name__, alias_reemplazos[reemplazo], mejor_solucion])

    # Mostrar tabla con resultados
    print("{:<20} {:<30} {:<20}".format("Función", "Reemplazo", "Mejor solución"))
    for resultado in resultados:

        print("{:<20} {:<30} {:<20}".format(resultado[0], resultado[1], str(resultado[2])))

print("Recocido simulado")
#ejecutar_recocido_simulado()

print("\nAlgoritmo genético")
#ejecutar_algoritmo_genetico()

# LOS RESULTADOS SON:
#Algoritmo genético
#Función              Reemplazo                      Mejor solución      
#sphere               Generacional                   0.005004887585532636
#sphere               Generacional con elitismo      0.005004887585532636
#sphere               Reemplazo de los peores        -0.005004887585532636
#ackley               Generacional                   0.02932551319648269
#ackley               Generacional con elitismo      -0.02932551319648269
#ackley               Reemplazo de los peores        -0.02932551319648269
#griewank             Generacional                   0.5865102639296538
#griewank             Generacional con elitismo      -0.5865102639296538
#griewank             Reemplazo de los peores        -0.5865102639296538
#rastrigin            Generacional                   -0.005004887585532636
#rastrigin            Generacional con elitismo      0.005004887585532636
#rastrigin            Reemplazo de los peores        0.005004887585532636
#rosenbrock           Generacional                   -0.0020019550342129655
#rosenbrock           Generacional con elitismo      -0.0020019550342129655
#rosenbrock           Reemplazo de los peores        0.0020019550342129655

# ¿Cuál es el mejor esquema de reemplazo para cada función de optimización?
# Para la función sphere, los tres esquemas de reemplazo son igualmente efectivos.
# Para la función ackley, los tres esquemas de reemplazo son igualmente efectivos.
# Para la función griewank, el mejor esquema de reemplazo es generacional
# Para la función rastrigin, el mejor esquema de reemplazo es generacional con elitismo
# Para la función rosenbrock, el mejor esquema de reemplazo de los peores

# ¿Qué esquema de reemplazo es el mejor en general?
# El mejor esquema de reemplazo en general es generacional con elitismo
# porque es el que obtiene los mejores resultados en la mayoría de las funciones de optimización.

# ¿Qué esquema de enfriamiento es el mejor en general?
# El mejor esquema de enfriamiento en general es el exponencial

# comparar algoritmo genetico con esquema de reemplazo generacional con elitismo y recocido simulado con esquema de enfriamiento exponencial

# Funciones de optimización
def genetico_vs_recocido():
    funciones = [sphere, ackley, griewank, rastrigin, rosenbrock]
    intervalos = [[-5.12, 5.12], [-30, 30], [-600, 600], [-5.12, 5.12], [-2.048, 2.048]]
    tamano_poblacion = 100
    num_genes = 10
    prob_mutacion = 0.01
    num_generaciones = 100
    reemplazo = generacional_elitismo
    T0 = 100
    n = 0.1
    kmax = 1000
    enfriamiento = enfriamiento_exponencial

    resultados = []
    for funcion, intervalo in zip(funciones, intervalos):
        mejor_solucion_genetico = algoritmo_genetico(funcion, intervalo, tamano_poblacion, num_genes, prob_mutacion, num_generaciones, reemplazo)
        mejor_solucion_recocido = recocido_simulado(funcion, intervalo, num_genes, T0, n, kmax, enfriamiento)
        resultados.append([funcion.__name__, mejor_solucion_genetico, mejor_solucion_recocido])

    print("{:<20} {:<20} {:<20}".format("Función", "Algoritmo genético", "Recocido simulado"))
    for resultado in resultados:
        print("{:<20} {:<20} {:<20}".format(resultado[0], str(resultado[1]), str(resultado[2])))

genetico_vs_recocido()

# resultados
#Función              Algoritmo genético   Recocido simulado   
#sphere               0.005004887585532636 -0.005004887585532636
#ackley               0.02932551319648269  0.02932551319648269 
#griewank             0.5865102639296538   12.316715542522047  
#rastrigin            0.005004887585532636 0.9559335288367548  
#rosenbrock           -0.0020019550342129655 0.13813489736070395 

# ¿Cuál es el mejor algoritmo para cada función de optimización?

#Algoritmo genético: Mejor para "griewank" y "rastrigin".
#Recocido simulado: Mejor para "rosenbrock".
#Ambos algoritmos son comparables para "sphere" y "ackley".
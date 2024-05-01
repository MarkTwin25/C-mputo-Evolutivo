
import numpy as np
import random
import math
import matplotlib.pyplot as plt
from funciones import sphere, ackley, griewank, rastrigin, rosenbrock

from script_1 import *
# Ejercicio 2. Experimentación en Optimización continua

# 2.a) Realizar al menos 30 repeticiones para diferentes funciones de prueba de
# optimización continua, en dimensión 10. *
# 2.b) Fijar criterio de término para todas las ejecuciones, de manera que se tenga una
# comparación justa (por ejemplo con tiempo total de ejecución).
# 2.c) El programa deberá imprimir como salida la semilla del generador de números
# aleatorios que se utilizó para la ejecución
# 2.d) El programa deberá permitir ingresar (como parámetro opcional) la semilla del
# generador de aleatorios con las que se hará la ejecución. Si no se indica nada, el
#programa deberá generar una semilla adecuada.

# *Utiliza las funciones de optimización continua contenidas en el archivo funciones.py

def experimentar_esquemas_enfriamiento(semilla=None):
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
    # Número de repeticiones
    repeticiones = 30
    # Semilla del generador de números aleatorios
    if semilla is None:
        semilla = random.randint(0, 10000)

    random.seed(semilla)
    print("repeticiones: ", repeticiones)
    print("semilla: ", semilla)
    print("{:<20} {:<20} {:<20} {:<20} {:<20}".format("Función", "Enfriamiento", "Promedio", "tempInicial", "numIteraciones"))
    for funcion, intervalo in zip(funciones, intervalos):
        for enfriamiento in enfriamientos:
            promedio = 0
            for _ in range(repeticiones):
                mejor_solucion = recocido_simulado(funcion, intervalo, num_bits, T0, n, kmax, enfriamiento, semilla)
                promedio += funcion([mejor_solucion])
            promedio /= repeticiones
            print("{:<20} {:<20} {:<20} {:<20} {:<20}".format(funcion.__name__, alias_enfriamientos[enfriamiento], promedio, T0, kmax))

# ejecutar con semilla pasado como parámetro
#experimentar_esquemas_enfriamiento(1234)
# ejecutar sin semilla
#experimentar_esquemas_enfriamiento()

def experimentar_esquemas_reemplazo(semilla=None):
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
    # Número de repeticiones
    repeticiones = 30
    # Semilla del generador de números aleatorios
    if semilla is None:
        semilla = random.randint(0, 10000)

    random.seed(semilla)

    # Tabla con resultados
    # formato de la tabla: Función, Reemplazo, Promedio, tamano_poblacion, num_genes, prob_mutacion, num_generaciones, semilla
    print("repeticiones: ", repeticiones)
    print("semilla: ", semilla)
    print("{:<20} {:<30} {:<20} {:<20} {:<20} {:<20} {:<20}".format("Función", "Reemplazo", "Promedio", "tamano_poblacion", "num_genes", "prob_mutacion", "num_generaciones"))
    for funcion, intervalo in zip(funciones, intervalos):
        for reemplazo in reemplazos:
            promedio = 0
            for _ in range(repeticiones):
                mejor_solucion = algoritmo_genetico(funcion, intervalo, tamano_poblacion, num_genes, prob_mutacion, num_generaciones, reemplazo, semilla)
                promedio += funcion([mejor_solucion])
            promedio /= repeticiones
            print("{:<20} {:<30} {:<20} {:<20} {:<20} {:<20} {:<20}".format(funcion.__name__, alias_reemplazos[reemplazo], promedio, tamano_poblacion, num_genes, 
                                                                                                                                prob_mutacion, num_generaciones))

#ejecutar con semilla pasado como parámetro
#experimentar_esquemas_reemplazo()

def experimentar_genetico_vs_recocido(semilla=None):
    # Funciones de optimización
    funciones = [sphere, ackley, griewank, rastrigin, rosenbrock]
    # Límites de los intervalos
    intervalos = [[-5.12, 5.12], [-30, 30], [-600, 600], [-5.12, 5.12], [-2.048, 2.048]]
    # Número de bits
    num_bits = 10
    # Tamaño de la población
    tamano_poblacion = 100
    # Número de genes
    num_genes = 10
    # Probabilidad de mutación
    prob_mutacion = 0.01
    # Número de generaciones
    num_generaciones = 100
    # Esquema de reemplazo
    reemplazo = generacional_elitismo
    # Temperatura inicial
    T0 = 100
    # Parámetro de enfriamiento
    n = 0.1
    # Número máximo de iteraciones
    kmax = 1000
    # Esquema de enfriamiento
    enfriamiento = enfriamiento_exponencial
    # Número de repeticiones
    repeticiones = 30
    # Semilla del generador de números aleatorios
    if semilla is None:
        semilla = random.randint(0, 10000)

    random.seed(semilla)

    # Tabla con resultados
    print("repeticiones: ", repeticiones)
    print("semilla: ", semilla)
    print("{:<20} {:<20} {:<20} {:<20} {:<20}".format("Función", "Algoritmo genético", "Recocido simulado", "tamano_poblacion", "num_genes"))
    for funcion, intervalo in zip(funciones, intervalos):
        promedio_genetico = 0
        promedio_recocido = 0
        for _ in range(repeticiones):
            mejor_solucion_genetico = algoritmo_genetico(funcion, intervalo, tamano_poblacion, num_genes, prob_mutacion, num_generaciones, reemplazo, semilla)
            mejor_solucion_recocido = recocido_simulado(funcion,

            intervalo, num_bits, T0, n, kmax, enfriamiento, semilla)
            promedio_genetico += funcion([mejor_solucion_genetico])
            promedio_recocido += funcion([mejor_solucion_recocido])
        promedio_genetico /= repeticiones
        promedio_recocido /= repeticiones
        print("{:<20} {:<20} {:<20} {:<20} {:<20}".format(funcion.__name__, promedio_genetico, promedio_recocido, tamano_poblacion, num_genes))

# 2.b) Fijar criterio de término para todas las ejecuciones, de manera que se tenga una
# comparación justa (por ejemplo con tiempo total de ejecución).

# El criterio de término es el número de iteraciones, que se fija en 1000 para el recocido simulado y en 100 para el algoritmo genético.
# se eligio este criterio de termino debido a que es un número de iteraciones suficiente para que los algoritmos converjan a una solución.

#ejecutar con semilla pasado como parámetro
#experimentar_genetico_vs_recocido()
import sys

if __name__ == "__main__":

    if sys.argv[1] == "1":
        if len(sys.argv) > 2:
            experimentar_esquemas_enfriamiento(int(sys.argv[2]))
        else:
            experimentar_esquemas_enfriamiento()
    elif sys.argv[1] == "2":
        if len(sys.argv) > 2:
            experimentar_esquemas_reemplazo(int(sys.argv[2]))
        else:
            experimentar_esquemas_reemplazo()
    elif sys.argv[1] == "3":
        if len(sys.argv) > 2:
            experimentar_genetico_vs_recocido(int(sys.argv[2]))
        else:
            experimentar_genetico_vs_recocido()
    else:
        print("Argumento inválido")
        print("1: Experimentar esquemas de enfriamiento")
        print("2: Experimentar esquemas de reemplazo")
        print("3: Experimentar algoritmo genético vs recocido simulado")
        print("Ejemplo de ejecución: python script_2.py 1 1234")
        print("Ejemplo de ejecución: python script_2.py 1")


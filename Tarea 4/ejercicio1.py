# Importamos las librerias necesarias
import numpy as np
import random
import math
import matplotlib.pyplot as plt
import sys
from funciones import sphere, ackley, griewank, rastrigin , rosenbrock 


# 1. Representación binaria para las soluciones
def generar_poblacion(tam_poblacion, tam_solucion):
    """
    Genera una poblacion de tam_poblacion soluciones binarias de tam_solucion bits cada una.

    Args:
    tam_poblacion (int): Tamaño de la poblacion.
    tam_solucion (int): Tamaño de la solucion.

    Returns:
    np.ndarray: Poblacion de tam_poblacion soluciones binarias de tam_solucion bits cada una.
    """
    return np.random.randint(2, size=(tam_poblacion, tam_solucion))

# 2. Selección de padres por el método de la ruleta
def seleccion_ruleta(aptitudes):
    """
    Selecciona dos padres por el metodo de la ruleta.

    Args:
    aptitudes (np.ndarray): Aptitudes de la poblacion.

    Returns:
    np.ndarray: Indices de los padres seleccionados.
    """
    # Calculamos la probabilidad de seleccion de cada individuo
    probabilidad = aptitudes / np.sum(aptitudes)
    # Seleccionamos dos padres
    padres = np.random.choice(np.arange(len(aptitudes)), size=2, p=probabilidad)
    return padres

# 3. Operador de cruza de n puntos
def cruza_n_puntos(padres, n_puntos):
    """
    Cruza dos padres en n_puntos.

    Args:
    padres (np.ndarray): Padres a cruzar.
    n_puntos (int): Numero de puntos de cruza.

    Returns:
    np.ndarray: Hijos resultantes de la cruza.
    """
    # Seleccionamos los puntos de cruza
    puntos = np.sort(np.random.choice(np.arange(len(padres[0])), size=n_puntos, replace=False))
    # Inicializamos los hijos
    hijos = np.zeros_like(padres)
    # Cruza de los padres
    hijos[0, :puntos[0]] = padres[0, :puntos[0]]
    hijos[1, :puntos[0]] = padres[1, :puntos[0]]
    for i in range(1, len(puntos)):
        if i % 2 == 0:
            hijos[0, puntos[i-1]:puntos[i]] = padres[1, puntos[i-1]:puntos[i]]
            hijos[1, puntos[i-1]:puntos[i]] = padres[0, puntos[i-1]:puntos[i]]
        else:
            hijos[0, puntos[i-1]:puntos[i]] = padres[0, puntos[i-1]:puntos[i]]
            hijos[1, puntos[i-1]:puntos[i]] = padres[1, puntos[i-1]:puntos[i]]
    hijos[0, puntos[-1]:] = padres[1, puntos[-1]:]
    hijos[1, puntos[-1]:] = padres[0, puntos[-1]:]
    return hijos

# 4. Mutación flip
def mutacion_flip(individuo, prob_mutacion):
    """
    Muta un individuo con probabilidad prob_mutacion.

    Args:
    individuo (np.ndarray): Individuo a mutar.
    prob_mutacion (float): Probabilidad de mutacion.

    Returns:
    np.ndarray: Individuo mutado.
    """
    for i in range(len(individuo)):
        if np.random.rand() < prob_mutacion:
            individuo[i] = 1 - individuo[i]
    return individuo


# 5. Reemplazo generacional con elitismo
def reemplazo_generacional(poblacion, aptitudes, nueva_poblacion, nueva_aptitudes):
    """
    Reemplaza la poblacion con la nueva_poblacion utilizando elitismo.

    Args:
    poblacion (np.ndarray): Poblacion actual.
    aptitudes (np.ndarray): Aptitudes de la poblacion actual.
    nueva_poblacion (np.ndarray): Nueva poblacion.
    nueva_aptitudes (np.ndarray): Aptitudes de la nueva poblacion.

    Returns:
    np.ndarray: Poblacion reemplazada.
    np.ndarray: Aptitudes de la poblacion reemplazada.
    """
    # Seleccionamos los indices de los individuos a reemplazar
    indices = np.argsort(aptitudes)[:len(nueva_poblacion)] 
    # Reemplazamos los individuos
    poblacion[indices] = nueva_poblacion
    aptitudes[indices] = nueva_aptitudes
    return poblacion, aptitudes


#  algoritmo genetico
def algoritmo_genetico(funcion, tam_poblacion, tam_solucion, n_generaciones, prob_mutacion):
    """
    Implementa un algoritmo genetico para la funcion de optimizacion funcion.

    Args:
    funcion (function): Funcion de optimizacion.
    tam_poblacion (int): Tamaño de la poblacion.
    tam_solucion (int): Tamaño de la solucion.
    n_generaciones (int): Numero de generaciones.
    prob_mutacion (float): Probabilidad de mutacion.

    Returns:
    np.ndarray: Mejor solucion encontrada.
    float: Valor de la mejor solucion.
    float: Valor de la peor solucion.
    list: Aptitudes promedio por generacion.
    list: Aptitudes de la mejor solucion por generacion.
    """
    # Inicializamos la poblacion
    poblacion = generar_poblacion(tam_poblacion, tam_solucion)
    # Inicializamos las aptitudes
    aptitudes = np.zeros(tam_poblacion)
    # Evaluamos la poblacion
    for i in range(tam_poblacion):
        aptitudes[i] = funcion(poblacion[i])
    # Guardamos la mejor solucion
    mejor_solucion = poblacion[np.argmin(aptitudes)]
    # Guardamos el valor de la mejor solucion
    mejor_valor = np.min(aptitudes)
    # Guardamos el valor promedio de la poblacion
    promedio = np.mean(aptitudes)
    # Guardamos el valor de la generacion
    generacion = 0
    # Guardamos los valores de la aptitud de la mejor solucion
    aptitudes_mejor_solucion = [mejor_valor]
    # Guardamos los valores de la aptitud promedio
    aptitudes_promedio = [promedio]
    # Iteramos sobre las generaciones
    while generacion < n_generaciones:
        # Seleccionamos los padres
        padres = seleccion_ruleta(aptitudes)
        # Cruzamos los padres
        hijos = cruza_n_puntos(poblacion[padres], 2)
        # Mutamos los hijos
        hijos[0] = mutacion_flip(hijos[0], prob_mutacion)
        hijos[1] = mutacion_flip(hijos[1], prob_mutacion)
        # Evaluamos los hijos
        aptitudes_hijos = np.array([funcion(hijo) for hijo in hijos])
        # Reemplazamos la poblacion
        poblacion, aptitudes = reemplazo_generacional(poblacion, aptitudes, hijos, aptitudes_hijos)
        # Guardamos la mejor solucion
        mejor_solucion = poblacion[np.argmin(aptitudes)]
        # Guardamos el valor de la mejor solucion
        mejor_valor = np.min(aptitudes)
        # Guardamos el valor promedio de la poblacion
        promedio = np.mean(aptitudes)
        # Guardamos los valores de la aptitud de la mejor solucion
        aptitudes_mejor_solucion.append(mejor_valor)
        # Guardamos los valores de la aptitud promedio
        aptitudes_promedio.append(promedio)
        # Incrementamos la generacion
        generacion += 1
    # Guardamos el peor valor
    peor_valor = np.max(aptitudes)
   
    return mejor_solucion, mejor_valor, peor_valor, aptitudes_promedio, aptitudes_mejor_solucion


# Funcion para graficar
def graficar(funcion_objetivo, nombre_funcion):
    """
    Grafica la convergencia de la funcion_objetivo.
    Args:
    funcion_objetivo (function): Funcion de optimizacion.
    nombre_funcion (str): Nombre de la funcion de optimizacion.
    """  
    num_ejecuciones = 25
    num_generaciones = 100
    tam_poblacion = 100
    tam_solucion = 30
    prob_mutacion = 0.01

    mejores_aptitudes = []

    for i in range(num_ejecuciones):
        _, _, _, aptitudes_promedio, aptitudes_mejor_solucion = algoritmo_genetico(funcion_objetivo, tam_poblacion,
                                                                     tam_solucion, num_generaciones, prob_mutacion)
        mejores_aptitudes.append(aptitudes_mejor_solucion)

    plt.figure()
    for i,aptitudes in enumerate(mejores_aptitudes):
        # Mostrar la ejecucion
        plt.plot(range(num_generaciones+1), aptitudes, label=f'Ejecucion {i+1}')
    plt.xlabel('Generacion')
    plt.legend(bbox_to_anchor=(0.97, 1), loc='upper left')
    plt.ylabel('Aptitud')
    plt.title('Evolución ' + nombre_funcion)
    plt.grid(True)
    plt.show()

# Graficamos todas las funciones
def graficar_funciones():
    funciones = [sphere, ackley, griewank, rastrigin, rosenbrock]
    nombres = ['Sphere', 'Ackley', 'Griewank', 'Rastrigin', 'Rosenbrock']

    for funcion, nombre in zip(funciones, nombres):
        graficar(funcion, nombre)



# Funcion para obtener los resultados estadisticos
def resultados_estadisticos(funcion_objetivo):
    num_ejecuciones = 30
    num_generaciones = 100
    tam_poblacion = 100
    tam_solucion = 30
    prob_mutacion = 0.01

    mejores_valores = []
    peores_valores = []
    valores_promedio = []

    for i in range(num_ejecuciones):
        _, mejor_valor, peor_valor, aptitudes_promedio, _ = algoritmo_genetico(funcion_objetivo, 
                                                            tam_poblacion, tam_solucion, num_generaciones, prob_mutacion)
        mejores_valores.append(mejor_valor)
        peores_valores.append(peor_valor)
        valores_promedio.append(aptitudes_promedio[-1])

    return np.min(mejores_valores), np.max(peores_valores), np.mean(valores_promedio)

def ejecutar_estadisticas():
    # Obtenemos los resultados estadisticos
    resultados = []
    funciones = [sphere, ackley, griewank, rastrigin, rosenbrock]
    nombres = ['Sphere', 'Ackley', 'Griewank', 'Rastrigin', 'Rosenbrock ']
    for funcion in funciones:
        resultados.append(resultados_estadisticos(funcion))

    # Mostramos los resultados en una tabla
    print('Resultados estadisticos')
    print('{:<10}{:<10}{:<10}{:<10}'.format('Funcion', 'Mejor', 'Peor', 'Promedio'))
    for i, nombre in enumerate(nombres):
        print('{:<10}{:<10.4f}{:<10.4f}{:<10.4f}'.format(nombre, resultados[i][0], resultados[i][1], resultados[i][2]))

# ejecutar este script 
if __name__ == '__main__':
    # si se pasa por parametro la palabra 'graficar' se grafican las funciones
    if len(sys.argv) > 1 and sys.argv[1] == 'graficar':
        graficar_funciones()
    # si se pasa por parametro la palabra 'estadisticas' se muestran los resultados estadisticos
    elif len(sys.argv) > 1 and sys.argv[1] == 'estadisticas':
        ejecutar_estadisticas()
    # si no se pasa ningun parametro se ejecutan las funciones
    else:
        graficar_funciones()
        ejecutar_estadisticas()


# ejemplo de ejecucion
# python principal.py graficar

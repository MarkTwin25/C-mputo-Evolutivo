# Importamos la librería numpy para poder trabajar con arreglos
import numpy as np
import sys
########################## Ejercicio 2 ##########################

# Implementa la lectura de archivos para leer información de ejemplares (instancias)

def leer_instancia(nombre_archivo):
    """
    Lee un archivo con información de ejemplares (instancias) del problema de coloración.
    Parameters:
    nombre_archivo -- nombre del archivo a leer
    Returns:
    nVertices -- número de vértices del grafo
    aristas -- lista de aristas del grafo
    """

    # Inicializamos la lista de aristas
    aristas = []
    # Abrimos el archivo
    with open(nombre_archivo, 'r') as archivo:
        # Leemos el archivo línea por línea
        for linea in archivo:
            # Ignoramos las líneas que empiezan con c
            if linea[0] == 'c':
                continue
            # Si encontramos la línea que empieza con p, leemos el número de vértices
            # y aristas
            if linea[0] == 'p':
                _, _, nVertices, nAristas = linea.split() #
                nVertices = int(nVertices)
                nAristas = int(nAristas)
            # Si encontramos la línea que empieza con e, leemos las aristas
            if linea[0] == 'e':
                _, x, y = linea.split()
                x = int(x)
                y = int(y)
                aristas.append((x, y))
    return nVertices, aristas

# Describe e implementa una función de evaluación para las soluciones.

def evaluar_solucion(solucion, nVertices, aristas):
    """
    Evalúa una solución al problema de coloración.
    Parameters:
    solucion -- vector de números enteros que representa la solución
    nVertices -- número de vértices del grafo
    aristas -- lista de aristas del grafo
    Returns:
    valido -- True si la solución es factible, False en otro caso
    """
    # Inicializamos la lista de colores
    colores = [0] * nVertices 
    # Recorremos las aristas
    for x, y in aristas:
        # Si dos vértices adyacentes tienen el mismo color, la solución no es factible
        if solucion[x - 1] == solucion[y - 1]:
            return False
    return True

# Describe e implementa un generador de soluciones aleatorias.

def generar_solucion_aleatoria(nVertices, num_colores):
    """
    Genera una solución aleatoria al problema de coloración.
    Parameters:
    nVertices -- número de vértices del grafo
    num_colores -- número de colores posibles
    Returns:
    solucion -- vector de números enteros que representa la solución
    """
    # Generamos un vector de números enteros aleatorios entre 1 y num_colores
    solucion = np.random.randint(1, num_colores + 1, nVertices)
    return solucion

# Describe e implementa una función u operador de vecindad, acorde al tipo de
#representación implementado en los incisos anteriores.

def vecindad(solucion):
    """
    Genera la vecindad de una solución al problema de coloración.
    Parameters:
    solucion -- vector de números enteros que representa la solución
    Returns:
    vecindad -- lista de soluciones vecinas
    """
    # Inicializamos la lista de soluciones vecinas
    vecindad = []
    # Recorremos los vértices de la solución
    for i in range(len(solucion)):
        # Generamos una copia de la solución
        vecina = solucion.copy()
        # Recorremos los colores posibles
        for color in range(1, max(solucion) + 1):
            # Si el color es diferente al color actual, cambiamos el color del vértice
            if color != solucion[i]:
                vecina[i] = color
                vecindad.append(vecina)
    return vecindad

# Describe e implementa una función de hill climbing para el problema de coloración.
# Usando la representación y operadores definidos en los incisos anteriores.

def hill_climbing(nVertices, aristas, num_colores, max_iter):
    """
    Resuelve el problema de coloración usando hill climbing.
    Parameters:
    nVertices -- número de vértices del grafo
    aristas -- lista de aristas del grafo
    num_colores -- número de colores posibles
    max_iter -- número máximo de iteraciones
    Returns:
    mejor_solucion -- mejor solución encontrada
    """
    # Generamos una solución aleatoria
    solucion = generar_solucion_aleatoria(nVertices, num_colores)
    print(solucion)
    # Evaluamos la solución
    mejor_solucion = solucion
    mejor_fitness = 0
    for i in range(max_iter):
        # Generamos la vecindad de la solución
        vecinos = vecindad(solucion)
        # Evaluamos los vecinos
        for vecino in vecinos:
            if evaluar_solucion(vecino, nVertices, aristas):
                # Si el vecino es mejor que la mejor solución encontrada, actualizamos
                # la mejor solución
                if sum(vecino) > mejor_fitness:
                    mejor_solucion = vecino
                    mejor_fitness = sum(vecino)
        # Actualizamos la solución
        solucion = mejor_solucion
    print("Vecindad de la solucion:",vecindad(solucion))
    print("Evaluacion:" ,evaluar_solucion(solucion, nVertices, aristas))
    return mejor_solucion


nombre_archivo = sys.argv[1]
nVertices, aristas = leer_instancia(nombre_archivo)
solucion = hill_climbing(nVertices, aristas, 3, 10)
print("Solución" ,solucion)
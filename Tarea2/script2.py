# Importamos la librería numpy para poder trabajar con arreglos
import numpy as np

# Función que recibe un número natural y lo convierte a su representación binaria
def binario_a_decimal(arreglo):
    """
    Convierte un número binario a su representación decimal.
    Parameters:
    arreglo -- lista de 0s y 1s que representa el número binario
    Returns:
    decimal -- número decimal
    """
    # Inicializamos la variable que guardará el número decimal
    decimal = 0
    # Recorremos el arreglo de derecha a izquierda
    for i in range(len(arreglo)):
        # Si el bit es 1, sumamos 2^i al número decimal
        if arreglo[len(arreglo) - i - 1] == 1:
            decimal += 2**i
    return decimal

# Función que recibe un número natural y lo convierte a su representación binaria
def decimal_a_binario(n, longitud):
    """
    Convierte un número decimal a su representación binaria.
    Parameters:
    n -- número decimal
    longitud -- número de bits usados para representar el número binario
    Returns:
    binario -- lista de 0s y 1s que representa el número binario
    """
    # Inicializamos el arreglo que guardará el número binario
    binario = np.zeros(longitud, dtype=int)
    # Recorremos el arreglo de derecha a izquierda
    i = longitud - 1
    while n > 0:
        # Si el residuo de dividir n entre 2 es 1, el bit es 1
        if n % 2 == 1:
            binario[i] = 1
        # Dividimos n entre 2
        n = n // 2
        # Decrementamos i
        i -= 1
    return binario   


def codificar(x, num_bits, a, b):
    """
    Codifica un número real en su representación binaria.
    Parameters:
    x -- número real a codificar
    num_bits -- número de bits usados para representar el número real
    a -- límite inferior del intervalo
    b -- límite superior del intervalo
    Returns:
    binario -- lista de 0s y 1s que representa el número real

    """
    
    precision = (b - a) / (2**num_bits)

    # asegura que x esté en el intervalo [a, b]
    x = max(a, min(b, x))

    # calcula el indice del intervalo al que pertenece x
    indice = int((x - a) / precision)

    # codifica el indice en binario
    # Usamos la funcion decimal_a_binario implementada anteriormente
    binario = decimal_a_binario(indice, num_bits)

    return binario

def decodificar(x_cod, num_bits, a, b):
    """
    Decodifica un número real a partir de su representación binaria.
    Parameters:
    x_cod -- lista de 0s y 1s que representa el número real
    num_bits -- número de bits usados para representar el número real
    a -- límite inferior del intervalo
    b -- límite superior del intervalo
    Returns:
    x -- número real decodificado

    """
    # calcula la precision
    precision = (b - a) / (2**num_bits)

    # decodifica el indice del intervalo al que pertenece x
    indice = binario_a_decimal(x_cod)

    # calcula x a partir del indice
    x = a + indice * precision
    return x

# Implementa las funciones necesarias para codificar y decodificar vectores de números reales

def codificar_vector(x, num_bits, a, b):
    """
    Codifica un vector de números reales en su representación binaria.
    Parameters:
    x -- vector de números reales a codificar
    num_bits -- número de bits usados para representar el número real
    a -- límite inferior del intervalo
    b -- límite superior del intervalo
    Returns:
    binario -- lista de listas de 0s y 1s que representa el vector de números reales

    """
    # Usamos la funcion codificar implementada anteriormente
    binario = [codificar(i, num_bits, a, b) for i in x]
    return binario

def decodificar_vector(x_cod, num_bits, a, b):
    """
    Decodifica un vector de números reales a partir de su representación binaria.
    Parameters:
    x_cod -- lista de listas de 0s y 1s que representa el vector de números reales
    num_bits -- número de bits usados para representar el número real
    a -- límite inferior del intervalo
    b -- límite superior del intervalo
    Returns:
    x -- vector de números reales decodificado

    """
    # Usamos la funcion decodificar implementada anteriormente
    x = [decodificar(i, num_bits, a, b) for i in x_cod]
    return x


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
    return mejor_solucion


# evaluar archivo pasado por consola
import sys  

nombre_archivo = sys.argv[1]
nVertices, aristas = leer_instancia(nombre_archivo)
solucion = hill_climbing(nVertices, aristas, 3, 1000)
print(solucion)
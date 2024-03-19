# decodificar
def decodificar(x_cod, intervalo, num_bits):
    """
    Decodifica un número real a partir de su representación binaria.
    Parameters:
    x_cod -- lista de 0s y 1s que representa el número real
    intervalo -- límites del intervalo
    num_bits -- número de bits usados para representar el número real
    Returns:
    x -- número real decodificado
    """
    # Calcula la precisión
    precision = (intervalo[1] - intervalo[0]) / (2**num_bits)
    # Calcula el índice del intervalo al que pertenece x
    indice = sum([x_cod[i] * 2**(num_bits - i - 1) for i in range(num_bits)])
    # Decodifica el índice a un número real
    x = intervalo[0] + indice * precision
    return x

# codificar
def codificar(x, intervalo, num_bits):

    """
    Codifica un número real en su representación binaria.
    Parameters:
    x -- número real a codificar
    intervalo -- límites del intervalo
    num_bits -- número de bits usados para representar el número real
    Returns:
    binario -- lista de 0s y 1s que representa el número real
    """
    # Calcula la precisión
    precision = (intervalo[1] - intervalo[0]) / (2**num_bits)
    # Calcula el índice del intervalo al que pertenece x
    indice = int((x - intervalo[0]) / precision)
    # Codifica el índice a binario
    binario = [int(i) for i in bin(indice)[2:]]
    # Añade ceros a la izquierda si es necesario
    binario = [0] * (num_bits - len(binario)) + binario
    return binario

# Implementa algoritmo de busqueda aleatoria

def busqueda_aleatoria(funcion, intervalo, num_bits, kmax):
    """
    Algoritmo de búsqueda aleatoria para optimizar funciones de optimización continua.
    Parameters:
    funcion -- función a optimizar
    intervalo -- límites del intervalo
    num_bits -- número de bits usados para representar el número real
    kmax -- número máximo de iteraciones
    Returns:
    mejor_solucion -- mejor solución encontrada
    """
    # Inicializa la mejor solución
    mejor_solucion = [random.randint(0, 1) for _ in range(num_bits)]
    # Inicializa la mejor evaluación
    mejor_evaluacion = funcion([decodificar(mejor_solucion, intervalo, num_bits)])
    # Itera hasta alcanzar el número máximo de iteraciones
    for _ in range(kmax):
        # Genera una solución aleatoria
        solucion = [random.randint(0, 1) for _ in range(num_bits)]
        # Decodifica la solución
        x = decodificar(solucion, intervalo, num_bits)
        # Calcula la evaluación de la solución
        evaluacion = funcion([x])
        # Si la solución es mejor que la mejor solución
        if evaluacion < mejor_evaluacion:
            # Actualiza la mejor solución
            mejor_solucion = solucion
            # Actualiza la mejor evaluación
            mejor_evaluacion = evaluacion
    mejor_solucion = decodificar(mejor_solucion, intervalo, num_bits)
    return mejor_solucion

# ejecuta el algoritmo de busqueda aleatoria para optimizar la funciónes
#print(busqueda_aleatoria(sphere, [-5.12, 5.12], 10, 1000))

# print(busqueda_aleatoria(ackley, [-30, 30], 10, 1000))
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
    
    precision = (b - a) / (2**num_bits)
    indice = binario_a_decimal(x_cod)
    #indice = int(''.join([str(i) for i in x_cod]), 2)
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
    
    x = [decodificar(i, num_bits, a, b) for i in x_cod]
    return x



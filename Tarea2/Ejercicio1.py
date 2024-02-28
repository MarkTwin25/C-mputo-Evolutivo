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

# Ejemplo binario_a_decimal
binario_ejemplo = [1, 0, 1, 0] 
decimal_resultado = binario_a_decimal(binario_ejemplo)
print(f"Ejemplo binario_a_decimal: {binario_ejemplo} -> Decimal: {decimal_resultado}")

# Ejemplo decimal_a_binario
decimal_ejemplo = 10
num_bits_ejemplo = 4
binario_resultado = decimal_a_binario(decimal_ejemplo, num_bits_ejemplo)
print(f"Ejemplo decimal_a_binario: Decimal {decimal_ejemplo} -> Binario: {binario_resultado}")

# Ejemplo codificar
x_ejemplo = 0.75
num_bits_codificar = 4
a_codificar = 0.0
b_codificar = 1.0
binario_codificado = codificar(x_ejemplo, num_bits_codificar, a_codificar, b_codificar)
print(f"Ejemplo codificar: Real {x_ejemplo} -> Binario codificado: {binario_codificado}")

# Ejemplo decodificar
binario_decodificar = [1, 0, 0, 1]
num_bits_decodificar = 4
a_decodificar = 0.0
b_decodificar = 1.0
x_decodificado = decodificar(binario_decodificar, num_bits_decodificar, a_decodificar, b_decodificar)
print(f"Ejemplo decodificar: Binario {binario_decodificar} -> Real decodificado: {x_decodificado}")

# Ejemplo codificar_vector
vector_ejemplo = [0.2, 0.5, 0.8]
num_bits_codificar_vector = 4
a_codificar_vector = 0.0
b_codificar_vector = 1.0
vector_codificado = codificar_vector(vector_ejemplo, num_bits_codificar_vector, a_codificar_vector, b_codificar_vector)
print(f"Ejemplo codificar_vector: Vector {vector_ejemplo} -> Vector codificado: {vector_codificado}")

# Ejemplo decodificar_vector
vector_binario_decodificar = [[1, 0, 0, 1], [0, 1, 0, 1], [1, 1, 1, 1]]
num_bits_decodificar_vector = 4
a_decodificar_vector = 0.0
b_decodificar_vector = 1.0
vector_decodificado = decodificar_vector(vector_binario_decodificar, num_bits_decodificar_vector, a_decodificar_vector, b_decodificar_vector)
print(f"Ejemplo decodificar_vector: Vector binario {vector_binario_decodificar} -> Vector decodificado: {vector_decodificado}")

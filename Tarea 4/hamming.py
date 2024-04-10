import random

import random

# Función para generar una cadena de bits aleatoria de longitud n
def generar_cadena(n):
    return ''.join(random.choice('01') for _ in range(n))

# Función para calcular los bits de paridad de Hamming
def hamming(mensaje):
    # Convertimos el mensaje en una lista de enteros para facilitar la manipulación
    mensaje = [int(bit) for bit in mensaje]
    
    # Calculamos el número de bits de paridad
    r = 0
    while 2**r < len(mensaje) + r + 1:
        r += 1

    # Creamos la cadena de bits de paridad
    bitsParidad = [0 for i in range(r)]
    for i in range(r):
        bitsParidad[i] = 2**i

    # Creamos la cadena de bits de datos
    bitsDatos = [0] * (len(mensaje) + r)
    j = 0
    for i in range(1, len(bitsDatos) + 1):
        if i in bitsParidad:
            continue
        bitsDatos[i-1] = mensaje[j]
        j += 1

    # Calculamos los bits de paridad
    for i in range(r):
        x = 2**i
        for j in range(x - 1, len(bitsDatos), x*2):
            for k in range(x):
                if j+k < len(bitsDatos):
                    bitsDatos[x-1] ^= bitsDatos[j+k]

    # Convertimos los bits de datos a una cadena de caracteres
    return ''.join(str(bit) for bit in bitsDatos)

# Funcion para simular un error en la cadena a transmitir
def simular_error(cadena):
    error_pos = random.randint(0, len(cadena) - 1)
    cadena_erronea = cadena[:error_pos] + str(1 - int(cadena[error_pos])) + cadena[error_pos + 1:]
    # Retornar la cadena con el error y la posición del error
    return cadena_erronea, error_pos
    

# Funcion para detectar y corregir un error en la cadena recibida
def detectar_corregir_error(cadena):
    n = len(cadena)
    r = 0
    while (2**r) < (n + r + 1):
        r += 1
    error_pos = 0
    # Calcular la posición del error
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if j & (2**i) == (2**i):
                val = val ^ int(cadena[-j])
        error_pos += val * (2**i)
    if error_pos:
        cadena = cadena[:n-error_pos] + str(1 - int(cadena[n-error_pos])) + cadena[n-error_pos+1:]
    return cadena, error_pos

# Generar la cadena original
cadena_original = generar_cadena(10)
# Hammear la cadena original
cadena_transmitida = ''.join(map(str, hamming(list(map(int, cadena_original)))))
# Simular un error en la cadena transmitida
cadena_con_error, error_pos = simular_error(cadena_transmitida)
# Detectar y corregir el error
cadena_corregida, _ = detectar_corregir_error(cadena_con_error)


# Mostrar resultados
print(f"Cadena original: {cadena_original}")
print(f"Cadena transmitida (con bits de paridad): {cadena_transmitida}")
print(f"Cadena con error: {cadena_con_error}")
print(f"Posición del error: {error_pos + 1}")
print(f"Cadena corregida: {cadena_corregida}")

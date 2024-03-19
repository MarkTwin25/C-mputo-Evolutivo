import random

def generar_vecino(solucion, num_cambios=1):
    """Genera un vecino de la solución dada cambiando un número específico de bits."""
    vecino = list(solucion)
    indices_a_cambiar = random.sample(range(len(solucion)), num_cambios)
    for indice in indices_a_cambiar:
        vecino[indice] = 1 - vecino[indice]  # Cambiar de 0 a 1 o de 1 a 0
    return vecino

# Rastringin 

import math

def rastringin(x: list):
    """
    Rastringin con x lista
    :param x: lista de valores
    """
    suma = 0
    for i in range(len(x)):
        suma += x[i] ** 2 - 10 * math.cos(2 * math.pi * x[i])
    return 10 * len(x) + suma

def rosembrock(x: list):
    """
    Rosembrock con x lista
    :param x: lista de valores
    """
    suma = 0
    for i in range(len(x) - 1):
        suma += 100 * (x[i + 1] - x[i] ** 2) ** 2 + (x[i] - 1) ** 2
    return suma


def griewank(x: list):
    """
    Griewank con x lista
    :param x: lista de valores
    """
    suma = 0
    producto = 1
    for i in range(len(x)):
        suma += x[i] ** 2 / 4000
        producto *= math.cos(x[i] / math.sqrt(i + 1))
    return suma - producto + 1

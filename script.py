
# Imports 
import math # bibloteca para manejar operaciones matematicas
import sys # bibloteca para manejar argumentos de la linea de comandos

# Funcion Rastringin
def rastringin(x: list, dimension: int):
    suma = 0
    for i in range(dimension):
        suma += x[i] ** 2 - 10 * math.cos(2 * math.pi * x[i])
    return 10 * dimension + suma

# Funcion Rosenbrock
def rosembrock(x: list, dimension: int):
    suma = 0
    for i in range(dimension - 1):
        suma += 100 * (x[i + 1] - x[i] ** 2) ** 2 + (x[i] - 1) ** 2
    return suma

# Funcion Schwefel
def schwefel(x: list, dimension: int):
    suma = 0
    for i in range(dimension):
        suma += x[i] * math.sin(math.sqrt(abs(x[i])))
    return 418.9829 * dimension - suma

# Evaluar funcion
def evaluar(funcion: str, dimension: int, *args):
    """
    Evalua una funcion en un punto dado y
    dependiendo de la funcion que se le pase
    evalua la funcion correspondiente con los
    argumentos dados y su dimension.
    """

    if funcion == "rastringin":
        print(rastringin(list(args), dimension)) 
    elif funcion == "rosembrock":
        print(rosembrock(list(args), dimension))
    elif funcion == "schwefel":
        print(schwefel(list(args), dimension))
    else:
        print("Funcion no encontrada")



if __name__ == "__main__":
# Se espera que se pase la funcion, la dimension y los argumentos
    if len(sys.argv) < 4: # Si no se pasan los argumentos necesarios se termina el programa
        print("Faltan argumentos")
        sys.exit(1)

    # Se obtienen los argumentos
    funcion = sys.argv[1]
    dimension = int(sys.argv[2])
    args = [float(x) for x in sys.argv[3:]]

    # Se evalua la funcion
    resultado = evaluar(funcion, dimension, *args)
    # Se imprime el resultado en terminal
    print(resultado)
    





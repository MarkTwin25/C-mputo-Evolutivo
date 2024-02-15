
# Imports 
import math # bibloteca para manejar operaciones matematicas
import sys # bibloteca para manejar argumentos de la linea de comandos
import random # bibloteca para manejar numeros aleatorios

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
        return rastringin(list(args), dimension)
    elif funcion == "rosembrock":
        return rosembrock(list(args), dimension)
    elif funcion == "schwefel":
        return schwefel(list(args), dimension)
    else:
        print("Funcion no encontrada")


# Funcion de busqueda aleatoria

def busqueda_aleatoria(funcion: str, dimension: int, iteraciones: int, intervalo: list):
    """
    Realiza una busqueda aleatoria para encontrar el minimo de una funcion
    dada en un intervalo dado.
    """
   # Se genera el primer punto aleatorio
    punto = [random.uniform(intervalo[0], intervalo[1]) for _ in range(dimension)]
    # Se inicializa la mejor y peor solucion encontrada con el primer punto
    mejor_solucion = punto
    peor_solucion = punto
    promedio = 0

    # Se realiza la busqueda aleatoria
    for _ in range(iteraciones):
        # Se genera un punto aleatorio
        punto = [random.uniform(intervalo[0], intervalo[1]) for _ in range(dimension)]
        # Se evalua la funcion en el punto
        resultado = evaluar(funcion, dimension, *punto)
        # Se compara el resultado con el mejor resultado encontrado
        if resultado < evaluar(funcion, dimension, *mejor_solucion):
            mejor_solucion = punto
            # promedio de los valores encontrados
            
        if resultado > evaluar(funcion, dimension, *peor_solucion):
            peor_solucion = punto
        
        promedio += resultado
        # promedio de los valores encontrados
    promedio_a =  promedio / iteraciones
    print("Mejor solucion encontrada:")
    print(f"x = {mejor_solucion}")
    print(f"f(x) = {evaluar(funcion, dimension, *mejor_solucion)}")
    print("Peor solucion encontrada:")
    print(f"x = {peor_solucion}")
    print(f"f(x) = {evaluar(funcion, dimension, *peor_solucion)}")
    print("Valor promedio:")
    print(f"x = {promedio_a}")



if __name__ == "__main__":
# Se espera que se pase la funcion, la dimension y los argumentos 
    if sys.argv[1] == "busqueda_aleatoria":
    # Se espera que se pase la funcion, la dimension, el numero de iteraciones y el intervalo
        if len(sys.argv) < 6: # Si no se pasan los argumentos necesarios se termina el programa
            print("Faltan argumentos")
            sys.exit(1)

        # Se obtienen los argumentos
        funcion = sys.argv[2]
        dimension = int(sys.argv[3])
        iteraciones = int(sys.argv[4])
        intervalo = [float(x) for x in sys.argv[5:]]
        # Se realiza la busqueda aleatoria
        busqueda_aleatoria(funcion, dimension, iteraciones, intervalo)
    else:

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
        





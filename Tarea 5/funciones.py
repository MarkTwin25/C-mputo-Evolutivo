import math

# a. Sphere con x_i ∈ [-5.12, 5.12]
def sphere(x):
    """Sphere function."""
    # Excepcion si x_i no esta en el intervalo
    if not all(-5.12 <= i <= 5.12 for i in x):
        raise ValueError("x_i debe estar en el intervalo [-5.12, 5.12]")
    return sum([i**2 for i in x])

# b. Ackley con x_i ∈ [-30, 30]

def ackley(x):
    """Ackley function."""
    # Excepcion si x_i no esta en el intervalo
    if not all(-30 <= i <= 30 for i in x):
        raise ValueError("x_i debe estar en el intervalo [-30, 30]")
    a = 20
    b = 0.2
    c = 2 * 3.14159
    d = len(x)
    sum1 = sum([i**2 for i in x])
    sum2 = sum([math.cos(c * i) for i in x])
    return -a * math.exp(-b * math.sqrt(sum1 / d)) - math.exp(sum2 / d) + a + math.exp(1)


# c. Griewank con x_i ∈ [-600, 600]

def griewank(x):
    """Griewank function."""
    # Excepcion si x_i no esta en el intervalo
    if not all(-600 <= i <= 600 for i in x):
        raise ValueError("x_i debe estar en el intervalo [-600, 600]")
    sum1 = sum([i**2 for i in x])
    prod = 1
    for i in range(len(x)):
        prod *= math.cos(x[i] / math.sqrt(i + 1))
    return 1 + sum1 / 4000 - prod

# d. Rastrigin con x_i ∈ [-5.12, 5.12]

def rastrigin(x):
    """Rastrigin function."""
    # Excepcion si x_i no esta en el intervalo
    if not all(-5.12 <= i <= 5.12 for i in x):
        raise ValueError("x_i debe estar en el intervalo [-5.12, 5.12]")
    return 10 * len(x) + sum([i**2 - 10 * math.cos(2 * math.pi * i) for i in x])


# e. Rosenbrock con x_i ∈ [-2.048, 2.048]

def rosenbrock(x):
    """Rosenbrock function."""
    # Excepcion si x_i no esta en el intervalo
    if not all(-2.048 <= i <= 2.048 for i in x):
        raise ValueError("x_i debe estar en el intervalo [-2.048, 2.048]")
    return sum([100 * (x[i + 1] - x[i]**2)**2 + (x[i] - 1)**2 for i in range(len(x) - 1)])
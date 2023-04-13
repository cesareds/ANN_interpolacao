from sympy import *
import math

# Definindo a função f(x)
def f(x):
    return math.exp(-x**2) +math.cos(x) + 3
    # return x ** 5 - 4 * x ** 2 + 2 * math.sqrt(x + 1) + math.cos(x)
    # return 4 + math.sin(x) - (x ** 2) / 30

# Definindo a função para calcular o polinômio interpolador
def interpolador(x, y):
    n = len(x)
    c = y.copy()
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            c[i] = (c[i] - c[i-1])/(x[i] - x[i-j])
    def p(t):
        result = c[n-1]
        for i in range(n-2, -1, -1):
            result = result * (t - x[i]) + c[i]
        return result
    return p

# Dados do problema
x = [0.493, 1.382, 1.951, 2.511, 3.688, 4.132, 5.251, 5.988, 6.592]
values = [0.624, 0.866, 1.643, 4.945, 5.226]
y = [f(xi) for xi in x]


# Encontrando o polinômio interpolador
p = interpolador(x, y)

# Calculando os erros absolutos
errors = [abs(f(xi) - p(xi)) for xi in values]

# Imprimindo os erros absolutos separados por vírgula
print(','.join(map(str, errors)))

# import math
# import random

# def calculate_PL(d):
#     n = 5
#     X = random.gauss(0, 4.78)  # Gera um número aleatório com distribuição normal (média 0 e desvio padrão 1)
#     PL = 102.125 + 10 * n * math.log10(d / 1260) + X
#     return PL

# # Exemplo de uso
# d = 3580 # Valor de d para o cálculo do PL


# result = calculate_PL(d)
# print(f"O valor de PL para d = {d} é: {result}")
# print(f"O valor de RSSI para d = {d} é : {result - 14}")

import math
import random

def calculate_PL(d):
    n = 3.57
    X = random.gauss(0,4.78)  # Gera um número aleatório com distribuição normal (média 0 e desvio padrão 1)
    #4.78
    #28.29
    PL_D0 = 14 + 89 + 5 + 2.1
    print("PL D0: ", PL_D0)
    PL = PL_D0 + 10 * n * math.log10(d / 1260) + X
    return PL


# Exemplo de uso
d = 100 # Valor de d para o cálculo do PL
limiar = -117  # Limiar de sensibilidade do receptor

count_below_threshold = 0  # Contador para valores menores que -117

for _ in range(10):
    result = calculate_PL(d)
    print(f"O valor de PL para d = {d} é: {result}")
    rssi = result - 21
    print(f"O valor de RSSI para d = {d} é: {rssi}")
    
    if - rssi < limiar:
        count_below_threshold += 1

print(f"Quantidade de valores menores que -117: {count_below_threshold}")
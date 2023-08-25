import math
import numpy as np

def calcular_a_hm(fc, hm):
    return (1.11 * math.log10(fc) - 0.7) * hm - (1.56 * math.log10(fc) - 0.8)

def calcular_K1(fc, hb, hm):
    a_hm = calcular_a_hm(fc, hm)
    return 69.5 + 26.16 * math.log10(fc) - 13.82 * math.log10(hb) - a_hm

def calcular_K2(hb):
    return 44.9 - 6.55 * math.log10(hb)

# Valores de entrada
fc = 915 # MHz
hb = 80 # m
hm = 1.5 # m

# Cálculo dos coeficientes K1 e K2
K1 = calcular_K1(fc, hb, hm)
K2 = calcular_K2(hb)

# Exibição dos resultados
print("Coeficiente K1:", K1)
print("Coeficiente K2:", K2)

pl =  K1 + K2 * np.log10(2500/1000)
rssi = pl - 14 - 2 - 5
print("PL ", pl)
print("RSSI ", rssi)
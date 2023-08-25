import sympy as sp
import numpy as np

# Definindo a variável simbólica
n = sp.symbols('n')



d0 = 1260
p0 = -89

#p1 = -82.85 - 10*n*np.log10(40/40)
# p2 = p0 - 10*n*np.log10(1260/d0)
p2 = p0 - 10*n*np.log10(1530/d0)
p3 = p0 - 10*n*np.log10(1980/d0)
p4 = p0 - 10*n*np.log10(2500/d0)
p5 = p0 - 10*n*np.log10(3000/d0)
p6 = p0 - 10*n*np.log10(3580/d0)
#p7 = p0 - 10*n*np.log10(3580/d0)
# p5 = p0 - 10*n*np.log10(3050/d0)
# p6 = p0 - 10*n*np.log10(3580/d0)
print(p2)
print(p3)
print(p4)
# print(p5)
# print(p6)
#p1 = -82.85
#p1_0 = -82.85
#p2_0 = -89
p2_0 = -88.95
p3_0 = -92.76
p4_0 = -94
p5_0 = -99.31
p6_0 = -113.81



# Definindo a função
pt2 = p2_0 - p2
pt3 = p3_0 - p3
pt4 = p4_0 - p4
pt5 = p5_0 - p5
pt6 = p6_0 - p6
#pt7 = p7_0 - p7
print(pt2)
print(pt3)
print(pt4)
print(pt5)
print(pt6)
funcao = pt2**2  + pt3**2 +  pt4**2 + pt5**2 + pt6**2
#pt5**2 +  pt6**2
# pt2 = (p2_0 - p2)**2
# #funcao = (p2_0 - p2)**2 
print(funcao)
# Calculando a derivada em relação a n

derivada = sp.diff(funcao, n)
valor_n = sp.solve(derivada, n) 
# Imprimindo a derivada
print(derivada)
print(valor_n)




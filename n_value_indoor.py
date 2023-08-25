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
p5 = p0 - 10*n*np.log10(3050/d0)
p6 = p0 - 10*n*np.log10(3580/d0)


#p1 = -82.85
#p1_0 = -82.85
#p2_0 = -89
p2_0 = -88.95454545 
p3_0 = -92.76315789 
p4_0 = -94 
p5_0 = -99.31578947 
p6_0 = -113.81818182 


# Definindo a função
funcao = (p2_0 - p2)**2  + (p3_0 - p3)**2 + (p4_0 - p4)**2 + (p5_0 - p5)**2 + (p6_0 - p6)**2
# pt2 = (p2_0 - p2)**2
# #funcao = (p2_0 - p2)**2 
# print(pt2)
# Calculando a derivada em relação a n

derivada = sp.diff(funcao, n)
valor_n = sp.solve(derivada, n) 
# Imprimindo a derivada
print(derivada)
print(valor_n)




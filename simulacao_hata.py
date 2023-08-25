import matplotlib.pyplot as plt

# Valores fornecidos
distancias = [1260, 1530, 1980, 2500, 3000, 3580]
PL_valores = [-109.855017, -112.589543, -116.220852, -119.505194, -122.073042, -124.562427]

# Criação do gráfico
plt.plot(distancias, PL_valores, marker='o')
plt.xlabel('Distância (d)')
plt.ylabel('Path Loss (PL)')
plt.title('Path Loss em função da Distância')
plt.grid(True)

# Exibição do gráfico
plt.show()
import numpy as np
import matplotlib.pyplot as plt

distancia = [55, 55, 58, 86, 86, 86, 90, 90, 111, 111, 111]
rssi = [-72.10, -81.78, -73.40, -69.50, -83.32, -77.77, -68.05, -77.02, -70.52, -79.67, -80.40]

# Calcula a média dos valores de RSSI para as mesmas distâncias
distancia_unicas = np.unique(distancia)
rssi_media = [np.mean([rssi[i] for i in range(len(distancia)) if distancia[i] == d]) for d in distancia_unicas]
print(distancia_unicas)
print(rssi_media)

# Plota o gráfico de distância x RSSI médio
plt.plot(distancia_unicas, rssi_media, marker='o', linestyle='-', color='b')
plt.xlabel('Distância (m)')
plt.ylabel('RSSI Médio (dBm)')
plt.title('Gráfico de Distância x RSSI Médio')
plt.grid(True)
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Distâncias em metros
distancias = [1260, 1530, 1980, 2500, 3050, 3580]
acertos = [17/32, 22/40, 38/80, 39/80, 19/40, 11/28]
index = range(len(distancias))
plt.bar(index, acertos)
plt.xlabel('Distância (metros)', fontsize=14)
plt.ylabel('Data Extraction Rate (DER)', fontsize=14)
plt.title('Gráfico de DER em função da Distância', fontsize=16)
plt.xticks([i for i in index], distancias)  # Define os rótulos do eixo x
plt.yticks(fontsize=13)
plt.xticks(fontsize=13)
plt.show()
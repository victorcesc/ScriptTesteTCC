import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Leitura dos dados do arquivo CSV
df = pd.read_csv('dados_coletados/dados_com_visada.csv')

# Agrupamento dos dados por distância
grouped_data = df.groupby('distancia')['rssi']

# Cria uma lista de listas com os valores de SNR para cada distância
data = [list(data) for distance, data in grouped_data]

# Plot do box plot com os quartis
box_plot = plt.boxplot(data, showfliers=False, medianprops={'color': 'red'}, patch_artist=True)

# Definir cores para cada caixa
colors = ['lightblue', 'lightgreen', 'lightyellow', 'lightpink','lightcoral','lightgray']
for patch, color in zip(box_plot['boxes'], colors):
    patch.set(facecolor=color)

# Adicionar os valores de mediana no gráfico
medians = [round(median, 2) for median in grouped_data.median()]
for i, median in enumerate(medians, start=1):
    plt.text(i, median, str(median), horizontalalignment='center', verticalalignment='bottom', fontweight='bold',fontsize = 13)

# Configuração dos rótulos do eixo x
plt.xticks(range(1, len(grouped_data) + 1), grouped_data.groups.keys(), rotation=0)
plt.xlabel('Distância(m)',fontsize = 15)
plt.grid(True)
plt.yticks(fontsize=13)
plt.xticks(fontsize=13)
# Configuração dos rótulos do eixo y
plt.ylabel('RSSI',fontsize = 15)

# Exibe o gráfico
plt.title('Box Plot - RSSI por Distância')
plt.show()

import matplotlib.pyplot as plt

distancia = [1260, 1530, 1980, 2500, 3000, 3580]
der_lognormal = [1, 1, 0.965116, 0.883721, 0.848837, 0.639535]
der_real = [17/32, 22/40, 38/80,  39/80, 19/40, 11/28]
der_hataokumura = [1, 1, 1, 0, 0, 0]

bar_width = 0.25  # Largura das barras
index = range(len(distancia))

plt.bar(index, der_lognormal, width=bar_width, color='b', label='Log Normal')
plt.bar([i + bar_width for i in index], der_hataokumura, width=bar_width, color='r', label='Hata Okumura')
plt.bar([i + 2*bar_width for i in index], der_real, width=bar_width, color='g', label='Real')

plt.xlabel('Distância', fontsize=14)
plt.ylabel('Data Extraction Rate (DER)', fontsize=14)
plt.title('Gráfico de DER em função da Distância', fontsize=16)

plt.xticks([i + bar_width for i in index], distancia)  # Define os rótulos do eixo x
plt.yticks(fontsize=13)
plt.xticks(fontsize=13)

plt.legend(fontsize=12)  # Adiciona a legenda

plt.show()
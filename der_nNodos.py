import matplotlib.pyplot as plt

n_nodos = [100, 200, 500]
der_lognormal = [0.387879,0.219500,0.095985]
# der_real = [17/32, 22/40, 38/80,  39/80, 19/40, 11/28]
# der_hataokumura = [1, 1, 1, 0, 0, 0]

bar_width = 0.25  # Largura das barras
index = range(len(n_nodos))

plt.bar(index, der_lognormal, width=bar_width)
# plt.bar([i + bar_width for i in index], der_hataokumura, width=bar_width, color='r', label='Hata Okumura')
# plt.bar([i + 2*bar_width for i in index], der_real, width=bar_width, color='g', label='Real')

plt.xlabel('Numero de nodos para', fontsize=14)
plt.ylabel('Data Extraction Rate (DER)', fontsize=14)
plt.title('Gráfico de DER x Numero de nodos', fontsize=16)

plt.xticks([i for i in index], n_nodos)  # Define os rótulos do eixo x
plt.yticks(fontsize=13)
plt.xticks(fontsize=13)

plt.legend(fontsize=12)  # Adiciona a legenda

plt.show()
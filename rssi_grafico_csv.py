import pandas as pd
import matplotlib.pyplot as plt

# Ler os dados do arquivo CSV
data = pd.read_csv('dados_com_visada.csv')


print(data)
# Calcular a média dos valores de RSSI para cada distância
media_rssi = data.groupby('distancia')['rssi'].mean()
media_snr = data.groupby('distancia')['snr'].mean()
print(media_rssi)
distancia = data['distancia']
rssi = data['rssi']
snr = data['snr']

num_distancias = len(distancia)
cores = plt.cm.get_cmap('jet', num_distancias)

# Extrair os valores de distância e rssi
distancia_media = media_rssi.index.tolist()
rssi_media = media_rssi.values
snr_media = media_snr.values




print(distancia_media)
print(rssi_media)

# Criar o gráfico
plt.figure(1)
plt.plot(distancia_media, rssi_media, 'o-')
plt.plot(distancia_media,snr_media, 'x-')
plt.yticks(fontsize=13)
plt.xticks(fontsize=13)
linhas = [plt.Line2D([], [], color='blue', marker='o', linestyle='-'),
          plt.Line2D([], [], color='orange', marker='x', linestyle='-')]

plt.legend(linhas, ['RSSI', 'SNR'])
plt.xlabel('Distância', fontsize = 14)
plt.ylabel('RSSI/SNR', fontsize = 14)
#plt.title('Gráfico de Média de RSSI em relação à Distância')
plt.grid(True)
# plt.xlim(0, max(distancia_media) * 1.1)
# plt.ylim(0, max(rssi_media) * 1.1)
# for x, y in zip(distancia_media, rssi_media):
#     plt.text(x, y, f'({x}, {round(y, 2)})')

plt.figure(2)
plt.scatter(distancia,rssi,c=distancia, cmap=cores)

plt.xlabel('Distância', fontsize = 14)
plt.ylabel('RSSI', fontsize = 14)
plt.yticks(fontsize=13)
plt.xticks(fontsize=13)

#plt.title('Gráfico de Dispersão de RSSI em relação à Distância')


plt.figure(3)
plt.scatter(distancia,snr,c=distancia, cmap=cores)

plt.xlabel('Distância', fontsize = 14)
plt.ylabel('SNR', fontsize = 14)
plt.yticks(fontsize=13)
plt.xticks(fontsize=13)
#plt.title('Gráfico de Dispersão de SNR em relação à Distância')
plt.show()
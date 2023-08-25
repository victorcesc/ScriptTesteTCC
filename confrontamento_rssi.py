import matplotlib.pyplot as plt

distancia = [1260, 1530, 1980, 2500, 3000, 3580]
# log_normal_perdas = [-89.06, -92.82, -98.04, -103.93,  -107.19, -109.88]
# hata_okumura_perdas = [-106.333192, -109.067718, -112.699027, -115.983369, -118.551217, -121.040601]
real_perdas = [-89,-88.95,-92.76,-94,-99.31,-113.81]

# plt.plot(distancia, log_normal_perdas, marker='o', linestyle='-', color='b', label='Log Normal')
# plt.plot(distancia, hata_okumura_perdas, marker='s', linestyle='-', color='r', label='Hata Okumura')
plt.plot(distancia, real_perdas, marker='o', linestyle='-', color='b', label='Real')
plt.xlabel('Distância (m)')
plt.ylabel('Perdas (dB)')
plt.title('Gráfico de Perdas x Distância')

plt.xlabel('Distância(m)', fontsize = 14)
plt.ylabel('RSSI(dBm)', fontsize = 14)
plt.yticks(fontsize=13)
plt.xticks(fontsize=13)
plt.grid(True)
plt.legend()
plt.show()
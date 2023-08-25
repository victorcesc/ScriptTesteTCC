import matplotlib.pyplot as plt

# Taxas de extração de dados para nodos
nodos = [50, 200, 500, 1000]

# Intervalos de numero de gw
intervalos = [1, 2, 4, 8]

# Dados simulados de taxa de extração (exemplo)
# 60s
taxas60 = [
    [0.67,0.29,0.11,0.05], #1gw v
    [0.81,0.48,0.23,0.11],  #2gw v
    [0.83,0.54,0.31,0.19],  #4gw v
    [0.95,0.78,0.56,0.37]   #8 v
]
taxas300 = [    
    [0.81,0.50,0.24,0.12], #1gw v
    [0.92,0.69,0.43,0.24],  #2gw v
    [0.91,0.73,0.50,0.32],  #4gw v
    [0.97,0.90,0.75,0.57]   #8 v
]
taxas500 = [    
    [0.87,0.60,0.33,0.18], #1gw v
    [0.92,0.77,0.54,0.33],  #2gw v
    [0.93,0.80,0.59,0.40],  #4gw v
    [0.98,0.93,0.82,0.67]   #8 v
]


marcadores = ['x', 'o', 's', '^']
# Configuração do gráfico
plt.figure(figsize=(10, 6))
plt.title('Taxa de Extração de Dados 60s de intervalo de msg',fontsize= 14)
plt.xlabel('Nodos',fontsize= 14)
plt.ylabel('Taxa de Extração (DER)',fontsize= 14)

# Plotagem das linhas pontilhadas com marcadores menores
for i in range(len(intervalos)):
    plt.plot(nodos, taxas60[i], linestyle='--', marker=marcadores[i], markersize=4, label= str(intervalos[i]) + 'gateway(s)')

# Definindo os valores do eixo x
plt.xticks(nodos)
plt.ylim(0, 1)
plt.yticks(fontsize=13)
plt.xticks(fontsize=13)
# Adicionando a legenda
plt.legend()

# Exibindo o gráfico
plt.show()

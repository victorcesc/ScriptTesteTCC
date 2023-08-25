import matplotlib.pyplot as plt

# Taxas de extração de dados para nodos
nodos = [50, 200, 500, 1000]

# Intervalos de envio de dados
gateways = [1]

# Dados simulados de taxa de extração (exemplo)
taxas60 = [258, 2228, 7004, 14852]
taxas300 = [72, 748, 2923, 6713]
taxas500 = [35, 431, 1821, 4370]

marcadores = ['x', 'o', 's', '^']

# Configuração do gráfico
plt.figure(figsize=(10, 6))
plt.title('Número de Colisões de Pacotes por Nodos e Intervalos', fontsize=14)
plt.xlabel('Nodos', fontsize=14)
plt.ylabel('Colisões', fontsize=14)

# Plotagem das linhas pontilhadas com marcadores
plt.plot(nodos, taxas60, linestyle='--', marker=marcadores[0], markersize=4, label='60s')
plt.plot(nodos, taxas300, linestyle='--', marker=marcadores[1], markersize=4, label='300s')
plt.plot(nodos, taxas500, linestyle='--', marker=marcadores[2], markersize=4, label='500s')

# Definindo os valores do eixo x
plt.xticks(nodos, fontsize=13)
plt.yticks(fontsize=13)

# Adicionando a legenda
plt.legend()

# Exibindo o gráfico
plt.show()

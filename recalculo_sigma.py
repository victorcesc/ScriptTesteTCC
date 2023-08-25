import numpy as np
import json

# Caminho do arquivo JSON
caminho_arquivo = "experimento2-indoor/labFisica_2andar_111m.json"

# Limiar de sensibilidade do receptor
limiar = -117

# Lista para armazenar os valores conhecidos de RSSI
rssi_conhecidos = []

# Ler os valores do arquivo JSON
with open(caminho_arquivo, 'r') as arquivo:
    dados_json = arquivo.readlines()

# Extrair os valores conhecidos de RSSI
for linha in dados_json:
    # Converter a linha JSON em um dicionário Python
    dados = json.loads(linha)

    # Extrair o valor de RSSI
    rssi = dados["rssi"]

    # Adicionar o valor de RSSI à lista de valores conhecidos
    rssi_conhecidos.append(rssi)

# Calcular a média e o desvio padrão dos valores conhecidos
media_observada = np.mean(rssi_conhecidos)
desvio_padrao_observado = np.std(rssi_conhecidos)

print(media_observada)

# Gerar 15 valores estimados menores que -117
valores_estimados = np.random.normal(loc=limiar, scale=desvio_padrao_observado, size=17)

print(valores_estimados)
valores_estimados = np.where(valores_estimados < limiar, valores_estimados, limiar)
valores_estimados= np.array(valores_estimados)
print(valores_estimados)
# Imprimir os valores estimados
# print("Valores Estimados:")
# for valor in valores_estimados:
#     print(valor)

rssi =  np.concatenate((rssi_conhecidos,valores_estimados))
rssi = np.mean(rssi)
print(rssi)
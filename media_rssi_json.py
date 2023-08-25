import json

# Abrir o arquivo JSON
with open('experimento2-indoor/salaCulturaGeral_1andar_91m.json') as file:
    data = file.readlines()

# Variáveis para armazenar a soma dos valores e o número de linhas
total_snr = 0
total_rssi = 0
num_linhas = 0

# Calcular a soma dos valores
for line in data:
    # Converter a linha em um objeto JSON
    json_data = json.loads(line)
    
    # Extrair os valores de SNR e RSSI
    snr = json_data['snr']
    rssi = json_data['rssi']
    
    # Atualizar a soma total
    total_snr += snr
    total_rssi += rssi
    
    # Atualizar o contador de linhas
    num_linhas += 1

# Calcular a média
media_snr = total_snr / num_linhas
media_rssi = total_rssi / num_linhas

# Exibir os resultados
print(f'Média de SNR: {media_snr:.2f}')
print(f'Média de RSSI: {media_rssi:.2f}')
import json
import matplotlib.pyplot as plt
from datetime import datetime

# Ler os dados do arquivo JSON
with open('experimento4/all_data.json', 'r') as file:
    data = file.readlines()

# Converter cada linha do arquivo JSON em um dicionário
data = [json.loads(line) for line in data]

# Extrair os valores de rssi e ts
rssi_values = [d['rssi'] for d in data]
ts_values = [datetime.strptime(d['ts'], "%Y-%m-%d %H:%M:%S") for d in data]

# Criar o gráfico
plt.plot(ts_values, rssi_values)
plt.xlabel('Tempo')
plt.ylabel('RSSI')
plt.title('Gráfico de RSSI ao longo do tempo')
plt.xticks(rotation=45)
plt.show()
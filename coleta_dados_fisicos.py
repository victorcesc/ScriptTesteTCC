import json
import datetime
import matplotlib.pyplot as plt

# eraldo 30 de maio
# 14h32 - 14h53 - 750m
# 15h01 - 15h21 - 1100m
# 15h34 - 15h54 - 2020m
# 15h59 - 16h18 - 2500m

# eu dia 1 de junho
# 09h36 - 09h56 - 750m
# 10h04 - 10h20 - 935m
# 10h24 - 10h44 - 1980m
# 10h48 - 11h - 2710m


#eu dia 6 de junho
# 14h28 - 14h36 - 1260m
# 14h40 - 14h50 - 1530m
# 14h53 - 15h03 - 1760m
# 15h12 - 15h22 - 3050m

start_time = datetime.datetime(2023, 6, 13, 16, 18, 0)
end_time = datetime.datetime(2023, 6, 13, 16, 28, 0)

# with open('data.json') as f:
#     data = json.load(f)
data = []


with open('./dados_coletados/dados_indoor.json', 'r') as f:
    for line in f:
        # remove os espaços em branco e quebra de linha
        line = line.strip()
        print(line)
        # ignora linhas em branco
        if not line:
            continue
        
        # decodifica o primeiro objeto JSON
        data.append(json.loads(line))
        
        # decodifica o segundo objeto JSON
        # data2 = json.loads(line.split(',')[1])
        
        # faça algo com os dados decodificados
        # print(data1)
        # print(data2)

is_first = 0
start_counter = 0
end_counter = 0
packets_received = 0
# snr = []
# rssi = []
timestamps = []
with open("cozinha_90m.json", "a") as arquivo:
    for obj in data:
        timestamp = obj['rx_timestamp']
        timestamp_without_microseconds = timestamp.split('.')[0] + 'Z'
        # print(timestamp_without_microseconds)
        formatted_timestamp = datetime.datetime.strptime(timestamp_without_microseconds, '%Y-%m-%dT%H:%M:%SZ')
        # print(formatted_timestamp)
        #timestamp = datetime.datetime.strptime(obj['rx_timestamp'], '%Y-%m-%dT%H:%M:%S.%fZ')
        if start_time <= formatted_timestamp <= end_time:
            #counter
            packets_received += 1
            # print(obj['snr'])
            if 'snr' in obj:
                # snr.append(obj['snr'])
                snr = obj['snr']
            if 'rssi' in obj:
                rssi = obj['rssi']
            linha = f'{{"snr": {snr}, "rssi": {rssi}, "ts" : "{formatted_timestamp}"}}\n'
            arquivo.write(linha)
            timestamps.append((formatted_timestamp - start_time).total_seconds()/60)
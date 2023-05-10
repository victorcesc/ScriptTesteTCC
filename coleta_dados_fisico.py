import json
import datetime
import matplotlib.pyplot as plt

# 14:35 do dia 5 de maio no fuso UTC + 3
start_time = datetime.datetime(2023, 5, 4, 14, 35, 0)
end_time = datetime.datetime(2023, 5, 8, 14, 50, 0)

# with open('data.json') as f:
#     data = json.load(f)
data = []


with open('data1.json', 'r') as f:
    for line in f:
        # remove os espaços em branco e quebra de linha
        line = line.strip()
        
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
snr = []
rssi = []
timestamps = []
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
        snr.append(obj['snr'])
        rssi.append(obj['rssi'])
        timestamps.append((formatted_timestamp - start_time).total_seconds()/60)
        # print(packets_received)
        if is_first == 0:
            # print(obj)
            start_counter = obj['counter']
            print(start_counter)
            is_first = 1
        end_counter = obj['counter']

total_packets = end_counter - start_counter
total_packets += 1
loss_packets = total_packets - packets_received
packet_error_rate = (loss_packets/total_packets)*100

print("total packets ", total_packets)
print("packets received", packets_received)
print("loss packets", loss_packets)
print(rssi)

print("Taxa de erros de pacote : ", packet_error_rate, "%")

print(start_time)
print(end_time)

print(timestamps)

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))

ax1.plot(timestamps,snr, label = 'SNR')
ax2.plot(timestamps,rssi, label = 'RSSI')
ax1.set_xlabel('Tempo(min)')
ax1.set_ylabel('Valor')
ax2.set_xlabel('Tempo(min)')
ax2.set_ylabel('Valor')
ax3.set_ylim(packet_error_rate - 0.500 , packet_error_rate + 0.500)
ax3.bar('Taxa de erros de pacote',packet_error_rate)
plt.legend()
plt.show()
            
   # print(obj['rx_timestamp'])
        # print(type(obj[1]))

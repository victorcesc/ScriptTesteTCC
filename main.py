##
'''**.loRaNodes[*].**initialLoRaSF = int(uniform(7.0, 12.0))
**.loRaNodes[*].**initialLoRaTP = 14dBm
**.loRaNodes[*].**initialLoRaBW = 125 kHz
**.loRaNodes[*].**initialLoRaCR = 4
**.loRaNodes[*].**.initFromDisplayString = false
**.loRaNodes[*].**.evaluateADRinNode = true

**.loRaNodes[*].numApps = 1
**.loRaNodes[*].app[0].typename = "SimpleLoRaApp"
**.loRaNodes[*].initialX = uniform(0m, 1000m)
**.loRaNodes[*].initialY = uniform(0m, 1000m)'''

import pandas as pd
import matplotlib.pyplot as plt

# Leitura do arquivo CSV
data = pd.read_csv('test.csv')

# Linhas que possuem as informações da aplicacao dos nós"
nodes_app = data[data['module'].str.contains('LoRaNetworkTest\.loRaNodes\[\d+\]\.app\[0\]') & data['value'].notna()]

server_app = data[data['module'].str.contains('LoRaNetworkTest\.networkServer\.app\[0\]') & data['value'].notna()]
print(nodes_app)

print("-------------")
# Selecionar somente as linhas com "sentPackets" na coluna "type" e sem valores NaN na coluna "value"
linhas_sent_packets = nodes_app[(nodes_app['name'] == 'sentPackets') & (nodes_app['value'].notna())]
print(linhas_sent_packets)
linha_packets_received = server_app[(server_app['name'] == 'totalReceivedPackets') & (server_app['value'].notna())]

print("-------------")

sent_packets_values = linhas_sent_packets['value'].tolist()
packets_received = linha_packets_received['value'].tolist()
print(sent_packets_values)
print(packets_received)
total_packets = 0

for element in sent_packets_values:
    print(element)
    total_packets += int(element)

total_received_packets = int(packets_received[0])/total_packets
loss_packets = total_packets - int(packets_received[0]) 
packet_error_rate = (loss_packets/total_packets)*100
print("total received packets", total_received_packets, "%")
print("loss packets", loss_packets)
print("packet error rate", packet_error_rate, "%")
# Plotar um gráfico com a coluna 'value' versus a coluna 'count' das linhas encontradas
#linhas_sent_packets.plot(x='value', y='count', kind='scatter')

# Exibir o gráfico
#plt.show()
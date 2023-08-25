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
import math


file = 'caralho2.csv'
# Leitura do arquivo CSV
data = pd.read_csv(file)


# print("===================")
#LoRaNetworkTest.networkServer.eth[0].mac
linhas_server_mac = data[data['module'].str.contains('LoRaNetworkTest\.networkServer\.eth\[0\]\.mac') & data['value'].notna()]
simulated_time = linhas_server_mac[(linhas_server_mac['name'] == 'simulated time') & (linhas_server_mac['value'].notna())]
simulated_time = simulated_time['value'].tolist()
print('Tempo de simulacao: ', simulated_time[0])
# Linhas que possuem as informações da aplicacao dos nós"
nodes_app = data[data['module'].str.contains('LoRaNetworkTest\.loRaNodes\[\d+\]\.app\[0\]') & data['value'].notna()]
server_app = data[data['module'].str.contains('LoRaNetworkTest\.networkServer\.app\[0\]') & data['value'].notna()]


gw_posX = data[data['attrname'].str.contains('loRaGW\[\d+\]\.\**\.initialX') & data['attrvalue'].notna()]['attrvalue'].values
gw_posY = data[data['attrname'].str.contains('loRaGW\[\d+\]\.\**\.initialY') & data['attrvalue'].notna()]['attrvalue'].values


nodes_posX = nodes_app[nodes_app['name'].str.contains('positionX')]['value'].values
nodes_posY = nodes_app[nodes_app['name'].str.contains('positionY')]['value'].values


i = 0
j = 0
distancias_nodos = []
while i < len(nodes_posX):
    j = 0
    while j < len(gw_posX):
        distanciaX = float(nodes_posX[i]) - float(gw_posX[j][:-1])
        distanciaY = float(nodes_posY[i]) - float(gw_posY[0][:-1])
        print('Distancia X do Nodo {} do Gateway {}: {}'.format(i, j, distanciaX))
        print('Distancia Y do Nodo {} do Gateway {}: {}'.format(i, j, distanciaY))
        distancia_total = math.sqrt(distanciaX**2 + distanciaY**2)
        distancias_nodos.append(distancia_total)
        print('Distancia total do Nodo {} do Gateway {} é {}'.format(i, j, distancia_total))
        j = j + 1
    i = i + 1    


# Linhas que possuem as informações de consumo de energia do radio dos nós"
nodes_radio = data[data['module'].str.contains('LoRaNetworkTest\.loRaNodes\[\d+\]\.LoRaNic\.radio\.energyConsumer') & data['value'].notna()]
#print(nodes_radio)

print("-------------")
# Selecionar somente as linhas com "sentPackets" na coluna "type" e sem valores NaN na coluna "value"
linhas_sent_packets = nodes_app[(nodes_app['name'] == 'sentPackets') & (nodes_app['value'].notna())]
linhas_packets_received = server_app[(server_app['name'] == 'totalReceivedPackets') & (server_app['value'].notna())]

# Selecionar somente as linhas que mostram o consumo de energia em joules
energy_consume_values = nodes_radio[(nodes_radio['name'] == 'totalEnergyConsumed') & (nodes_radio['value'].notna())]

print("-------------")

## Energy consume in watts

energy_consume_values = energy_consume_values['value'].tolist()
#print(energy_consume_values)
energy_consumed_watts = []
total_energy_consumed = 0
for element in energy_consume_values:
    energy_in_watts = float(element)/int(simulated_time[0])
    total_energy_consumed += float(element)
    print(energy_in_watts, "W")
    energy_consumed_watts.append(energy_in_watts)

total_energy_consumed = total_energy_consumed/int(simulated_time[0])
nodos = [f'Nodo {i+1}' for i in range(len(energy_consumed_watts))]

print("MEDIA DE ENERGIA CONSUMIDA : ", total_energy_consumed/len(energy_consumed_watts))

plt.figure(1)
plt.bar(nodos, energy_consumed_watts)
#plt.set_title('Energia consumida por nodo',fontsize=8)
plt.ylabel('W',fontsize=8)
plt.figure(2)
plt.bar("Media de energia consumida", total_energy_consumed/len(energy_consumed_watts))
#ax2.set_title('Avg Energy Consumed',fontsize=8)
plt.ylabel('W',fontsize=8)
# plt.bar(nodos, energy_consumed_watts)
# plt.xlabel('Nodo')
# plt.ylabel('Energia consumida (W)')
# plt.title('Energia consumida por nodo na rede LoRa')
#plt.show()



# Packet error rate



sent_packets_values = linhas_sent_packets['value'].tolist()
packets_received = linhas_packets_received['value'].tolist()
total_packets = 0

for element in sent_packets_values:
    total_packets += int(element)

print("Total de pacotes enviados pelos nodos : ", total_packets)
print("Total de pacotes recebidos pelos servidor : ", packets_received[0])
total_received_packets = int(packets_received[0])/total_packets
loss_packets = total_packets - int(packets_received[0]) 
packet_error_rate = (loss_packets/total_packets)*100

print("Taxa de erros de pacote : ", packet_error_rate, "%")
plt.figure(3)
plt.ylim(0, 100)
plt.bar('Taxa de erros de pacote', packet_error_rate)
plt.ylabel('%')
plt.figure(4)
plt.bar(nodos,distancias_nodos)
plt.title('Distancia de cada nodo do GW',fontsize=8)
plt.ylabel('m',fontsize=8)
#ax3.set_title('Packet error rate',fontsize=8)


# Exibir as janelas de gráfico separadamente
plt.show()
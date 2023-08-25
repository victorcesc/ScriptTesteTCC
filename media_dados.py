import csv

snr = []
rssi = []
def ler_csv(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        for linha in leitor_csv:
            distancia = linha['distancia']
            if distancia == '40':
                rssi.append(float(linha['rssi']))
                snr.append(float(linha['snr'])) 
            # Faça o que desejar com os valores lidos
            # por exemplo, imprimir no console:
                print(f"Distância: {distancia}, RSSI: {linha['rssi']}, SNR: {linha['snr']}")

# Exemplo de uso:
nome_arquivo = 'dados.csv'  # Substitua pelo nome do seu arquivo CSV
ler_csv(nome_arquivo)

media_rssi = sum(rssi)/len(rssi)
print(media_rssi)
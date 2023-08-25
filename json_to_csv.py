
import pandas as pd
import json
import os
# Ler o arquivo JSON
dados = []
path_in = 'experimento2-indoor/Setor_transporte_1andar_55m.json'
path_out = 'dados_indoor_corrigidos.csv'

# 750, 1100, 

with open(path_in, 'r') as f:
    for linha in f:
        # Carregar o JSON da linha atual
        print(linha)
        json_obj = json.loads(linha)
        print(json_obj)
        # Adicionar a coluna "distancia" fixa em 600 aos dados
        json_obj['distancia'] = 56.5
        
        # Adicionar o objeto JSON na lista de dados
        dados.append(json_obj)

# Criar um DataFrame com os dados
df = pd.DataFrame(dados)

# Reordenar as colunas
df = df[['distancia', 'rssi', 'snr']]

# Salvar o DataFrame como um arquivo CSV
if os.path.exists(path_out) :
    df.to_csv(path_out, mode='a', index=False, header=False)
else: 
    df.to_csv(path_out, index=False)
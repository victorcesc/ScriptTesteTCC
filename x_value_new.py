import math

medias = [-102.125, -101.575, -105.4875, -105.7875, -108.6]
desvios_padrao = [14.328184637280467, 14.43, 12.93, 11.68, 9.14]

# Calcular a soma dos desvios quadrados ponderados
soma_desvios_quadrados_ponderados = sum([(desvio ** 2) * (len(medias) - 1) for desvio in desvios_padrao])

# Calcular o fator de normalização
fator_normalizacao = sum([len(medias) - 1])

# Calcular o desvio padrão combinado
desvio_padrao_combinado = math.sqrt(soma_desvios_quadrados_ponderados / fator_normalizacao)

print(f"O desvio padrão combinado das medidas é: {desvio_padrao_combinado}")
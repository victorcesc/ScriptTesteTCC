# Configurações iniciais da placa ESP RoboCore

## Configuração do appeui, deveui e appkey

As configurações do `appeui`, `deveui` e `appkey` devem ser definidas de acordo com as especificações do servidor LoRaWAN que está sendo utilizado.

## Configuração da região e dos canais

Para configurar a região e os canais, foram realizados os seguintes passos:

1. Utilizou-se o comando `AT+REGION <região>` para configurar a região da placa ESP RoboCore. A região escolhida foi a Australia (AU915 = 1).

2. Desativaram-se todos os canais utilizando o comando `AT+CH <canal> status=0`.

3. Ativaram-se os canais 9 a 16 e o canal 60 utilizando o comando `AT+CH <canal> status=1`.

## Configuração do spread factor e duty cycle

O spread factor e o duty cycle foram configurados de forma que o tempo médio de ocupação de qualquer frequência não seja superior a 0,4 segundos num intervalo de 14 segundos.

Para isso, utilizou-se o seguinte comando: `AT+DR 5`. O valor escolhido para configura o spread factor para 7 e a largura de banda para 125kHz.

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


```
//Verifica se o modelo de placa selecionado esta correto
#if !defined(ARDUINO_ESP32_DEV) // ESP32
#error Use this example with the ESP32
#endif

//Inclusao da biblioteca
#include "RoboCore_SMW_SX1276M0.h"

//Declaracao dos pinos de comunicacao serial do Kit
#include <HardwareSerial.h>
HardwareSerial LoRaSerial(2);
#define RXD2 16
#define TXD2 17

//Criacao do objeto lorawan para a biblioteca SMW_SX1276M0
SMW_SX1276M0 lorawan(LoRaSerial);

//Declaracao da variavel que armazena as respostas do modulo
CommandResponse resposta;

unsigned long intervalo;
int count = 1;

//Declaracao das variaveis que armazenam as informacoes da rede
const char APPEUI[] = "0AC17911E4534CF9"; //Application EUI
const char APPKEY[] = "B651D286D11A7DB3A66218EBD8353CD6"; //Application Key
const char DEVEUI[] = "BA8C371935604693";

void setup() {
  //Inicia o monitor serial e imprime o cabecalho
  Serial.begin(115200);
  Serial.println(F("--- SMW_SX1276M0 Bridge ---"));

  //Definicao do pino de reset do modulo
  lorawan.setPinReset(5);
  lorawan.reset(); //Realiza um reset no modulo
  
  //Inicia a comunicacao serial com o modulo
  LoRaSerial.begin(115200, SERIAL_8N1, RXD2, TXD2);

  //Ve qual valor setado para ADR
  uint8_t adr; 
  resposta = lorawan.get_ADR(adr);
  Serial.print(F("Valor do ADR : "));
  Serial.println(adr);

  resposta = lorawan.set_AppEUI(APPEUI);  
  if(resposta == CommandResponse::OK){
    Serial.print(F("Application EUI configurado ("));
    Serial.write((uint8_t *)APPEUI, 16);
    Serial.println(')');
  } else {
    Serial.println(F("Erro ao configurar o Application EUI"));
  }

  //seta o DEVEUI caso a placa tenha resetado as configurações
   resposta = lorawan.set_DevEUI(DEVEUI);  
  if(resposta == CommandResponse::OK){
    Serial.print(F("Dev EUI configurado ("));
    Serial.write((uint8_t *)DEVEUI, 16);
    Serial.println(')');
  } else {
    Serial.println(F("Erro ao configurar o Dev EUI"));
  }


  //configura o ADR para inativo
  resposta = lorawan.set_ADR(0);
  if(resposta == CommandResponse::OK){
    Serial.println(F("ADR configurado (0)"));   
  } else {
    Serial.println(F("Erro ao configurar o ADR"));
  }

  //Configura o Application Key no modulo
  resposta = lorawan.set_AppKey(APPKEY);
  if(resposta == CommandResponse::OK){
    Serial.print(F("Application Key configurado ("));
    Serial.write((uint8_t *)APPKEY, 32);
    Serial.println(')');
  } else {
    Serial.println(F("Erro ao configurar o Application Key"));
  }

  //Configura o modo de operação para OTAA
  resposta = lorawan.set_JoinMode(SMW_SX1276M0_JOIN_MODE_OTAA);
  if(resposta == CommandResponse::OK){
    Serial.println(F("Metodo de Conexao Configurado como OTAA"));
  } else {
    Serial.println(F("Erro ao configurar o metodo OTAA"));
  }

  //Requisita conexao com a rede
  Serial.println(F("Conectando a Rede"));
  lorawan.join();
  
}

void loop() {
  lorawan.listen(); 
  if(lorawan.isConnected()){
    
    if(intervalo < millis()){
      uint8_t msg;
      resposta = lorawan.get_ADR(msg);
      char mensagem[32];
      sprintf(mensagem,"Valor do ADR =============== %d", msg);
      Serial.println("Connected");
      Serial.print("Mensagem : ");
      Serial.println(mensagem);
      resposta = lorawan.sendT(1,mensagem);
      intervalo = millis() + 30000;
    }
    
  }else{
    //Imprime um "." a cada 5 segundos
    if(intervalo < millis()){
      Serial.println('.');
      intervalo = millis() + 5000; //Atualiza a contagem de tempo
    }
  }
  
}
```
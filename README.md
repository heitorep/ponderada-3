# 🚗 Integração do Sistema de aluguel de veículos autônomos

## 📌 Visão Geral
Este repositório documenta e implementa um fluxo de integração como código para um sistema de aluguel de veículos autônomos. O sistema conecta serviços de telemetria, pagamento, gestão de frotas e controle de identidade para permitir uma experiência segura e eficiente.

## 🏗 Arquitetura
A arquitetura segue uma abordagem modular, dividida nos seguintes componentes:

### 🔹 Camadas e componentes
- **API Gateway**: Interface que recebe requisições dos usuários e direciona para os módulos corretos.
- **Autenticação e identificação**: Valida identidade do usuário antes da locação.
- **Gestão de frotas**: Controla a disponibilidade dos veículos.
- **Serviço de pagamento**: Processa pagamentos e confirma transação.
- **Telemetria**: Coleta dados do carro e garante que ele está apto para a viagem.
- **Monitoramento e relatórios**: Registra o status da viagem e do veículo.

## 🔄 Fluxo de integração
1. O usuário solicita um veículo pelo aplicativo.
2. O sistema valida a identidade e histórico do cliente.
3. O serviço de gestão de frotas verifica a disponibilidade do veículo mais próximo.
4. O serviço de telemetria confirma que o veículo está apto para uso.
5. O usuário confirma o pagamento.
6. O veículo é liberado e se desloca até o ponto de retirada.
7. O sistema acompanha a viagem em tempo real.
8. Ao final, um relatório é gerado e armazenado.

## 🛠 Controle de qualidade da integração
Para garantir a qualidade da integração, adotamos os seguintes controles:

### ⏳ Tempos e Desempenho
- **Autenticação**: < 500ms
- **Verificação de frota**: < 1s
- **Confirmação de pagamento**: < 2s
- **Telemetria do veículo**: Tempo real (< 100ms de atraso)

### 📡 Protocolos utilizados
- REST APIs para comunicação entre serviços.
- WebSockets para atualização em tempo real.
- Banco de dados relacional para registros e análise histórica.

### ⚠️ Tratamento de exceções
- **Veículo indisponível** → O sistema sugere outro modelo similar.
- **Falha no pagamento** → O usuário é notificado e pode tentar outro método.
- **Problemas na telemetria** → O carro é retirado do sistema até resolução.

## 📡 APIs e comunicação
### Exemplo de endpoint para verificação de frota
```http
GET /api/fleet/availability?location=lat,long
```
#### Resposta esperada:
```json
{
  "available": true,
  "vehicle_id": "V12345",
  "model": "Autonomous Sedan X"
}
```

### Exemplo de endpoint para pagamento
```http
POST /api/payment/confirm
```

#### Corpo da requisição:
```json
{
  "user_id": "U98765",
  "vehicle_id": "V12345",
  "amount": 150.00
}
```

#### Resposta esperada:
```json
{
  "status": "approved",
  "transaction_id": "T67890"
}
```
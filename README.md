# Solução de Dados em Tempo Real – Squad de Pedidos

## 📌 Objetivo
Desenhar uma arquitetura de dados em tempo real para apoiar a squad de pedidos na captura e análise dos eventos transacionais gerados pela aplicação de pedidos.

## 🧩 Visão Geral da Solução

A solução proposta contem:
- Emissão de eventos pela aplicação de pedidos
- Ingestão em tempo real com Azure Event Hub
- Processamento contínuo com Databricks Structured Streaming
- Armazenamento no Delta Lake em três camadas (Bronze, Silver e Gold)
- Consumo dos dados via dashboards (Power BI), alertas (Azure Monitor) ou APIs

![Diagrama da Solução](....)

## 🏗️ Arquitetura

### 1. Aplicação de Pedidos
Responsável por emitir eventos de pedidos via API no formato JSON.

### 2. Azure Event Hub
Serviço de mensageria em tempo real que recebe os eventos da aplicação. Alta escalabilidade e integração nativa com o Azure.

### 3. Azure Databricks – Structured Streaming
Lê os dados em tempo real do Event Hub, processa e armazena em Delta Lake.

### 4. Delta Lake
- *Bronze*: dados crus, versão original dos eventos
- *Silver*: dados limpos, com normalizações e enriquecimentos
- *Gold*: dados prontos para consumo analítico

### 5. Camadas de Consumo
- Power BI (dashboards)
- Azure Monitor (notificações)
- APIs para integrações

## 💻 Exemplo de Código

Arquivo stream_ingestao_pedidos.py: exemplo de leitura do Event Hub e gravação em Delta Lake com PySpark.

[.....](code/stream_ingestao_pedidos.py)

## ⚙️ Stack de Tecnologias

| Componente            | Tecnologia                | Justificativa |
|-----------------------|---------------------------|----------------|
| Ingestão de Eventos   | Azure Event Hub           | Escalável, nativo do Azure |
| Processamento         | Databricks Structured Streaming (PySpark) | Integração com Event Hub e Delta Lake |
| Armazenamento         | Delta Lake (Bronze, Silver, Gold) | Governança e versionamento |
| Visualização/Alertas  | Power BI, Azure Monitor   | Pronto para uso em real time |

## 👩‍💻 Sobre mim

Case desenvolvido por Raquel Elias Zanatta Banuth para a vaga de Data Analytics Engineer 

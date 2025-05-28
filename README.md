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

! [Diagrama da Solução](docs/Raquel_diagrama.pdf)

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

> ⚠️ Por se tratar de um case técnico sem acesso ao ambiente real do Azure Databricks, a ingestão foi simulada com leitura de arquivos JSON em um diretório, eu criei uma pasta de input na minha máquina, salvei alguns arquivos .json com estrutura semelhante ao schema que coloquei no arquivo abaixo e copiei esses arquivos aos poucos para a pasta (testei com cerca de 40 segundos) para simular eventos chegando. Essa abordagem reproduz o comportamento de streaming com base na chegada de arquivos e permite testar a logica de transformação e escrita de dados de forma que seja minimamente parecida com o ambiente real ⚠️

## 💻 Exemplo de Código

[Trecho de Código](code/stream_ingestion_pedidos.py)

## 🧩 O que meu código precisa fazer 🧩
- *1*: *Conectar ao Event hub* (simulado)
- *2*: *Ler os dados em tempo real* (com Structured Streaming)
- *3*: *Converter os dados de JSON para colunas*
- *4*: *Gravar no delta lake* (camada bronze, dados raw)

## ⚙️ Stack de Tecnologias

| Componente            | Tecnologia                | Justificativa |
|-----------------------|---------------------------|----------------|
| Ingestão de Eventos   | Azure Event Hub           | Escalável, nativo do Azure |
| Processamento         | Databricks Structured Streaming (PySpark) | Integração com Event Hub e Delta Lake |
| Armazenamento         | Delta Lake (Bronze, Silver, Gold) | Governança e versionamento |
| Visualização/Alertas  | Power BI, Azure Monitor   | Pronto para uso em real time |


> ⚠️ Ponto de atenção: A ingestão em tempo real utiliza arquivos JSON monitorados por Spark Strutured Streaming. Por padrão, o Spark apenas processa **novos arquivos** que aparecem nessa pasta monitorada. Se um arquivo for modificado após já ter sido processado, ele não será processado automaticamente. Esse comportamento segue o padrão de uso com o checkpoint para garantir consistência no consumo de dados. ⚠️

## 👩‍💻 Sobre mim

Case desenvolvido por Raquel Elias Zanatta Banuth para a vaga de Data Analytics Engineer 

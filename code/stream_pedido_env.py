import os
from pyspark.sql.types import StructType, StringType, IntegerType, DoubleType
from pyspark.sql.functions import col, year, month, dayofmonth
from dotenv import load_dotenv

# Carregando aqui as variáveis do .env
load_dotenv("/mnt/data/.env")

INPUT_PATH = os.getenv("INPUT_PATH")
DELTA_OUTPUT_PATH = os.getenv("DELTA_OUTPUT_PATH")
CHECKPOINT_PATH = os.getenv("CHECKPOINT_PATH")
ENVIRONMENT = os.getenv("ENVIRONMENT")

# Schema baseado no dataset do Kaggle disponibilizado
pedido_schema = StructType() \
    .add("InvoiceNo", StringType()) \
    .add("StockCode", StringType()) \
    .add("Description", StringType()) \
    .add("Quantity", IntegerType()) \
    .add("InvoiceDate", StringType()) \
    .add("UnitPrice", DoubleType()) \
    .add("CustomerID", StringType()) \
    .add("Country", StringType())

# Leitura do stream de arquivos JSON
pedidos_stream = spark.readStream \
    .schema(pedido_schema) \
    .json(INPUT_PATH)

# Ação de acordo com o ambiente
if ENVIRONMENT == "develop":
    # Apenas imprime no console
    query = pedidos_stream.writeStream \
        .format("console") \
        .outputMode("append") \
        .option("truncate", False) \
        .start()
else:
    # Adiciona colunas de partição (por exemplo data extraída de InvoiceDate)
    from pyspark.sql.functions import to_timestamp
    pedidos_particionados = pedidos_stream.withColumn(
        "InvoiceDateTS", to_timestamp("InvoiceDate", "d/M/yyyy H:mm")
    ).withColumn("year", year("InvoiceDateTS")) \
     .withColumn("month", month("InvoiceDateTS")) \
     .withColumn("day", dayofmonth("InvoiceDateTS"))

    # Escreve no Delta Lake com particionamento
    query = pedidos_particionados.writeStream \
        .format("delta") \
        .partitionBy("year", "month", "day") \
        .outputMode("append") \
        .option("checkpointLocation", CHECKPOINT_PATH) \
        .start(DELTA_OUTPUT_PATH)

query.awaitTermination()

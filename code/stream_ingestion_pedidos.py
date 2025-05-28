from pyspark.sql.types import StructType, StringType, IntegerType, DoubleType
from pyspark.sql.functions import col

# Schema baseado no dataset do Kaggle
pedido_schema = StructType() \
    .add("InvoiceNo", StringType()) \
    .add("StockCode", StringType()) \
    .add("Description", StringType()) \
    .add("Quantity", IntegerType()) \
    .add("InvoiceDate", StringType()) \
    .add("UnitPrice", DoubleType()) \
    .add("CustomerID", StringType()) \
    .add("Country", StringType())

# Caminho para os arquivos JSON simulando eventos chegando
input_path = "\Weback\Desktop\json_pedidos_simulados_case_JS" ## nesse momento fui copiando outros arquivos para dentro da mesma pagina (com aproximadamente 40 segundos) com isso o readStream vai detectar automaticamente e processar os arquivos

# Leitura contínua dos arquivos JSON
pedidos_stream = spark.readStream \
    .schema(pedido_schema) \
    .json(input_path)

# Exibir no console (para testes, sem salvar)
query = pedidos_stream.writeStream \
    .format("console") \
    .outputMode("append") \
    .option("truncate", False) \
    .start()

query.awaitTermination()

from pyspark.sql import SparkSession, DataFrame


def load_data(spark: SparkSession, path: str , header: bool, inferSchema: bool) -> DataFrame:
    data = spark.read.csv(path = path, header = header, inferSchema = inferSchema)
    return data
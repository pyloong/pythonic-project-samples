from pyspark.sql import SparkSession


def _table_exists(spark: SparkSession, table: str) -> bool:
    db, table_name = table.split(".", maxsplit=1)
    return table_name in [t.name for t in spark.catalog.listTables(db)]

"""Spark Init"""
from dynaconf.base import Settings
from pyspark.sql import SparkSession


def init_spark(settings: Settings, app_name: str):
    """Create spark session"""
    spark_builder = (SparkSession.builder
                     .master(settings.spark_master)
                     .appName(app_name))
    # Spark settings load
    for key, val in settings.spark_config.items():
        spark_builder.config(key, val)
    # Spark session create
    spark_session = spark_builder.getOrCreate()
    return spark_session

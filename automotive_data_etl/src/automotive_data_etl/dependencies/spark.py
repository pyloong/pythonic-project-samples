"""Spark Init and Spark Log4j class"""
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


class SparkLog4j:
    """Wrapper class for Log4j JVM object.
    Please setting default log level to "WARN".
    :param spark: SparkSession object.
    """

    def __init__(self, spark: SparkSession):
        # get spark app details with which to prefix all messages
        conf = spark.sparkContext.getConf()
        app_id = conf.get('spark.app.id')
        app_name = conf.get('spark.app.name')
        spark.sparkContext.setLogLevel('info')
        log4j = spark._jvm.org.apache.log4j
        message_prefix = '<' + app_name + ' ' + app_id + '>'
        self.logger = log4j.LogManager.getLogger(message_prefix)

    def error(self, message):
        """Log an error.
        :param: Error message to write to log
        :return: None
        """
        self.logger.error(message)

    def warn(self, message):
        """Log a warning.
        :param: Warning message to write to log
        :return: None
        """
        self.logger.warn(message)

    def info(self, message):
        """Log information.
        :param: Information message to write to log
        :return: None
        """
        self.logger.info(message)

"""logging"""
from pyspark.sql import SparkSession


class Log4j:
    """Wrapper class for Log4j JVM object.
    Please setting default log level to "WARN".
    :param spark: SparkSession object.
    """

    def __init__(self, spark: SparkSession):
        # get spark app details with which to prefix all messages
        conf = spark.sparkContext.getConf()
        app_id = conf.get('spark.app.id')
        app_name = conf.get('spark.app.name')
        spark.sparkContext.setLogLevel('warn')
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

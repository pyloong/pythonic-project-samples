"""Context"""
from dynaconf.base import Settings

from automotive_data_etl.constants import ENV_DEVELOPMENT
from automotive_data_etl.dependencies.config import settings
from automotive_data_etl.dependencies.spark import init_spark
from automotive_data_etl.dependencies.spark import SparkLog4j


class Context:
    _instance = None
    environment = ENV_DEVELOPMENT

    def __new__(cls):
        """Singleton mode"""
        if cls._instance is None:
            cls._instance = super(Context, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        """Context Parameters"""
        self.settings: Settings = settings.from_env(self.environment)

    def get_spark_session(self):
        """Get spark session"""
        return init_spark(self.settings, app_name='etl_template')

    def get_spark_logger(self) -> SparkLog4j:
        """Get the initialized Spark log object"""
        spark = self.get_spark_session()
        return SparkLog4j(spark)

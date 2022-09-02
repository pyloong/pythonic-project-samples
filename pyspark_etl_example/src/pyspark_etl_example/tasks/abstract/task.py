from abc import ABC, abstractmethod

from dynaconf.base import Settings
from pyspark.sql import SparkSession, DataFrame

from pyspark_etl_example.dependecies.log import Log4j


class AbstractTask(ABC):
    """
    Base class to read a dataset, transform it, and save it to a table.
    """

    def __init__(self, spark: SparkSession, settings: Settings, logger: Log4j):
        self.spark = spark
        self.settings = settings
        self.logger = logger

    def run(self) -> None:
        df = self._input()
        df_transformed = self._transform(df)
        self._output(df_transformed)

    @abstractmethod
    def _input(self) -> DataFrame:
        """Load data from file/database/other format."""
        raise NotImplementedError

    @abstractmethod
    def _transform(self, df: DataFrame) -> DataFrame:
        raise NotImplementedError

    @abstractmethod
    def _output(self, df: DataFrame) -> None:
        raise NotImplementedError

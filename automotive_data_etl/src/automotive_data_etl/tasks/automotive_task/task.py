"""Processing car tmp task."""
import logging

from pyspark.sql import DataFrame

from automotive_data_etl.tasks.abstract.task import AbstractTask
from automotive_data_etl.tasks.automotive_task.automotive_transform import AutomotiveDataTransform


class AutomotiveDataTask(AbstractTask):
    """Processing car tmp task."""

    def __init__(self):
        super().__init__()
        self.spark = self.ctx.get_spark_session()

    def _extract(self) -> DataFrame:
        """Read CSV file return DataFrame"""
        df: DataFrame = self.spark.read.csv(
            self.settings.input_path,
            encoding='utf-8',
            header=True,
            inferSchema=True
        )
        logging.info(f'Extract tmp from {self.settings.input_path}')
        return df

    def _transform(self, df: DataFrame) -> DataFrame:
        """execute CarTransform transform function"""
        return AutomotiveDataTransform().transform(df)

    def _load(self, df: DataFrame) -> None:
        """Load final tmp to output path"""
        df.write.json(self.settings.output_path, mode='overwrite', encoding='utf-8')
        logging.info(f'Load tmp to {self.settings.output_path}')

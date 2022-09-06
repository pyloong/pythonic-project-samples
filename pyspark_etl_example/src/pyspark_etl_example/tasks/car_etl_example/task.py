"""Processing car data task."""
from pyspark.sql import DataFrame

from pyspark_etl_example.tasks.abstract.task import AbstractTask
from pyspark_etl_example.tasks.car_etl_example.car_transform import \
    CarTransform


class CarDataTask(AbstractTask):
    """Processing car data task."""

    def _input(self) -> DataFrame:
        """Read CSV file return DataFrame"""
        print(self.settings)
        df: DataFrame = self.spark.read.csv(
            self.settings.input_path,
            encoding='utf-8',
            header=True,
            inferSchema=True
        )
        self.logger.warn(f'Extract data from {self.settings.input_path}')
        return df

    def _transform(self, df: DataFrame) -> DataFrame:
        """execute CarTransform transform function"""
        return CarTransform().transform(df)

    def _output(self, df: DataFrame) -> None:
        """Load final data to output path"""
        df.show()
        df.write.json(self.settings.output_path, mode='overwrite', encoding='utf-8')
        self.logger.warn(f'Load data to {self.settings.output_path}')

"""Car data Transformation."""
from functools import reduce

from pyspark.sql import DataFrame
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType

from pyspark_etl_example.tasks.abstract.transform import AbstractTransform


class CarTransform(AbstractTransform):
    """Car data Transformation."""

    def transform(self, df: DataFrame) -> DataFrame:
        """Execute the transform process"""
        transformations = (
            self._filter_price,
            self._process_car_name,
            self._select_final_columns,
        )
        return reduce(DataFrame.transform, transformations, df)  # type: ignore

    @staticmethod
    def _filter_price(df: DataFrame) -> DataFrame:
        return df.filter(col('price') > 1000)

    @staticmethod
    def _process_car_name(df: DataFrame) -> DataFrame:
        """Clean [dirty data] from CarName"""
        res_df = df.withColumn('CarName', _name_replace_udf(col('CarName')).alias('CarName'))
        return res_df

    @staticmethod
    def _select_final_columns(df: DataFrame) -> DataFrame:
        """Car price data dataframe select final columns"""
        return df.select(
            col('car_ID').alias('car_id'),
            col('symboling'),
            col('CarName').alias('car_name'),
            col('price'),
        )


@udf(returnType=StringType())
def _name_replace_udf(car_name):
    """Clean [dirty data] udf"""
    if not car_name:
        return None
    err_str = '[dirty data]'
    if err_str not in car_name:
        return car_name
    car_name = car_name.replace(err_str, '')
    return car_name

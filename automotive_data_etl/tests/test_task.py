"""Test log"""
import pytest
from pyspark.sql.functions import col

from automotive_data_etl.context import Context
from automotive_data_etl.tasks.automotive_task.automotive_transform import AutomotiveDataTransform
from automotive_data_etl.tasks.automotive_task.task import AutomotiveDataTask


@pytest.fixture()
def context():
    """Fixture context for the tests"""
    Context().environment = 'testing'
    ctx = Context()
    return ctx


def test_settings(context):
    """Test: Setting init by "testing" env"""
    settings = context.settings

    assert settings.message == 'This is in testing env'

    # tmp path
    assert settings.input_path == '../tmp/input/car_price.csv'
    assert settings.output_path == '../tmp/output'

    # spark configs
    assert settings.spark_master == 'local[*]'
    assert settings.spark_config.spark.driver.memory == '3G'
    assert settings.spark_config.spark.executor.memory == '16G'
    assert settings.spark_config.spark.sql.debug.maxToStringFields == 100


@pytest.fixture()
def test_extract(context):
    """Test: Read CSV file return DataFrame"""
    task = AutomotiveDataTask()
    df = task._extract()

    assert df.count() == 205

    return df


@pytest.fixture()
def test_transform_filter_price(test_extract):
    """Test: Filter results price > 10000"""
    transform = AutomotiveDataTransform()
    df = transform._filter_price(test_extract)

    assert df.filter(col('price') <= 10000).count() == 0

    return df


@pytest.fixture()
def test_transform_process_car_name(test_transform_filter_price):
    """Test: Clean [dirty tmp] from CarName"""
    transform = AutomotiveDataTransform()
    df = transform._process_car_name(test_transform_filter_price)

    assert df.filter(col('CarName').contains('[dirty tmp]')).count() == 0

    return df


@pytest.fixture()
def test_transform_select_final_columns(test_transform_process_car_name):
    """Test: Final columns is ['car_id', 'car_name', 'symboling',  'price']"""
    final_columns = ['car_id', 'car_name', 'symboling', 'price']
    transform = AutomotiveDataTransform()
    df = transform._select_final_columns(test_transform_process_car_name)
    names = df.schema.names

    assert names.sort() == final_columns.sort()

    return df


def test_load(test_transform_select_final_columns):
    """Test: Load csv file"""
    task = AutomotiveDataTask()
    task._load(test_transform_select_final_columns)

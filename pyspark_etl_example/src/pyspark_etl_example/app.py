"""Project executor"""
import argparse

from stevedore import ExtensionManager

from pyspark_etl_example.constants import TASK_NAMESPACE
from pyspark_etl_example.dependecies.config import settings
from pyspark_etl_example.dependecies.log import Log4j
from pyspark_etl_example.dependecies.spark import init_spark
from pyspark_etl_example.executor import Executor


def _parse_args() -> argparse.Namespace:
    """Parameter parsing"""
    parser = argparse.ArgumentParser(allow_abbrev=False)
    # parser add arguments
    parser.add_argument(
        "--env",
        required=False,
        choices=['development', 'testing', 'production'],
        default="development"
    )
    parser.add_argument(
        "--task",
        required=True,
        choices=_get_task_list()
    )
    return parser.parse_args()


def _get_task_list():
    """Get task list by namespace"""
    extension_manager = ExtensionManager(namespace=TASK_NAMESPACE, invoke_on_load=False)
    return extension_manager.entry_points_names()


def main() -> None:
    """
    Parse args, init spark, init logger and executor task run.
    """
    args = _parse_args()
    __settings = settings.from_env('args.env')
    spark = init_spark(__settings, args.task)
    logger = Log4j(spark)
    logger.warn('etl job init success.')
    logger.warn(f'env configs options: {__settings.message}')
    Executor(spark, __settings, logger, args.task).run()


if __name__ == "__main__":
    main()

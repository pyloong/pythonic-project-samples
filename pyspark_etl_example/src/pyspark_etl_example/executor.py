"""
Loads a Task class and calls its `run()` method.
"""
from typing import Callable

from dynaconf.base import Settings
from pyspark.sql import SparkSession
from stevedore import ExtensionManager

from pyspark_etl_example.constants import TASK_NAMESPACE
from pyspark_etl_example.dependecies.log import Log4j
from pyspark_etl_example.utils.exception import PluginNotFoundError


class Executor:
    """
    Loads a Task class and calls its `run()` method.
    """

    def __init__(self, spark: SparkSession, settings: Settings, logger: Log4j, task: str):
        self.spark = spark
        self.settings = settings
        self.task = task
        self.logger = logger

    def run(self) -> None:
        task_class = self._load_task(TASK_NAMESPACE, self.task)
        self.logger.warn(f"Running task: {task_class}")
        task_class(self.spark, self.logger, self.settings).run()

    def _load_task(self, namespace: str, name: str) -> Callable:
        """Get extension by name from namespace."""
        extension_manager = ExtensionManager(namespace=namespace, invoke_on_load=False)
        for ext in extension_manager.extensions:
            if ext.name == name:
                return ext.plugin
            self.logger.warn(f'Load plugin: {ext.plugin} in namespace "{namespace}"')
        raise PluginNotFoundError(namespace=namespace, name=name)
